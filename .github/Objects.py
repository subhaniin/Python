class car:
    def __init__(self, Brand, Model, Year):
        self.Brand = Brand
        self.Model = Model
        self.Year = Year

    def info(self):
         print(f"{self.Brand} {self.Model} {self.Year}")
    def start(self):
        print(f"{self.Brand} {self.Model} is starting")
    
car1 = car()

car1.info()
car1.start()