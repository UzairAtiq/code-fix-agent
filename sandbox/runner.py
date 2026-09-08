import subprocess

def runner(test_file : str) :

  #creating the subprocess 
  result = subprocess.run(  ["python" ,test_file] , capture_output=True , text= True)

  #returning the subprocess result 
  return result


