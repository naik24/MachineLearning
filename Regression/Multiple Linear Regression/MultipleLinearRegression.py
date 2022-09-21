#MULTIPLE LINEAR REGRESSION

#DATASET: 50 STARTUPS
# ------- Profit and Expenditure
# ------- 5 Columns

#TASK: ANALYZE THE DATA AND CREATE A MODEL

#END GOAL: TO PROVIDE VENTURE CAPITALIST WITH INFO ON VARIOUS PARAMETERS(DEPENDENT VARIABLES) THAT
# ------- HELP COMPANIES MAKE PROFIT

#DEPENDENT VARIABLE: PROFIT
#INDEPENDENT VARIABLE: R&D SPEND, ADMINISTRATION, MARKETING SPEND, STATE

#IMPORTING LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression


#IMPORTING THE DATASET
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

#ENCODING CATEGORICAL DATA
ct = ColumnTransformer(transformers = [('encoder', OneHotEncoder(), [3])], remainder = 'passthrough')
X = np.array(ct.fit_transform(X))

#SPLITTING THE DATASET INTO TRAINING AND TEST SET
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

#TRAINING THE MULTIPLE LINEAR REGRESSION MODEL ON THE TRAINING SET
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#PREDICTING THE TEST SET RESULTS
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), axis=1))






