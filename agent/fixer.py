from llm.llm import llm
from llm.prompt import prompt



def get_fix(broken_code : str , error)  :




  prompt_llm = prompt(error , broken_code)

  #Storing response from llm in a variable 
  llm_response =  llm(prompt_llm)

  #returning the response 
  return llm_response










