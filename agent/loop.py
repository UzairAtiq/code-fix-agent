from agent.fixer import get_fix
from sandbox.runner import runner
from agent.stopping import stopper



def fix_loop (test_file : str , fixed_file) :

  #count variable for counting how mant times the loop has run
  count = 0

  #copying the broken files code into a variable for the fixer

  #Reading the code from the test file 
  with open(test_file, "r") as f:
      code = f.read()

  #Splitting the fucntion and assert statements  
  lines = code.splitlines()

  function_lines = [line for line in lines if not line.strip().startswith("assert")]
  assert_lines = [line for line in lines if line.strip().startswith("assert")]

  function = "\n".join(function_lines)
  assert_statements = "\n".join(assert_lines)

  #Writing the code to the fixed file 
  with open(fixed_file, "w") as f:
          f.write(function + "\n" + assert_statements)

  #Fixer loop
  while True :

    #Incrementing count
    count += 1

    #Printing the number of times the loop ran 
    print("Attempt # : ",count)

    #Running the file through the runner(executor)
    result = runner(fixed_file)

    #If no error
    if result.returncode == 0 :
      print("FILE RAN SUCESSFULLY")

      #Printing the output 
      print("File Output : ",result.stdout)
      break

    elif stopper(count) :
      print("FAILED TO FIX AFTER MAX ATTEMPTS")
      print("Last Error:", result.stderr)
      break   
    
    else : 

      #Getting the error
      error = result.stderr
       
      #Sending the file path to the fixer
      fix_llm = get_fix(function , error)

      #Printing llm proposed fix
      print("Proposed Fix : " , fix_llm)

       #Writing the fix to the file path
      with open(fixed_file, "w") as f:
        f.write(fix_llm + "\n" + assert_statements)

   





  