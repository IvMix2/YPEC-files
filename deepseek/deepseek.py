import requests
import json

url = "https://api.intelligence.io.solutions/api/v1/chat/completions"
API_KEY = ""

def deepseek_query(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": "deepseek-ai/DeepSeek-R1",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": True
    }
    with requests.post(
            url=url,
            headers=headers,
            json=data,
            stream=True
    ) as response:
        if response.status_code != 200:
            print("Ошибка API:", response.status_code)
            return ""

        full_response = []

        for chunk in response.iter_lines():
            if chunk:
                chunk_str = chunk.decode('utf-8').replace('data: ', '')
                try:
                    chunk_json = json.loads(chunk_str)
                    if "choices" in chunk_json:
                        content = chunk_json["choices"][0]["delta"].get("content", "")
                        if content:
                            print(content, end='', flush=True)
                            full_response.append(content)
                except:
                    pass
        return ''.join(full_response).split('</think>\n\n')[1]

def main():
    print("Для выхода введите 'exit'\n")

    while True:
        user_input = input("Вы: ")

        if user_input.lower() == 'exit':
            print("Завершение работы...")
            break

        print("DeepSeek-R1:", end=' ', flush=True)
        res = deepseek_query(user_input)
        print(res)

if __name__ == "__main__":
    main()