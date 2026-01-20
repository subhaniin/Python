lst1=list(range(1,53))
lsta=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d1a=dict(zip(lst1,lsta ))
print(d1a, "\n")
da1={value:key for key,value in d1a.items()}
print(da1, "\n")
d2={i:i*i for i in lst1}
print("d2:", d2, "\n")
d3={i:i*i*i for i in lst1}
print("d3:", d3, "\n")

import string

def num_to_letters(n):
    result = ""
    while n > 0:
        n -= 1
        result = chr(97 + (n % 26)) + result
        n //= 26
    return result

d1aa = {i: num_to_letters(i) for i in lst1}
print("d1aa:",d1aa, "\n")

daa1={value:key for key,value in d1aa.items()}
print("daa1:",daa1, "\n")