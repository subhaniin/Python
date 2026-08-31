import dis
dis.dis("print('Hello, World!')")

import types

# Compile the string into a code object
code_obj = compile("print('Hello, World!')", "rough_dis.py", "exec")

# Print the raw array of bytes
print(list(code_obj.co_code))
