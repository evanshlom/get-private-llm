from chain import llm_chain
def ask_question(question):
    result = llm_chain(question)
    print(result['question'])
    print("")
    print(result['text'])

# with Timer():
#     ask_question("Describe some famous landmarks in London")

ask_question("Describe some famous landmarks in London")