lst1 = [1,1,2,2,3,3,4,5,6,7,8,9]
remove_duplicates = set(lst1)
lst2=(list(remove_duplicates))

print(type(lst2))
print(lst2)
print(lst1)
print(lst1 == lst2)  # This will print True if duplicates were removed      
print(lst1 is lst2)  # This will print False because they are different objects
print(lst1 is lst1)  # This will print True because they are the same object    
print(lst2 is lst2)  # This will print True because they are the same object 