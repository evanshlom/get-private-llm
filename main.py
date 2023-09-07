from credentials.hf_api import HF_API_KEY
from langchain import 
from transformers import 

# DOwnload hf model from api to loca lifle
model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ROMANCE")
