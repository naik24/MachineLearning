# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Importing Datasets
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, : -1].values
y = dataset.iloc[:, -1].values

print(dataset)

# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, train_size = 0.8, random_state=1)

# Training the Simple Linear Regression model on the training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting the test set results
y_predicted = regressor.predict(X_test)

#Visualizing training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train))
plt.title('Salary v/s Experience (Training Set)')
plt.xlabel('Experience (in years)')
plt.ylabel('Salary (in dollars)')
plt.show()

#Visualizing test set results
plt.scatter(X_test, y_test, color = 'blue')
plt.plot(X_train, regressor.predict(X_train))
plt.title('Salary v/s Experience (Test Set)')
plt.xlabel('Experience (in years)')
plt.ylabel('Salary (in dollars)')
plt.show()

#Making a single prediction
print(regressor.predict([[100]]))

#Getting the final linear regression equation with the values of the coefficients
print('b0: ', regressor.coef_)
print('b1: ', regressor.intercept_)
