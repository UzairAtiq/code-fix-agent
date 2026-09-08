from agent.fixer import get_fix
from sandbox.runner import runner
from agent.stopping import stopper

def fix_loop (test_file : str) :

  #count variable for counting how mant times the loop has run
  count = 0

  #Fixer loop
  while True :

    #Incrementing count
    count += 1

    #Running the file through the runner(executor)
    result = runner(test_file)

    #If no error
    if result.returncode == 0 or stopper(count):
      break
    else : 
        #Sending the file path to the fixer
       fix_llm = get_fix(test_file)

       #Writing the fix to the file path
       with open(test_file, "w") as f:
        f.write(fix_llm)





  