from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the Questions below
Here is the conversation history : {context}
Question : {question}
Answer : 
"""
model = OllamaLLM(model="llama3") 
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model 

def conversations():
    context = ""
    print("Welcome, to the Morphed Library! \n Type 'exit' to Quit")
    while True:
        user_input = input("You:  ")
        if user_input.lower == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Morphed Librarian:  " , result)
        context = f"\n User: {user_input}\n Librarian: {result}"

if __name__ == "__main__":
    conversations()
