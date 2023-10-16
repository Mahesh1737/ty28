import pandas as pd
import matplotlib.pyplot as plt
#data = [['mahesh',18,99],['abhi',18,90],['gaurav',18,85],['jay',18,75]]
df = pd.DataFrame(columns = ['name','age','precentage'])
df.loc[0] = ['mahesh', 18, 99]
df.loc[1] = ['jay', 18, 36]
df.loc[2] = ['abhi', 18, 90]
df.loc[3] = ['gaurav', 18, 85]
df.loc[4] = ['aharva', 18, 82]
df.loc[5] = ['kunal', 18, 70]
df.loc[6] = ['tejas', 18, 72]
df.loc[7] = ['sopan', 18, 86]
df.loc[8] = ['monu', 18, 98]
df.loc[9] = ['om', 18, 56]
df.loc[10] = ['yash', 18, 95]
df.loc[11] = ['shri', 18, 99]
df.loc[12] = ['omkar', 18, 95]
df.loc[13] = ['mahesh', 18, 99]
df.loc[14] = ['zoro', 18, 36]
df["remarks"]=None
#print("information=",df.info())
#print(df.drop(columns='remarks', axis='1', inplace=True))
#print(df.isnull())
#df.plot(x='name', y='precentage')
df.plot.scatter(x='name', y='precentage')
plt.show()
