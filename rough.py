lst1=[0,1,2,3,4,5,6,7,8,9]
lst2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y', 'z']
b = ''.join(lst2)
c=b.upper()
lst3=list(c)
print(lst3)
print(c)

lst1 = list(range(26))
mapping = dict(zip(lst1, lst3))
print(mapping)
