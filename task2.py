# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 11:15:51 2020
Linear Regression with Python Scikit Learn-
In this regression task we will predict the percentage of marks that a student is expected to score based 
upon the number of hours they studied. This is a simple linear regression task as it involves just two 
variables.

From the graph above, we can clearly see that there is a positive linear relation between the number of 
hours studied and percentage of score
@author: aashu
"""
#importing requisite libraries 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt


#importing dataset from external source to our python workspace using pandas
url = "http://bit.ly/w-data"
dataset = pd.read_csv(url)

X = dataset.iloc[ : ,0:1]
Y = dataset.iloc[ : ,1:2]

plt.scatter(X,Y,marker='.')
plt.xlabel('Hours studied',fontsize=20)
plt.ylabel('Scores obtained',fontsize=20)
plt.title('Hours studied vs Scores obtained')
plt.show()

from sklearn.model_selection import train_test_split
#splitting 80% of data into training set and 20% into test set
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

#training the algorithm
from sklearn.linear_model import LinearRegression
slr = LinearRegression()
slr.fit(X_train,y_train)

#predictions
print(slr.coef_)
""" This means that for every one unit of change in hours studied, the change in the score is about 9.91% """
line=slr.coef_*X+slr.intercept_
plt.scatter(X,Y)
plt.plot(X,line);
plt.show()

Y_predict=slr.predict(X_test)

#making predictions

df= pd.DataFrame({'Actual':[y_test], 'Predicted': [Y_predict]})

#Evaluating algorithm
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, Y_predict))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, Y_predict))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, Y_predict)))
