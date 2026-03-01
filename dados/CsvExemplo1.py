import pandas as pd
import os

df = pd.read_csv('steam.csv')

print(df.head())
print(df.tail())
print(df.columns)