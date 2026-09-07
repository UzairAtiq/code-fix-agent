import subprocess

def runner(test_file : str) :

  #creating the subprocess 
  result = subprocess.run(  ["python" ,test_file] , capture_output=True , text= True)


  #printing the output or error of the subprocess
  print(result.stdout)
  print(result.stderr)

