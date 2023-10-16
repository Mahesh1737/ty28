#1
'''import numpy as np
demo = np.array([[0,1],[2,3]])
print("Original array : ")
print(demo)

print("Maximum value of the flattened array : ",np.max(demo))

print("Minimum value of the flattened array : ",np.min(demo))'''

#2

'''import numpy as np
import scipy.stats as s
import matplotlib.pyplot as plt

p1 = [1,2,3]
p2 = [5,6,7]
dist = np.linalg.norm(p1,p2)
print("Euclidean distance between P1 & p2 : ",dist)'''

#3

'''import numpy as np
import scipy.stats as s

data = np.array([45,12,78,63,78,89])
mean = np.mean(data)
range1 = (np.max(data) - np.min(data))
q2,q1 = np.percentile(data,[75,25])
print("Date : ",data)
print("Mean of data : ",mean)
print("Range of data : ",range1)
print("Inter quantile range : ",q2-q1) '''

#4

'''import numpy as np
def dist(x,y,n):
    sum1=0
    for i in range(n):
        for j in range(i+1,n):
            sum1+=(abs(x[i] - x[j]))+(abs(y[i] - y[j]))
    return sum1
x=[1,2,3,4]
y=[1,2,3,4]
n = len(x)
print("Manhatten Distance : ",dist(x,y,n))'''


#5

'''import numpy as np
import matplotlib.pyplot as plt
nums = np.array([0.5,0.7,1,1.2,1.3,2.1])
bins = np.array([0,1,2,3])
plt.hist(nums,bins,color='magenta',edgecolor='black')
print("Result : ")
plt.show()'''

#6
import numpy as np
import pandas as pd
import scipy.stats as s

df = pd.DataFrame(columns = ['name','age','precentage'])
df.loc[0] = ['mahesh', 18, 99]
df.loc[1] = ['jay', 18, 36]
df.loc[2] = ['abhi', 18, 90]
df.loc[3] = ['gaurav', 18, 85]
df.loc[4] = ['rupesh', 18, 35]
df.loc[5] = ['Atharva', 18, 40]
df.loc[6] = ['Monu', 18, 50]
df.loc[7] = ['Monu', 18, 50]
df.loc[8] = ['sopan', 18, 99]
df.loc[9] = ['tejas', 18, 99]
print(df)
print("Statistical Data : ", df.describe())





'''output: 

ty28@pc61:~/TY28/FDS/ASSIGNMENT_02/SET_A$ python3 flat_arr.py
Original array : 
[[0 1]
 [2 3]]
Maximum value of the flattened array :  3
Minimum value of the flattened array :  0
ty28@pc61:~/TY28/FDS/ASSIGNMENT_02/SET_A$ python3 flat_arr.py
Traceback (most recent call last):
  File "/data/ty28/TY28/FDS/ASSIGNMENT_02/SET_A/flat_arr.py", line 15, in <module>
    import malplotlib.pyplot as plt
ModuleNotFoundError: No module named 'malplotlib'
ty28@pc61:~/TY28/FDS/ASSIGNMENT_02/SET_A$ python3 flat_arr.py
Euclidean distance between P1 & p2 :  [4.68288699 3.62044036 3.01257828]
ty28@pc61:~/TY28/FDS/ASSIGNMENT_02/SET_A$ python3 flat_arr.py
Date :  [45 12 78 63 78 89]
Mean of data :  60.833333333333336
Range of data :  77
Inter quantile range :  28.5
ty28@pc61:~/TY28/FDS/ASSIGNMENT_02/SET_A$ python3 flat_arr.py
Manhatten Distance :  20
ty28@pc61:~/TY28/FDS/ASSIGNMENT_02/SET_A$ python3 flat_arr.py
Result : 
ty28@pc61:~/TY28/FDS/ASSIGNMENT_02/SET_A$ python3 flat_arr.py
Traceback (most recent call last):
  File "/data/ty28/TY28/FDS/ASSIGNMENT_02/SET_A/flat_arr.py", line 65, in <module>
    df = pd.DataFrame(columns = ['name','age','precentage'])
NameError: name 'pd' is not defined
ty28@pc61:~/TY28/FDS/ASSIGNMENT_02/SET_A$ python3 flat_arr.py
      name  age  precentage
0   mahesh   18          99
1      jay   18          36
2     abhi   18          90
3   gaurav   18          85
4   rupesh   18          35
5  Atharva   18          40
6     Monu   18          50
7     Monu   18          50
8    sopan   18          99
9    tejas   18          99
ty28@pc61:~/TY28/FDS/ASSIGNMENT_02/SET_A$ python3 flat_arr.py
      name  age  precentage
0   mahesh   18          99
1      jay   18          36
2     abhi   18          90
3   gaurav   18          85
4   rupesh   18          35
5  Atharva   18          40
6     Monu   18          50
7     Monu   18          50
8    sopan   18          99
9    tejas   18          99
Statistical Data :          age  precentage
count  10.0   10.000000
mean   18.0   68.300000
std     0.0   28.284468
min    18.0   35.000000
25%    18.0   42.500000
50%    18.0   67.500000
75%    18.0   96.750000
max    18.0   99.000000'''

