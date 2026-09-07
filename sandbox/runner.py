import subprocess

#test file path
test_file = "/Users/uzair/Developer/code-fix-agent/tests/sample_broken/test1.py"

result = subprocess.run(  ["python" ,test_file] , capture_output=True , text= True)

print(result.stdout)
print(result.stderr)

