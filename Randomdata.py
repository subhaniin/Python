import pandas as pd
import numpy as np
import random
from faker import Faker

fake = Faker()

# Generate 1000+ rows of unclean data
num_rows = 1200

# Create random unique IDs (with some duplicates)
ids = [random.randint(1000, 9999) for _ in range(num_rows)]
ids[:20] = ids[5:25]  # Introduce duplicates

# Generate names (with typos and extra spaces)
names = [fake.name() for _ in range(num_rows)]
for i in range(0, num_rows, 20):
    names[i] = names[i].lower()  # Random lowercase names
    names[i+1] = " " + names[i+1] + "  "  # Extra spaces
    names[i+2] = names[i+2].replace('a', '@').replace('o', '0')  # Typos

# Generate ages (with outliers)
ages = [random.randint(20, 60) for _ in range(num_rows)]
ages[50] = 150  # Extreme outlier
ages[200] = 5   # Extreme outlier

# Generate salaries (with missing values)
salaries = [random.randint(30000, 150000) for _ in range(num_rows)]
for i in range(0, num_rows, 15):
    salaries[i] = None  # Introduce missing values

# Generate joining dates (different formats)
dates = [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_rows)]
for i in range(0, num_rows, 30):
    dates[i] = dates[i].strftime("%d-%m-%Y")  # Different format
    dates[i+1] = dates[i+1].strftime("%m/%d/%Y")  # Different format

# Generate department names (with inconsistencies)
departments = ["HR", "Finance", "Engineering", "Sales", "Marketing", "IT"]
department_column = [random.choice(departments) for _ in range(num_rows)]
for i in range(0, num_rows, 25):
    department_column[i] = department_column[i].lower()  # Random lowercase
    department_column[i+1] = department_column[i+1] + " "  # Extra space
    department_column[i+2] = department_column[i+2].replace("e", "3")  # Typos

# Create DataFrame
data = pd.DataFrame({
    "ID": ids,
    "Name": names,
    "Age": ages,
    "Salary": salaries,
    "Joining Date": dates,
    "Department": department_column
})

# Save as Excel file
file_path = "/mnt/data/unclean_data.xlsx"
data.to_excel(r"C:\Users\subha\OneDrive\Desktop\Programming\other_unclean_data.xlsx")

# Return the file path
file_path