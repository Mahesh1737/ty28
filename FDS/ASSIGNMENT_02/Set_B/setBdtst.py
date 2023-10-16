import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as s
df = pd.read_csv('Iris.csv')
print(df)

#1
#print(df.sample(20))
print("Max value of SepalLengthCm : ",max(df['SepalLengthCm']))
print("Min value of  SepalLengthCm : ",min(df['SepalLengthCm']))
print("\n")
print("Max value of PetalWidthCm : ",max(df['PetalWidthCm']))
print("Min value of  PetalWidthCm : ",min(df['PetalWidthCm']))

#2
print("Number of Records for each distinct value of class attribute : ",df['Species'].value_counts())

#3

print("Mean of the SepalLengthCm :",df['SepalLengthCm'].mean())

print("Mean of the PetalWidthCm :",df['PetalWidthCm'].mean())

print("Median of the SepalLengthCm :",df['SepalLengthCm'].median())

print("Median of the PetalWidthCm :",df['PetalWidthCm'].median())
