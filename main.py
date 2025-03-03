import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
LB_API_KEY = os.getenv('LB_API_KEY')

def main():
    url = 'https://api.langbase.com/v1/pipes/run'
    apiKey = LB_API_KEY

    content = input("User: ")

    data = {
        'messages': [{'role': 'user', 'content': content}],
		'stream': False
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
    # for line in response.iter_lines():
    #     if line:
    #         line = line.decode('utf-8')
    #         if line.startswith('data:'):
    #             json_data = json.loads(line[len('data:'):].strip())
    #             if "choices" in json_data and json_data["choices"]:
    #                 content = json_data["choices"][0].get("delta", {}).get("content")
    #                 if content:
    #                     print(content)

    response = response.json()
    success = response['success']
    completion_text = response['completion']
    raw_data = response['raw']

    if not success:
        print("Error: ", raw_data)
        return

    print("LangBase:", completion_text)
    print("--------------------------")
    print("Tokens used:", raw_data['usage']['total_tokens'])
    print("--------------------------")
    print("Raw:", raw_data)

if __name__ == "__main__":
    main()

