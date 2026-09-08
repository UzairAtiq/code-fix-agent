from llm.llm import llm
from llm.prompt import prompt



def get_fix(test_file : str , error)  :


  #Reading the code from the test file 
  with open(test_file, "r") as f:
    code = f.read()

  prompt_llm = prompt(error , code)

  #Storing response from llm in a variable 
  llm_response =  llm(prompt_llm)

  #returning the response 
  return llm_response










