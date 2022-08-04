from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

df=pd.read_csv("content/train_u6lujuX_CVtuZ9i.csv")

df.isnull().sum()

df=df.dropna()

df.isnull().sum()

df = df.replace(to_replace='3+', value=4)

df.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0}, 'Self_Employed':{'No':0,'Yes':1}, 'Property_Area':{'Rural':0,'Semiurban':1, 'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)


X = df.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y = df['Loan_Status']

X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=2)

mlash = svm.SVC(kernel='linear')

mlash.fit(X_train,Y_train)

X_train_prediction = mlash.predict(X_train)
training_data_accuray = accuracy_score(X_train_prediction,Y_train)

print('Accuracy on training data : ', training_data_accuray)

y_pred = mlash.predict(X_test)
test_data_accuray = accuracy_score(y_pred,Y_test)

print('Accuracy on test data : ', test_data_accuray)

flash=RandomForestClassifier(n_estimators=100)

flash.fit(X_train,Y_train)

len(flash.estimators_)

y_pred=flash.predict(X_test)

print("accuracy of the model :",accuracy_score(Y_test,y_pred))

villan=LogisticRegression()

villan.fit(X_train,Y_train)

y_pred=villan.predict(X_test)

print("accuracy of the model :",accuracy_score(Y_test,y_pred))

mf=pd.read_csv('content/test_Y3wMUE5_7gLdaTN.csv')

mf.isnull().sum()

mf=mf.dropna()

mf.isnull().sum()

mf.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1}, 'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)

mf = mf.replace(to_replace='3+', value=4)

M = mf.drop(columns=['Loan_ID',],axis=1)

mf["Loan_Status"]=flash.predict(M)


mf.to_csv("Loan_Status.csv",header=True,index=False)