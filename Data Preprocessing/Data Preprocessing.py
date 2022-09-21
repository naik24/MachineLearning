# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Taking care of missing data
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# ENCODING CATEGORICAL DATA
# Encoding independent variables
column_transform = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(column_transform.fit_transform(X))

# Encoding dependent variable
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Splitting dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, train_size=0.8, random_state=1)

# Feature Scaling
# feature scaling should be done after splitting the dataset into training and test set
# feature scaling is not required for all the datasets
# Normalization is preferred when the features are normally distributed
# Standardization works well all the time
scaler = StandardScaler()
X_train[:, 3:] = scaler.fit_transform(X_train[:, 3:])
X_test[:, 3:] = scaler.transform(X_train[:, 3:])
# We apply only the transform function to the test set because we want to transform the test set
# but don't want to fit it
