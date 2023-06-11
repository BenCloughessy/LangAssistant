from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.vectorstores import Vectara
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
vectara_customer_id=os.getenv("VECTARA_CUSTOMER_ID"), 
vectara_corpus_id=os.getenv("VECTARA_CORPUS_ID"),
vectara_api_key=os.getenv("VECTARA_API_KEY")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

# Load documents
loader = TextLoader("A saga de um ribeirinho.txt", encoding='utf-8')
documents = loader.load()
vectara  = Vectara.from_documents(documents, embedding=None)

# Instantiate a chat model (OpenAI) and a retrieval chain (Vectara)
qa = RetrievalQA.from_llm(llm=ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo"), retriever=vectara.as_retriever())

while True:
    query = input("> ")
    answer = qa.run(query)
    print(answer)