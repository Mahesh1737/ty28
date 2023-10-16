import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as s
df = pd.read_csv('SOCR-HeightWeight.csv')
df["BMI"]=df["Weight(Pounds)"]/(df["Height(Inches)"])**2
print(max(df["BMI"]))
print(min(df["BMI"]))

df.plot.scatter(x="Height(Inches)", y="Weight(Pounds)")
plt.show()
