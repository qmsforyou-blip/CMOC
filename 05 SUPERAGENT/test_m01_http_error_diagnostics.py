"""M01 reports actionable HTTP metadata without echoing request or error body."""
import io
import os
from unittest.mock import patch
from urllib.error import HTTPError

from m01_llm import M01LLMError, _request_json


def main():
    payload = b'{"error":{"code":"credit_balance_exhausted","type":"insufficient_quota","message":"sensitive response"}}'
    error = HTTPError(
        "https://api.openai.com/v1/chat/completions", 429, "Too Many Requests",
        {"Retry-After": "60"}, io.BytesIO(payload),
    )
    with patch.dict(os.environ, {"LLM_API_KEY": "private-key", "LLM_MODEL": "gpt-5.6-sol"}):
        with patch("m01_llm.urllib.request.urlopen", side_effect=error):
            try:
                _request_json({"model": "gpt-5.6-sol", "messages": []})
            except M01LLMError as exc:
                detail = str(exc)
            else:
                raise AssertionError("Expected M01LLMError")
    assert "HTTP 429" in detail
    assert "code=credit_balance_exhausted" in detail
    assert "type=insufficient_quota" in detail
    assert "retry_after=60" in detail
    assert "private-key" not in detail
    assert "sensitive response" not in detail
    print("M01 HTTP ERROR DIAGNOSTICS: PASS")


if __name__ == "__main__":
    main()
