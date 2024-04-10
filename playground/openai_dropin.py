
import dotenv
dotenv.load_dotenv()
import os
import openai

def main():
    # openai.api_type = "azure"
    openai.api_key = os.environ['OAI_SERVER_API_KEY']
    openai.api_base = "http://127.0.0.1:8081"
    # openai.api_base = "https://www.ericmusa.com"
    # openai.api_version = "2023-05-15"

    chat_with_bob = [
        {'role': 'user', 'content': 'Hello, Bob.'},
        {'role': 'assistant', 'content': 'Hello. How may I help you today?'},
        {'role': 'user', 'content': 'Please tell me the largest city in Europe.'},
        {'role': 'assistant', 'content': 'Sure. The largest city in Europe is Moscow, the capital of Russia.'},
        {'role': 'user', 'content': "that's great, what is Moscow's population?"},
    ]

    # create a chat completion

    # chat_completion = openai.ChatCompletion.create(model="llama-2-70b-chat", messages=[{"role": "user", "content": "Hello world"}], max_tokens=32)
    # chat_completion = openai.ChatCompletion.create(model="llama-2-7b-chat", messages=chat_with_bob, max_tokens=32)
    # chat_completion = openai.ChatCompletion.create(model="llama-2-13b-chat", messages=chat_with_bob, max_tokens=32)
    # chat_completion = openai.ChatCompletion.create(model="llama-2-70b-chat", messages=chat_with_bob, max_tokens=32, model_params={'seed':124})
    # print(chat_with_bob)
    # chat_completion = openai.ChatCompletion.create(model="llama-2-70b-chat", messages=chat_with_bob, max_tokens=32, seed=124)
    # chat_completion = openai.ChatCompletion.create(model="llama-2-70b", messages=chat_with_bob, max_tokens=128, model_kwargs={'seed':123})
    chat_completion = openai.ChatCompletion.create(model="llama-2-70b", messages=chat_with_bob, max_tokens=128, seed=123)
    # chat_completion = openai.Completion.create(model="llama-2-70b", prompt='the name of the largest city in Europe ', max_tokens=32)

    # print the completion
    print(chat_completion.choices[0].message.content)
    # print(chat_completion.system_fingerprint)
    # print(chat_completion.id)
    # print(chat_completion.usage)
    # print(chat_completion.choices[0].text)

if __name__ == '__main__':
    main()