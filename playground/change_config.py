import dotenv
dotenv.load_dotenv()

import os
import json
import requests


    # 'chat_prompt': '',
    # 'user_name': "\\nuser: ",
    # 'ai_name': "\\nassistant: ",
    # 'system_name': "\\nSYSTEM: ",
    # 'stop': "</s>",
    # 'host': '127.0.0.1',
    # 'port': 8081,
    # 'output_dir': output_dir,
    # 'llama_api_addr': 'http://127.0.0.1:8080',
    # 'model_name': None,
    # # 'api_key': None,
    # 'llama_logfile': None,
    # 'model_proc_id': None,
    # 'tunnel_proc_id': None,


openai_api_key = os.environ['OAI_SERVER_API_KEY']
openai_api_base = 'http://127.0.0.1:8081'

auth_headers = {
    'Authorization': f'Bearer {openai_api_key}',
    'Content-Type': 'application/json',
}

def _url(endpoint):
    return f'{openai_api_base}/{endpoint}' 


def _make_req(endpoint, data, headers, method='POST'):
    return requests.request(method=method, url=_url(endpoint), headers=headers, data=json.dumps(data))


def update_config(new_config):
    return _make_req('config', new_config, auth_headers)


def change_model(new_model_name):
    return _make_req('model', new_model_name, auth_headers)


def get_model(to_json=True):
    res = _make_req('model', None, auth_headers, 'GET')
    return res.json() if to_json else res


if __name__ == '__main__':
    # test_data = {
    #     'a': 0,
    #     'b': 1,
    #     'c': 2,
    #     'd': 3,
    #     'e': 4,
    #     'f': 5,
    #     'g': 6,
    #     'h': 7,
    #     'j': 8,
    #     'i': 9,
    # }

    new_config = {
        'chat_prompt': 'Chat: '
    }

    # response = _make_req('config', new_config, auth_headers)
    # print(response, response.text)

    new_model = {
        'model_name': 'llama-2-70b'
    }

    # response = _make_req('model', new_model, auth_headers, method='GET')
    # print(response, response.text)
    
    response = _make_req('model', new_model, auth_headers)
    print(response, response.text)
    # print(response.status_code)
    # print(response.json())
    