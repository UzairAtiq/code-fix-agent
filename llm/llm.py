from langchain_groq import ChatGroq
from llm.prompt import prompt
from sandbox.runner import runner
from config import GROQ_API_KEY

def llm(prompt : str) :

  #Setiing up the llm
  llm = ChatGroq(
      model="openai/gpt-oss-120b",
      api_key=GROQ_API_KEY
  )

  #sending prompt to llm to get fix
  answer = llm.invoke(prompt)

  #Returning only the text content
  return answer.content


