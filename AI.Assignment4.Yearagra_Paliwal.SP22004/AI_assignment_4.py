# -*- coding: utf-8 -*-
"""AI_Assignment_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nnZmUmUS2fSAfcJT_BjfI1SVjtBcyIzl

# Installation of Libraries
"""

!pip install pandas
!pip install numpy
!pip install matplotlib
!pip install scikit-learn
!pip install seaborn
!pip install https://github.com/pandas-profiling/pandas-profiling/archive/master.zip

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import metrics
from pandas_profiling import ProfileReport
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix

"""# Dataset"""

from google.colab import files
uploaded = files.upload()

"""DATASET

"""

import io
data = pd.read_csv(io.BytesIO(uploaded['roo_data.csv']))
data

"""# Preprocessing

RECLASSIFICATION OF VARIABLES
"""

data.loc[data['Suggested Job Role'] =='Data Architect','Suggested Job Role' ] = 'Architect'
data.loc[data['Suggested Job Role'] =='Solutions Architect','Suggested Job Role' ] = 'Architect'

data.loc[data['Suggested Job Role'] =='Technical Services/Help Desk/Tech Support','Suggested Job Role' ] = 'Support'
data.loc[data['Suggested Job Role'] =='Technical Support','Suggested Job Role' ] = 'Support'

data.loc[data['Suggested Job Role'] =='Database Manager','Suggested Job Role' ] = 'Manager'
data.loc[data['Suggested Job Role'] =='Information Technology Manager','Suggested Job Role' ] = 'Manager'
data.loc[data['Suggested Job Role'] =='Project Manager','Suggested Job Role' ] = 'Manager'

data.loc[data['Suggested Job Role'] == 'Network Security Administrator','Suggested Job Role'] = 'Admin'
data.loc[data['Suggested Job Role'] == 'Portal Administrator','Suggested Job Role'] = 'Admin'
data.loc[data['Suggested Job Role'] == 'Database Administrator','Suggested Job Role'] = 'Admin'
data.loc[data['Suggested Job Role'] == 'Systems Security Administrator','Suggested Job Role'] = 'Admin'

data.loc[data['Suggested Job Role'] =='UX Designer','Suggested Job Role' ] = 'Associate'
data.loc[data['Suggested Job Role'] =='Software Quality Assurance (QA) / Testing','Suggested Job Role' ] = 'Associate'
data.loc[data['Suggested Job Role'] =='Quality Assurance Associate','Suggested Job Role' ] = 'Associate'
data.loc[data['Suggested Job Role'] =='Information Technology Auditor','Suggested Job Role' ] = 'Associate'

data.loc[data['Suggested Job Role'] =='Network Engineer','Suggested Job Role' ] = 'Engineer'
data.loc[data['Suggested Job Role'] =='Network Security Engineer','Suggested Job Role' ] = 'Engineer'
data.loc[data['Suggested Job Role'] =='Software Engineer','Suggested Job Role' ] = 'Engineer'
data.loc[data['Suggested Job Role'] =='Software Systems Engineer','Suggested Job Role' ] = 'Engineer'
data.loc[data['Suggested Job Role'] =='Technical Engineer','Suggested Job Role' ] = 'Engineer'

data.loc[data['Suggested Job Role'] =='Applications Developer','Suggested Job Role' ] = 'Developer'
data.loc[data['Suggested Job Role'] =='CRM Technical Developer','Suggested Job Role' ] = 'Developer'
data.loc[data['Suggested Job Role'] =='Database Developer','Suggested Job Role' ] = 'Developer'
data.loc[data['Suggested Job Role'] =='Mobile Applications Developer','Suggested Job Role' ] = 'Developer'
data.loc[data['Suggested Job Role'] =='Software Developer','Suggested Job Role' ] = 'Developer'
data.loc[data['Suggested Job Role'] =='Web Developer','Suggested Job Role' ] = 'Developer'

data.loc[data['Suggested Job Role'] =='Business Intelligence Analyst','Suggested Job Role' ] = 'Analyst'
data.loc[data['Suggested Job Role'] =='Business Systems Analyst','Suggested Job Role' ] = 'Analyst'
data.loc[data['Suggested Job Role'] =='CRM Business Analyst','Suggested Job Role' ] = 'Analyst'
data.loc[data['Suggested Job Role'] =='Information Security Analyst','Suggested Job Role' ] = 'Analyst'
data.loc[data['Suggested Job Role'] =='Programmer Analyst','Suggested Job Role' ] = 'Analyst'
data.loc[data['Suggested Job Role'] =='Systems Analyst','Suggested Job Role' ] = 'Analyst'
data.loc[data['Suggested Job Role'] =='E-Commerce Analyst','Suggested Job Role' ] = 'Analyst'
data

"""LABEL ENCODING"""

label_encoder = preprocessing.LabelEncoder()

data['can work long time before system?']= label_encoder.fit_transform(data['can work long time before system?'])
data['self-learning capability?']= label_encoder.fit_transform(data['self-learning capability?'])
data['Extra-courses did']= label_encoder.fit_transform(data['Extra-courses did'])
data['certifications']= label_encoder.fit_transform(data['certifications'])
data['workshops']= label_encoder.fit_transform(data['workshops'])
data['talenttests taken?']= label_encoder.fit_transform(data['talenttests taken?'])
data['olympiads']= label_encoder.fit_transform(data['olympiads'])
data['reading and writing skills']= label_encoder.fit_transform(data['reading and writing skills'])
data['memory capability score']= label_encoder.fit_transform(data['memory capability score'])
data['Interested subjects']= label_encoder.fit_transform(data['Interested subjects'])
data['interested career area ']= label_encoder.fit_transform(data['interested career area '])
data['Job/Higher Studies?']= label_encoder.fit_transform(data['Job/Higher Studies?'])
data['Type of company want to settle in?']= label_encoder.fit_transform(data['Type of company want to settle in?'])
data['Taken inputs from seniors or elders']= label_encoder.fit_transform(data['Taken inputs from seniors or elders'])
data['interested in games']= label_encoder.fit_transform(data['interested in games'])
data['Interested Type of Books']= label_encoder.fit_transform(data['Interested Type of Books'])
data['Salary Range Expected']= label_encoder.fit_transform(data['Salary Range Expected'])
data['In a Realtionship?']= label_encoder.fit_transform(data['In a Realtionship?'])
data['Gentle or Tuff behaviour?']= label_encoder.fit_transform(data['Gentle or Tuff behaviour?'])
data['Management or Technical']= label_encoder.fit_transform(data['Management or Technical'])
data['Salary/work']= label_encoder.fit_transform(data['Salary/work'])
data['hard/smart worker']= label_encoder.fit_transform(data['hard/smart worker'])
data['worked in teams ever?']= label_encoder.fit_transform(data['worked in teams ever?'])
data['Introvert']= label_encoder.fit_transform(data['Introvert'])
data['Suggested Job Role']= label_encoder.fit_transform(data['Suggested Job Role'])
data

"""EDA REPORT """

#profile = ProfileReport(data, title="EDA Report")
#profile.to_notebook_iframe()

X= data.drop(columns='Suggested Job Role')
Y= data['Suggested Job Role']

"""# ARTIFICIAL NEURAL NETWORK (MLP CLASSIFIER) 
# (Parameter: activation = tanh, solver = sgd)
"""

split_ratio=[0.4,0.3,0.2,0.1]
hidden_layer_sizes=[(128,252,252,128),(118,246,246,118),(148,266,266,148),(108,222,222,108)]
# Hidden Layer 1 (128,252,252,128) = 10
# Hidden Layer 2 (118,246,246,118) = 20
# Hidden Layer 3 (148,266,266,148) = 30
# Hidden Layer 4 (108,222,222,108) = 40
Layer_Range=[10,20,30,40]
accuracy=[]
precision=[]
recall=[]
F1=[]

for i in range(0,4):
  X_train, X_test,Y_train,Y_test= train_test_split( X, Y, test_size=split_ratio[i], random_state=2)
  sc_X = StandardScaler()
  X_trainscaled=sc_X.fit_transform(X_train)
  X_testscaled=sc_X.transform(X_test)

  gd = MLPClassifier(activation='tanh', solver = 'sgd',early_stopping = True, hidden_layer_sizes=hidden_layer_sizes[i], verbose = 1, max_iter = 200).fit(X_trainscaled, Y_train)
  Y_pred=gd.predict(X_testscaled) 
  print("Accuracy:",metrics.accuracy_score(Y_test, Y_pred)*100,"%")
  accuracy.append(metrics.accuracy_score(Y_test, Y_pred)*100)

  print ("Precision: ",precision_score(Y_test, Y_pred, average='macro')*100,"%")
  precision.append(precision_score(Y_test, Y_pred, average='macro')*100)

  print ("F1: ",f1_score(Y_test, Y_pred, average='macro')*100,"%")
  F1.append(f1_score(Y_test, Y_pred, average='macro')*100)

  print ("Recall: ",recall_score(Y_test, Y_pred, average=None)*100,"%")
  recall.append(recall_score(Y_test, Y_pred, average=None)*100)

"""Accuracy"""

fig, ax = plt.subplots()
ax.plot(Layer_Range, accuracy, **{'color': 'lightsteelblue', 'marker': 'o'})
plt.legend(loc = "upper left")
plt.xlabel('Layer_range')
plt.ylabel('Accuracy')
print()
print("Accuracy:", accuracy,"%")
print()
plt.grid()
plt.show()

"""Precision"""

fig, ax = plt.subplots()
ax.plot(Layer_Range, precision, **{'color': 'lightsteelblue', 'marker': 'o'})
plt.legend(loc = "upper left")
plt.xlabel('Layer_range')
plt.ylabel('Precision')
print()
print("Precision:", precision,"%")
print()
plt.grid()
plt.show()

"""F1"""

fig, ax = plt.subplots()
ax.plot(Layer_Range, F1, **{'color': 'lightsteelblue', 'marker': 'o'})
plt.legend(loc = "upper left")
plt.xlabel('Layer_range')
plt.ylabel('F1')
print()
print("F1:", F1,"%")
print()
plt.grid()
plt.show()

"""Recall"""

fig, ax = plt.subplots()
ax.plot(Layer_Range, recall, **{'color': 'lightsteelblue', 'marker': 'o'})
plt.legend(loc = "upper left")
plt.xlabel('Layer_range')
plt.ylabel('Recall')
print()
print("Recall:", recall,"%")
print()
plt.grid()
plt.show()

"""# ARTIFICIAL NEURAL NETWORK (MLP CLASSIFIER) 
# (Parameter: activation = relu, solver = adam)
"""

from sklearn.metrics._plot.confusion_matrix import plot_confusion_matrix
split_ratio=[0.4,0.3,0.2,0.1]
hidden_layer_sizes=[(128,252,252,128),(118,246,246,118),(148,266,266,148),(108,222,222,108)]
# Hidden Layer 1 (128,252,252,128) = 10
# Hidden Layer 2 (118,246,246,118) = 20
# Hidden Layer 3 (148,266,266,148) = 30
# Hidden Layer 4 (108,222,222,108) = 40
Layer_Range=[10,20,30,40]
accuracy=[]
precision=[]
recall=[]
F1=[]

for i in range(0,4):
  X_train, X_test,Y_train,Y_test= train_test_split( X, Y, test_size=split_ratio[i], random_state=2)
  sc_X = StandardScaler()
  X_trainscaled=sc_X.fit_transform(X_train)
  X_testscaled=sc_X.transform(X_test)

  gd = MLPClassifier(activation='relu', solver = 'adam',early_stopping = True, hidden_layer_sizes=hidden_layer_sizes[i], verbose = 1, max_iter = 200).fit(X_trainscaled, Y_train)
  Y_pred=gd.predict(X_testscaled) 
  print("Accuracy:",metrics.accuracy_score(Y_test, Y_pred)*100,"%")
  accuracy.append(metrics.accuracy_score(Y_test, Y_pred)*100)

  print ("Precision: ",precision_score(Y_test, Y_pred, average='macro')*100,"%")
  precision.append(precision_score(Y_test, Y_pred, average='macro')*100)

  print ("F1: ",f1_score(Y_test, Y_pred, average='macro')*100,"%")
  F1.append(f1_score(Y_test, Y_pred, average='macro')*100)

  print ("Recall: ",recall_score(Y_test, Y_pred, average=None)*100,"%")
  recall.append(recall_score(Y_test, Y_pred, average=None)*100)




  plt.ylabel('True label')
  plt.xlabel('Predicted label')

"""Confussion Matrics"""

plt.figure(figsize=(10,10))
cf_matrix = confusion_matrix(Y_pred, Y_test)
sns.heatmap(cf_matrix/np.sum(cf_matrix), annot= True)

"""Accuracy"""

fig, ax = plt.subplots()
ax.plot(Layer_Range, accuracy, **{'color': 'lightsteelblue', 'marker': 'o'})
plt.legend(loc = "upper left")
plt.xlabel('Layer_range')
plt.ylabel('Accuracy')
print()
print("Accuracy:", accuracy,"%")
print()
plt.grid()
plt.show()

"""Precision"""

fig, ax = plt.subplots()
ax.plot(Layer_Range, precision, **{'color': 'lightsteelblue', 'marker': 'o'})
plt.legend(loc = "upper left")
plt.xlabel('Layer_range')
plt.ylabel('Precision')
print()
print("Precision:", precision,"%")
print()
plt.grid()
plt.show()

"""F1"""

fig, ax = plt.subplots()
ax.plot(Layer_Range, F1, **{'color': 'lightsteelblue', 'marker': 'o'})
plt.legend(loc = "upper left")
plt.xlabel('Layer_range')
plt.ylabel('F1')
print()
print("F1:", F1,"%")
print()
plt.grid()
plt.show()

"""Recall"""

fig, ax = plt.subplots()
ax.plot(Layer_Range, recall, **{'color': 'lightsteelblue', 'marker': 'o'})
plt.legend(loc = "upper left")
plt.xlabel('Layer_range')
plt.ylabel('Recall')
print()
print("Recall:", recall,"%")
print()
plt.grid()
plt.show()