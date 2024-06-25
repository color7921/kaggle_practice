#!pip install langchain
#!pip install openai
#!pip install google-search-results
import os
os.environ["OPENAI_API_KEY"] = ""
os.environ["SERPAPI_API_KEY"] = ""

from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain import LLMMathChain, SerpAPIWrapper
from langchain.agents import Tool

search = SerpAPIWrapper()
params = {
    "engine": "bing",
    "gl": "us",
    "hl": "en"
}
search = SerpAPIWrapper(params=params)

llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo') 

tools = [
    Tool(
        name = "Search",
        func=search.run,
        description="검색하는 API"
    )
]

agent = initialize_agent(tools, llm, verbose=True)
result = agent.invoke("한국의 수도는 어디?")
print(result['output'])