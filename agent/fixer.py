from llm.llm import llm
from llm.prompt import prompt
from sandbox.runner import runner



def extract_fix(test_file : str) :

  #Sending the path of file to runner
  result = runner(test_file)

  #Extracting the std err attribute from the CompltetedProcess Object
  error = result.stderr

  #Reading the code from the test file 
  with open(test_file, "r") as f:
    code = f.read()

  prompt = prompt(error , code)

  #Storing response from llm in a variable 
  llm_response =  llm(prompt)

  #returning the response 
  return llm_response










