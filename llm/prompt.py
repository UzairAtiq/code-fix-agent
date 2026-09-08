from langchain_core.prompts import PromptTemplate


def prompt(error , test_file) :

  #Creating the prompt template and passing the error in the prompt 
  build_template = PromptTemplate.from_template(
  "You are a code fixer \n" 
  "The error i am getting in my code is {Error}\n"
  "The code is {Test_file} \n"
  "Fix this error and return ONLY the corrected Python code.\n"
  "Do not include explanations, comments about the fix, or markdown code fences.\n"
  "Return just the raw, working code.\n"
  )

  #formatting the template
  template = build_template.format(
    Error = error ,
    Test_file = test_file
  )

  return template