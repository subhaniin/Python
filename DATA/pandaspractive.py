import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/datasets/global-temp/master/data/monthly.csv")
df.head()
df.info()
df.describe()
df.columns  
df.shape
df.isnull().sum()
df.dropna(inplace=True)
df.isnull().sum()
df['Year'].unique()
df['Year'].nunique()
df['Year'].value_counts()