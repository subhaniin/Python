class car:
    def __init__(self, Brand:str, Model:str, Year:int):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year

    def info(self):
         print(f"{self.Brand} {self.Model} {self.Year}")
    def start(self):
        print(f"{self.Brand} {self.Model} is starting")
    
car1 = car('TATA', 'safari', 'abcd')

car1.info()
car1.start()

# Example of a class with type checking in Python
# This will raise an error if the type does not match


class Dog:
    def __init__(self, age: int):
        if not isinstance(age, int):
            raise TypeError("age must be an int")
        self.age = age

# Example of using Pydantic for data validation
# This will raise an error if the type does not match

from pydantic import BaseModel

class Dog(BaseModel):
    name: str
    age: int

dog = Dog(name="Bruno", age="5")  # ❌ raises error, must be int

# Example of using mypy for static type checking
# This will check the types at compile time ❌ (static only)
# To run mypy, you would typically run the following command in your terminal:
# Make sure you have mypy installed: pip install mypy
#mypy your_file.py
