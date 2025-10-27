import os
from langchain import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


# Optional: agent style orchestration imports
# from langchain.agents import Tool, initialize_agent
# from langchain.utilities import GoogleSearchAPIWrapper


OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
raise Exception("OPENAI_API_KEY not set in env")


# Simple LLM wrapper for MVP. Swap for full agent (tools, memory) later.


def run_agent(prompt_text: str, user_id: str = "anonymous") -> str:
prompt = PromptTemplate(input_variables=["input"], template="You are a helpful business assistant. {input}")
llm = OpenAI(temperature=0)
chain = LLMChain(llm=llm, prompt=prompt)
resp = chain.run({"input": prompt_text})
return resp
