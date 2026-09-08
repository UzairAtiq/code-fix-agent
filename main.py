from agent.loop import fix_loop

test_file = '/Users/uzair/Developer/code-fix-agent/tests/sample_broken/test1.py'
fixed_file = "/Users/uzair/Developer/code-fix-agent/tests/fixed/test1.py"

fix_loop(test_file , fixed_file)