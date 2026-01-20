def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

a,b=1,2
r=add(a,b),subtract(a,b),multiply(a,b),divide(a,b)

print(f"add:{r[0]}")
print(f"substract:{r[1]}")
print(f"multiply:{r[2]}")
print(f"divsion:{r[3]}")
print()
print(f"add:{r[0]}","\n",f"Substract{[1]}","\n",r[2],"\n",r[3])  # This will print the results of the operations
print()
print(f"Add: {r[0]}, Subtract: {r[1]}, Multiply: {r[2]}, Divide: {r[3]}")

import datetime as dt
print(dt.datetime.now().strftime("%Y-%m-%d  %H:%M:%S%p"))  # Print current date and time in a specific formats