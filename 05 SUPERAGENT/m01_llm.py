"""M01 semantic extractor adapter for SUPERAGENT MVP.

The adapter is source/task agnostic. It accepts a SOURCE_PACKAGE containing
source fragments and asks an OpenAI-compatible chat-completions endpoint to
produce Extraction Records. The orchestration kernel remains deterministic;
semantic extraction is delegated to this adapter.

Required environment for a live run:
  LLM_API_KEY
  LLM_MODEL
Optional:
  LLM_BASE_URL (default: https://api.openai.com/v1)
""" 
from __future__ import annotations

import json
import os
import urllib.request
from typing import Any, Dict, List


M01_SYSTEM_PROMPT = """You are MACHINE-SOURCE-001 executing TASK M01 EXTRACTION.

Extract engineering-relevant observations from ONLY the supplied SOURCE_PACKAGE.
Do not add external knowledge, interpretation, synthesis, or CMOC canonization.

For every observation return:
- id: EX-###
- location: exact supplied source location
- observation: faithful source-grounded observation
- source_quote_or_evidence: short evidence from the supplied fragment
- uncertainty: CLEAR or UNCERTAIN
- source_id

Return JSON only:
{"records":[...]}
Do not invent locations or evidence. If a fragment does not support a
reliable observation, omit it rather than filling the gap.
"""


class M01LLMError(RuntimeError):
    pass


def _request_json(payload: Dict[str, Any], timeout: int = 120) -> Dict[str, Any]:
    api_key = os.environ.get("LLM_API_KEY")
    model = os.environ.get("LLM_MODEL")
    base_url = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/")

    if not api_key:
        raise M01LLMError("LLM_API_KEY is not set")
    if not model:
        raise M01LLMError("LLM_MODEL is not set")

    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        raise M01LLMError(f"LLM request failed: {exc}") from exc


def extract(source_package: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Execute semantic M01 against the supplied source package."""
    fragments = source_package.get("fragments", [])
    if not fragments:
        raise M01LLMError("SOURCE_PACKAGE has no fragments")

    user_payload = {
        "source_id": source_package["source_id"],
        "source_name": source_package.get("source_name", ""),
        "source_version": source_package.get("source_version", ""),
        "fragments": fragments,
    }

    response = _request_json({
        "model": os.environ["LLM_MODEL"],
        "temperature": 0,
        "messages": [
            {"role": "system", "content": M01_SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)},
        ],
    })

    try:
        content = response["choices"][0]["message"]["content"]
        parsed = json.loads(content)
        records = parsed["records"]
    except (KeyError, TypeError, json.JSONDecodeError) as exc:
        raise M01LLMError(f"Invalid M01 JSON response: {exc}") from exc

    if not isinstance(records, list):
        raise M01LLMError("M01 records must be a list")

    normalized: List[Dict[str, Any]] = []
    for i, record in enumerate(records, 1):
        required = {"location", "observation", "source_quote_or_evidence", "uncertainty"}
        if not required.issubset(record):
            raise M01LLMError(f"M01 record {i} is missing required fields")
        normalized.append({
            "id": f"EX-{i:03d}",
            "location": record["location"],
            "observation": record["observation"],
            "source_quote_or_evidence": record["source_quote_or_evidence"],
            "uncertainty": record["uncertainty"],
            "source_id": source_package["source_id"],
        })
    return normalized
