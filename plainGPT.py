from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
)
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

while True:
    query = input("> ")
    response = llm([HumanMessage(content=query)])
    answer = response.content
    print(answer)