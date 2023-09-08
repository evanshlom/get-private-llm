# # https://github.com/samwit/langchain-tutorials/blob/main/YT_LangChain_Running_HuggingFace_Models_Locally.ipynb
# from credentials.hf_api import HF_API_KEY
# from langchain import 
# from transformers import 

# !pip -q install langchain huggingface_hub transformers sentence_transformers

# import os
# os.environ['HUGGINGFACEHUB_API_TOKEN'] = ''

# from langchain import PromptTemplate, HuggingFaceHub, LLMChain

# DOwnload hf model from api to loca lifle
# https://github.com/samwit/langchain-tutorials/blob/main/YT_LangChain_Running_HuggingFace_Models_Locally.ipynb
# YT_LangChain_Running_HuggingFace_Models_Locally.ipynb
# T5-Flan - Encoder-Decoder
from langchain.llms import HuggingFacePipeline
# import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSeq2SeqLM

model_id = 'google/flan-t5-large'# go for a smaller model if you dont have the VRAM
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id, load_in_8bit=True)

pipe = pipeline(
    "text2text-generation",
    model=model, 
    tokenizer=tokenizer, 
    max_length=100
)

local_llm = HuggingFacePipeline(pipeline=pipe)