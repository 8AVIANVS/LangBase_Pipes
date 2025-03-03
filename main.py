import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
LB_API_KEY = os.getenv('LB_API_KEY')

def main():
    url = 'https://api.langbase.com/v1/pipes/run'
    apiKey = LB_API_KEY

    data = {
        'messages': [{'role': 'user', 'content': 'Hello!'}],
		'stream': True
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {apiKey}"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if not response.ok:
        print(response.json())
        return

    # Read SSE stream response (OpenAI Format) and log the response
    # Here, we manually process the response stream
    for line in response.iter_lines():
        if line:
            line = line.decode('utf-8')
            if line.startswith('data:'):
                json_data = json.loads(line[len('data:'):].strip())
                if "choices" in json_data and json_data["choices"]:
                    content = json_data["choices"][0].get("delta", {}).get("content")
                    if content:
                        print(content)

if __name__ == "__main__":
    main()

