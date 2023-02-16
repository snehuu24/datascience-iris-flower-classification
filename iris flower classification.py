import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter("ignore")
df=pd.read_csv(r'C:UsersAdminDownloadsIris.csv')
df
df.info()
df.isnull().sum()
df.isnull().sum()
df.columns
Index(['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm',
       'Species'],
      dtype='object')
df=df.drop(columns="Id")
df
df['Species'].value_counts()
Iris-setosa        50
Iris-versicolor    50
Iris-virginica     50
Name: Species, dtype: int64
sns.countplot(df['Species']);
x=df.iloc[:,:4]
y=df.iloc[:,4]
x
y
0         Iris-setosa
1         Iris-setosa
2         Iris-setosa
3         Iris-setosa
4         Iris-setosa
            ...      
145    Iris-virginica
146    Iris-virginica
147    Iris-virginica
148    Iris-virginica
149    Iris-virginica
Name: Species, Length: 150, dtype: object
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)
x_train.shape
x_test.shape
y_train.shape
y_test.shape
