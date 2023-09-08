from get_llm import local_llm

print(local_llm('What is the capital of France? '))

llm_chain = LLMChain(prompt=prompt,
                     llm=local_llm
                     )

question = "What is the capital of England?"

print(llm_chain.run(question))