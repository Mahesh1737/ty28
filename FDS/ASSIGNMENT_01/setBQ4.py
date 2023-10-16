import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('SOCR-HeightWeight.csv')
print(df.isnull().sum())
print(df.describe())
print(df.info())
