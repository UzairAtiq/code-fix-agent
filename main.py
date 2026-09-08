import os
from agent.loop import fix_loop
import json

#Results list for writing to evaluate.json
results = []

broken_dir = "/Users/uzair/Developer/code-fix-agent/tests/sample_broken"
fixed_dir = "/Users/uzair/Developer/code-fix-agent/tests/fixed"


#looping through all file in sample_broken 
for filename in sorted(os.listdir(broken_dir)):
    #if file is not a python file
    if not filename.endswith(".py"):
        continue

    #if file is a python file
    else :

      #creating the paths for broken files and fixed files
      test_file = os.path.join(broken_dir, filename)
      fixed_file = os.path.join(fixed_dir, filename)

    #printing all the stuff hapeening inside the fixing loop like attempts and proposed fix 
      print(f"\n--- Running: {filename} ---")
      #storing the attempts log list in variable 
      result = fix_loop(test_file, fixed_file)

      #for json dump in evaluate.json get the file name 
      result["filename"] = filename
      results.append(result)

with open("/Users/uzair/Developer/code-fix-agent/data/evaluation.json", "w") as f:
    json.dump(results, f, indent=2)