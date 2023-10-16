import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as s
df = pd.read_csv('data.csv')
#print(df)

#1
'''print("\n")
print("Statistical Data : \n", df.describe())
print("\n")
print("Shape : ",df.shape)
print("\n")
print("Top 3 Head : \n",df.head(3))
print("\n")

#2
print(df.isnull())
print("\nDrop rows value having  0 \n",df.dropna())
#print("\nEvery missing value replace with 0 \n",(df.fillna("NaN", inplace=True)))
mean = df['Age'].mean()
df['Age'].fillna(mean, inplace=True)
print("\n\n",df)

mean = df['Salary'].mean()
df['Salary'].fillna(mean, inplace=True)
print("\n\n",df)'''

#3
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
#print("\nOne Hot :\n")
enc = OneHotEncoder(handle_unknown='ignore')
enc_df = pd.DataFrame(enc.fit_transform(df[['Purchased']]).toarray())
print("  One Hot :  \n ",enc_df)

labelencoder = LabelEncoder()
df['Country'] = labelencoder.fit_transform(df['Country'])
print("\n\n",df)
labelencoder = LabelEncoder()
df['Purchased'] = labelencoder.fit_transform(df['Purchased'])
print("\n\n",df)

print("\n\nLevel Encoder :\n",df)

print("\nJoined Country & Salary  :\n")
df = df.join(enc_df)
print(df)
