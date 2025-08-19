import json
import pandas as pd
from pandas import json_normalize

# Read JSON file
with open("JEMPS2634H.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Flatten the JSON
df = json_normalize(data)

# Display as table
print(df.head())

# Save to CSV for Excel view
df.to_csv("itr3_table.csv", index=False)
