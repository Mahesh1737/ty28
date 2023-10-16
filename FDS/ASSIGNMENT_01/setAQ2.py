import pandas as pd
#data = [['mahesh',18,99],['abhi',18,90],['gaurav',18,85],['jay',18,75]]
df = pd.DataFrame(columns = ['name','age','precentage'])
df.loc[0] = ['mahesh', 18, 99]
df.loc[1] = ['jay', 18, 36]
df.loc[2] = ['abhi', 18, 90]
df.loc[3] = ['gaurav', 18, 85]
df.loc[4] = ['aharva', 18, 82]
df.loc[4] = ['kunal', 18, 70]
df.loc[4] = ['tejas', 18, 72]
df.loc[4] = ['sopan', 18, 86]
df.loc[4] = ['monu', 18, 98]
df.loc[4] = ['om', 18, 56]
print(df)
print("Shape=",df.shape)
print("DataTypes=\n",df.dtypes)
#print("Description=\n",df.describe)
print("Information=\n",df.info())
