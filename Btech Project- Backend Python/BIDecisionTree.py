import pandas as pd #For data manipulation

#For decision tree visualization
from sklearn.tree import export_graphviz 

#import petl as etl

# Import Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier 

# Import train_test_split function
from sklearn.model_selection import train_test_split 

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics 

#For representation of tree in text format
from sklearn import tree

#For extraction of data
dataSales = pd.read_excel (r'C:\Users\RUTUJA\Desktop\RUTUJA\FINAL YEAR PROJECT\BI_Information_Data.xlsx', sheet_name='Sales') 
    
dataStocks = pd.read_excel (r'C:\Users\RUTUJA\Desktop\RUTUJA\FINAL YEAR PROJECT\BI_Information_Data.xlsx', sheet_name='Stocks') 

dataCI = pd.read_excel (r'C:\Users\RUTUJA\Desktop\RUTUJA\FINAL YEAR PROJECT\BI_Information_Data.xlsx', sheet_name='Customer Information') 
    
dataRevenue = pd.read_excel (r'C:\Users\RUTUJA\Desktop\RUTUJA\FINAL YEAR PROJECT\BI_Information_Data.xlsx', sheet_name='Revenue') 

#For display of all the dataframe
with pd.option_context('display.max_rows',None,'display.max_columns',None):
    print(dataSales)
    print(dataStocks)
    print(dataCI)
    print(dataRevenue)
    
#Transforming of data
#Data cleaning
    
# Data Renaming of the column
dataSalesETL = dataSales.rename(columns = {"Cost per month (INR)" : "Cost incurred of goods per month (INR)"})
print("RENAMING THE COLUMN --------------")
print(dataSalesETL)

# Transforming month to dataframe
dataMonth = dataSales["Month"]
print(dataMonth)

#Transforming and conversion of data profit
dataSalesConversion = dataSales["Total profit made (Overall for the shop) [INR]"].astype(float)
print("CONVERSION FROM INTEGER TO FLOAT -----------")
print(dataSalesConversion)

#Loading data into fact table using merge command
result = pd.merge(dataMonth,dataSales[['Month','Total profit made (Overall for the shop) [INR]']],on='Month',how='left')
result = pd.merge(result,dataStocks[['Month','Number of goods sold']],on='Month',how='left')
result = pd.merge(result, dataStocks[['Month','Inventory']],on='Month',how='left')
result = pd.merge(result, dataCI[['Month','Customer Fluctuation']],on='Month',how='left')
result = pd.merge(result, dataCI[['Month','Total Customers']],on='Month',how='left')
print("Result Table with all the facts")
print(result)

#Transposing the result table
print("TRANSPOSE ----------------")
result1 = result.transpose()
print(result1)

#Showing the minimum values of final table
print("MINIMUM VALUES ---------------")
minValue = result.min()
print(minValue)

#Showing the maximum values of final table
print("MAXIMUM VALUES ---------------")
maxValue = result.max()
print(maxValue)

#Show the complete final table 
with pd.option_context('display.max_rows',None,'display.max_columns',None):
    print(result)
 
#The fetures chosen for the decision tree
feature_cols = ['Number of goods sold','Inventory','Customer Fluctuation']
# Features transfer
X = result[feature_cols]
# Target variable
y = result['Total profit made (Overall for the shop) [INR]']
print(y)

# 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# Visualize data of the tree in text representation
text_representation = tree.export_text(clf)
print(text_representation)

#Creation of the decision tree in dot format, then export it to graphviz
export_graphviz(clf, out_file='profitree.dot')

