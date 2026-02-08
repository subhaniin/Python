from faker import Faker
import random
fake = Faker("ar_EG")
fake = Faker("en_IN")

first_names = [
    "Mohammad", "Ahmed", "Ali", "Hassan", "Hussain", "Abdul", "Umar",
    "Ibrahim", "Yusuf", "Bilal", "Saif", "Zaid", "Ayaan", "Arman"
]

last_names = [
    "Khan", "Shaikh", "Syed", "Ansari", "Qureshi", "Pathan",
    "Farooqi", "Rizvi", "Siddiqui", "Hashmi", "Subhani"
]

for _ in range(10):
    first = random.choice(first_names)
    last = random.choice(last_names)
    print(f"{first} {last}","\n")

for i in range(10):
    print(fake.name(),"",fake.email(),"\n")
