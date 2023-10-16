import pandas as pd
import numpy as np
from sklearn import preprocessing
import scipy.stats as s
#creating dataframe
d={'c01':[1,3,7,4], 'c02':[12,2,7,1], 'c03':[22,34,-11,9]}
df2 = pd.DataFrame(d)
print("\n Original data values")

print(df2)

#Rescaling data
print("\n\ndata scaling betweeen 0 to 1")
data_scaler = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled = data_scaler.fit_transform(df2)
print("\nMin Max Scaled data")
print(data_scaled.round(2))


#Normalization rescales such that sumof each row is 1
dn = preprocessing.normalize(df2, norm='l1')
print("\nL1 Normalized Data ")
print(dn.round(2))

#Binarize data (make Binary)
data_binarized = preprocessing.Binarizer(threshold=5).transform(df2)
print("\nBinarized data")
print(data_binarized)

#Standardize data
print("\nStandardize data")
x_train = np.array([[1.,-1.,2.],[2.,0.,0.],[0.,1.,-1.]])
print("\nOriginal Data \n",x_train)
print("\nInitial mean : ",s.tmean(x_train).round(2))
print("Initial Standard deviation :",round(x_train.std(),2))
x_scaled = preprocessing.scale(x_train)
x_scaled.mean(axis=0)
x_scaled.std(axis=0)
print("\nStadardized data :\n",x_scaled.round(2))
print("\nScaled mean : ",s.tmean(x_scaled).round(2))
print("\nScaled standard Deviation : ",round(x_scaled.std(),2))






'''
Output:

ty28@pc56:~/TY28/FDS/ASSIGNMENT_03/SET_B$ python3 A3setB.py

 Original data values
   c01  c02  c03
0    1   12   22
1    3    2   34
2    7    7  -11
3    4    1    9


data scaling betweeen 0 to 1

Min Max Scaled data
[[0.   1.   0.73]
 [0.33 0.09 1.  ]
 [1.   0.55 0.  ]
 [0.5  0.   0.44]]

L1 Normalized Data 
[[ 0.03  0.34  0.63]
 [ 0.08  0.05  0.87]
 [ 0.28  0.28 -0.44]
 [ 0.29  0.07  0.64]]
/usr/local/lib/python3.9/dist-packages/sklearn/base.py:458: UserWarning: X has feature names, but Binarizer was fitted without feature names
  warnings.warn(

Binarized data
[[0 1 1]
 [0 0 1]
 [1 1 0]
 [0 0 1]]

Standardize data

Original Data 
 [[ 1. -1.  2.]
 [ 2.  0.  0.]
 [ 0.  1. -1.]]

Initial mean :  0.44
Initial Standard deviation : 1.07

Stadardized data :
 [[ 0.   -1.22  1.34]
 [ 1.22  0.   -0.27]
 [-1.22  1.22 -1.07]]

Scaled mean :  0.0

Scaled standard Deviation :  1.0


'''
