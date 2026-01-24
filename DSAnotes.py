# Different Python data types (one per line)

a = 10
print(a, type(a))              # int
a=input()
b=input()
print(int(a+b))

b = 3.14
print(b, type(b))              # float

c = "Hello"
print(c, type(c))              # str

d = True
print(d, type(d))              # bool

e = [1, 2, 3]
print(e, type(e))              # list

f = (1, 2, 3)
print(f, type(f))              # tuple

g = {1, 2, 3}
print(g, type(g))              # set

h = {"a": 1, "b": 2}
print(h, type(h))              # dict

from array import array
i = array("i", [1, 2, 3])
print(i, type(i))              # array.array

import numpy as np
j = np.array([1, 2, 3])
print(j, type(j))              # numpy.ndarray
#------ Various Data Structures -----

list1=[1,2,3,4,5]
tuple1=(1,2,3,4,5)
set1={1,2,3,4,5}
dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
from array import array
array1=array("i",[1,2,3,4,5])
array2=array("f",[1.1,2.2,3.3,4.4,5.5])
array3=array("u",['a','b','c','d','e'])
array4=array("b",[1,0,1,0,1])
array5=array("B",[255,0,127,64,32])
array6=array("h",[1000,2000,3000,4000,5000])
array7=array("H",[10000,20000,30000,40000,50000])   
array8=array("l",[100000,200000,300000,400000,500000])
array9=array("L",[1000000,2000000,3000000,4000000,5000000])
array10=array("q",[10000000000,20000000000,30000000000,40000000000,50000000000])
array11=array("Q",[100000000000,200000000000,300000000000,400000000000,500000000000])
array12=array("d",[1.111111,2.222222,3.333333,4.444444,5.555555])
import numpy as np
np.array1=np.array([1,2,3,4,5])

# ===== BASIC TYPES =====
a = 10
print(a, type(a))                     # int

b = 3.14
print(b, type(b))                     # float

c = 2 + 3j
print(c, type(c))                     # complex

d = "Hello"
print(d, type(d))                     # str

e = True
print(e, type(e))                     # bool

f = None
print(f, type(f))                     # NoneType


# ===== COLLECTION TYPES =====
g = [1, 2, 3]
print(g, type(g))                     # list

h = (1, 2, 3)
print(h, type(h))                     # tuple

i = {1, 2, 3}
print(i, type(i))                     # set

j = frozenset([1, 2, 3])
print(j, type(j))                     # frozenset

k = {"a": 1, "b": 2}
print(k, type(k))                     # dict


# ===== RANGE =====
l = range(5)
print(l, type(l))                     # range


# ===== BYTES TYPES =====
m = b"hello"
print(m, type(m))                     # bytes

n = bytearray(b"hello")
print(n, type(n))                     # bytearray

o = memoryview(b"hello")
print(o, type(o))                     # memoryview


# ===== FUNCTION TYPE =====
def func():
    pass

print(func, type(func))               # function


# ===== GENERATOR TYPE =====
gen = (x for x in range(3))
print(gen, type(gen))                 # generator


# ===== ARRAY (typed container) =====
from array import array
arr = array("i", [1, 2, 3])
print(arr, type(arr))                 # array.array


# ===== NUMPY ARRAY =====
import numpy as np
np_arr = np.array([1, 2, 3])
print(np_arr, type(np_arr))           # numpy.ndarray


# ===== TORCH TENSOR =====
try:
    import torch
    tensor = torch.tensor([1, 2, 3])
    print(tensor, type(tensor))       # torch.Tensor
except ImportError:
    print("Torch not installed")


# ===== CUSTOM CLASS TYPE =====
class Person:
    pass

p = Person()
print(p, type(p))                     # custom class


# ===== SET COMPREHENSION =====
s_comp = {x for x in range(3)}
print(s_comp, type(s_comp))           # set


# ===== LAMBDA FUNCTION =====
lam = lambda x: x * 2
print(lam, type(lam))                 # function
# ===== COMPLEX DATA STRUCTURE =====
complex_structure = {
    "numbers": [1, 2, 3, (4, 5)],
    "info": {
        "name": "Alice",
        "age": 30,
        "is_student": False
    },  
    "matrix": np.array([[1, 2], [3, 4]])
}   
print(complex_structure, type(complex_structure))  # dict

# ===== FUNCTION WITH VARIOUS TYPES =====
def process_data(data: dict) -> list:
    result = []
    for key, value in data.items():
        if isinstance(value, (list, tuple, set)):
            result.append(len(value))
        elif isinstance(value, dict):
            result.append(len(value.keys()))
        else:
            result.append(1)
    return result
data_input = {
    "list_data": [1, 2, 3],
    "tuple_data": (4, 5),
    "set_data": {6, 7, 8, 9},
    "dict_data": {"a": 1, "b": 2}
}
output = process_data(data_input)
print(output, type(output))  # list
# ===== ASYNC FUNCTION =====
import asyncio
async def fetch_data() -> str:
    await asyncio.sleep(1)
    return "Data fetched"
async def main():
    data = await fetch_data()
    print(data, type(data))  # str
asyncio.run(main())
# ===== DECORATOR FUNCTION =====
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper  
@decorator
def greet(name: str) -> str:
    return f"Hello, {name}!"    
greeting = greet("Bob")
print(greeting, type(greeting))  # str
# ===== CONTEXT MANAGER =====
from contextlib import contextmanager   
@contextmanager
def open_file(file_name: str, mode: str):
    file = open(file_name, mode)
    try:
        yield file
    finally:
        file.close()
with open_file("sample.txt", "w") as f:
    f.write("Hello, World!")
print("File written successfully")
# ===== ENUMERATION TYPE =====
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
print(Color.RED, type(Color.RED))  # Color
# ===== DATETIME TYPE =====
from datetime import datetime
now = datetime.now()
print(now, type(now))               # datetime.datetime
# ===== DECIMAL TYPE =====
from decimal import Decimal
dec = Decimal("10.5")   
print(dec, type(dec))               # decimal.Decimal
# ===== FRACTION TYPE =====
from fractions import Fraction
frac = Fraction(1, 3)
print(frac, type(frac))             # fractions.Fraction
# ===== CHAINMAP TYPE =====
from collections import ChainMap
dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}
chain_map = ChainMap(dict_a, dict_b)
print(chain_map, type(chain_map))   # collections.ChainMap
# ===== NAMEDTUPLE TYPE =====
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y']) 
p = Point(10, 20)
print(p, type(p))                   # collections.namedtuple