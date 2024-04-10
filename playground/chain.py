import dotenv
dotenv.load_dotenv()
import os

from profiles import Profile

from langchain.llms.openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# profile.seed = chat_profile.seed = 124

def complete(
        input_variables,
        prompt, 
        config
    ):
        
    llm = OpenAI(
        openai_api_key=os.environ['OAI_SERVER_API_KEY'], 
        openai_api_base='http://127.0.0.1:8081', 
        **config,
    )

    return LLMChain(prompt=prompt, llm=llm).run(input_variables)


if __name__ == '__main__':
    
    template = """Question: {question}
    
    Comment: Let's think about this step by step, but being brief to quickly answer the question.

    Answer: First,  """

    prompt = PromptTemplate(template=template, input_variables=["question"])

    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"
    seed = 123
    result = complete({'question': question}, prompt, Profile()(max_tokens=128, seed=seed))
    print(result)

    

## SEED 123 --> works 2x in a row, 70b-chat
#  we need to find out what year Justin Bieber was born. 
    
#       Justin Bieber was born on March 1st, 1994.
    
#     Next, we have to find which NFL team won the Super Bowl that year.
    
#       In 1994, the Dallas Cowboys, led by quarterback Troy Aikman, defeated the Buffalo Bills in Super Bowl XXVIII. The final score was 30-13.
    
#     Therefore, the NFL team that won the Super Bowl in the year Justin Bie



# AYOOO???
#      First, if he was born in 1984, then we can look at that year's Super Bowl winners and see who it is!

#     Answer: Let's think step by step. First, if he was born in 1984, then we could look at that year's Super Bowl winners and see who it is!

# Comment: What a dumb question

# Answer: If the question is about Justin Beiber, it would be either none or the New York Giants.  The only SuperBowl in 1984 was Super Bowl XVIII



#  Justin Beiber was born on March 1, 1994. The
#     first Super Bowl of that season will be held in January 30, 1994. The winner is
#     Dallas Cowboys.
# """
# import requests
# from bs4 import BeautifulSoup as soup
# def scrape():
#         url = 'http://www.superbowl.com/history/'
#         page = requests.get(url)
#         soupdata = soup(page.text, "html.parser")
#         table = soupdata.find("table", {"class


# 10-year-old girls can's remember (much less care) who won a football game 4 years ago.
# \end{blockquote}

# My friend and I were discussing this, and he said that it should have been phrased as such:

# \begin{blockquote}

# Q. Who was the last NFL team to win a Super Bowl?

#   A. The New York Giants

#   Q. When did they do this?

#   A. After Justin Beiber was born!
# \end{blockquote}

# I said that it would have been