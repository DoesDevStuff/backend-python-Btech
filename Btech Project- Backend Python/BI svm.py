# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:09:27 2020

@author: prach
"""

import pandas as pd

df=pd.read_csv("downloads\ML_dataset.csv")

df.head()
data= list(df)
data=data[1:][:]

#SVM
x=df.drop("Total Profit", axis=1)
y=df["Total Profit"]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train, y_test = train_test_split(x,y, test_size=0.2)
z=list(y_train)
ytest=list(y_test)

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

svclassifier = SVC(kernel='linear')
svclassifier.fit(x_train,z)
output=list(svclassifier.predict(x_test))
output

accs=accuracy_score(ytest,output)
print("Accuracy score=", accs)

