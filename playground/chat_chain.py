import dotenv
dotenv.load_dotenv()
import os
import re

from profiles import ChatProfile
from change_config import update_config, change_model

from langchain.chat_models.openai import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)


class Chat:

    def __init__(self, 
            messages, 
            profile, 
        ) -> None:
        self.messages = messages
        self.profile = profile
    
    def __call__(self, user_input=None, max_tokens=32, seed=None, verbose=False, return_all_messages=False):
        assert user_input or isinstance(self.messages[-1], HumanMessage), 'user_input evaluated to False and the last message in the thread was not by a Human'
        
        user_input = HumanMessage(content=user_input) if isinstance(user_input, str) else user_input
        self.messages.append(user_input)
        if verbose:
            for message in messages:
                print(message.type.upper(), '-', message.content)
        
        chat_chain = ChatOpenAI(
            openai_api_key=os.environ['OAI_SERVER_API_KEY'], 
            openai_api_base='http://127.0.0.1:8081', 
            **self.profile(max_tokens, seed)
        )

        ai_response = chat_chain(self.messages)

        if verbose:
            print(f'{ai_response.type.upper()}: {ai_response.content}')

        self.messages.append(ai_response)
        return self.messages if return_all_messages else ai_response
    
    def conversation(self):
        for message in messages:
            print(f'{message.type.upper()}: {message.content}')
        if self.messages and isinstance(self.messages[-1], HumanMessage):
            self()
        while True:  
            user_input = HumanMessage(content=input())
            self.messages.append(user_input)              
            ai_response = self(user_input)
            # print(ai_response)
            print(f'{ai_response.type.upper()}: {ai_response.content}')
            self.messages.append(ai_response)



if __name__ == '__main__':
    
    messages = [
          # SystemMessage(content="You are a helpful assistant that translates anything the user says from English to French."),
        #   HumanMessage(content="Can you translate whatever I say next that is contained in quotes (' ') into French, please? Anything not within quotes, respond normally."),
        #   AIMessage(content="Sure thing! Whatever you say next, I will provide French translations for things within quotes and respond normally to everything else."),
    ]
    
    chat_profile = ChatProfile()
    # chat_profile.seed = 124
    # update_config({
    # 'user_name': "Human:",
    # 'ai_name': "AI:",
    # })
    chat = Chat(messages, chat_profile,)

    # chat.conversation()
    chat('Hello!', max_tokens=128, seed=125)
# data = requests.request("POST", urllib.parse.urljoin("http://127.0.0.1:8080", "/completion"), data=json.dumps(postData))
