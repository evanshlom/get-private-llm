# https://www.markhneedham.com/blog/2023/06/23/hugging-face-run-llm-model-locally-laptop/
from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

from get_llm import local_llm

template = """
You are a friendly chatbot assistant that responds conversationally to users' questions.
Keep the answers short, unless specifically asked by the user to elaborate on something.

Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=local_llm)