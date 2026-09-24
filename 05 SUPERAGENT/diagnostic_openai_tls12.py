import os
import json
import ssl
import urllib.request
import urllib.error

ctx = ssl.create_default_context()
ctx.minimum_version = ssl.TLSVersion.TLSv1_2
ctx.maximum_version = ssl.TLSVersion.TLSv1_2

url = os.environ["LLM_BASE_URL"].rstrip("/") + "/chat/completions"

payload = {
    "model": os.environ["LLM_MODEL"],
    "messages": [
        {"role": "user", "content": "Reply with exactly: OK"}
    ],
    "max_tokens": 10,
}

request = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": "Bearer " + os.environ["LLM_API_KEY"],
        "Content-Type": "application/json",
    },
    method="POST",
)

try:
    response = urllib.request.urlopen(
        request,
        context=ctx,
        timeout=60,
    )
    print("STATUS:", response.status)
    print(response.read().decode("utf-8"))

except urllib.error.HTTPError as e:
    print("HTTP STATUS:", e.code)
    print("RESPONSE BODY:")
    print(e.read().decode("utf-8"))

except Exception as e:
    print("ERROR TYPE:", type(e).__name__)
    print("ERROR:", e)
