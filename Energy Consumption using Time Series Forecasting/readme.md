# Energy Consumption Prediction using Time Series Forecasting [![access-code-here](https://img.shields.io/badge/Access%20Code-Here-1f425f.svg)](https://github.com/naik24/MachineLearning/blob/master/Energy%20Consumption%20using%20Time%20Series%20Forecasting/Energy_Consumption_using_Time_Series_Forecasting.ipynb)

## Goal

To predict hourly/monthly/weekly/yearly energy consumption based on previous data.

## Data Information

PJM Interconnection LLC (PJM) is a regional transmission organization (RTO) in the United States. It is part of the Eastern Interconnection grid operating an electric transmission system serving all or parts of Delaware, Illinois, Indiana, Kentucky, Maryland, Michigan, New Jersey, North Carolina, Ohio, Pennsylvania, Tennessee, Virginia, West Virginia, and the District of Columbia. The hourly power consumption data comes from PJM's website and are in megawatts (MW). The regions have changed over the years so data may only appear for certain dates per region.

## Data Visualization

![image](https://github.com/naik24/MachineLearning/assets/69704762/28f5166a-ff75-4063-870c-5facf85b3a01)

## Feature Creation

The original data file consists of only two columns - Datetime and Energy Consumed. Using the datetime information we create features like hour, day of the week, quarter, month, year, day of year, day of month, and week of year. Using these features, we can analyze the energy consumption at different hours, days, months, etc. This information will help us predict the energy consumption at the given times. Below are the plots of energy consumption by hour and month.

<p align = "center"><img src = "https://github.com/naik24/MachineLearning/assets/69704762/931d2d1f-bab0-4490-8671-e575f3b95a23"></p>
<p align = "center"><img src = "https://github.com/naik24/MachineLearning/assets/69704762/29a8456f-0c05-468d-bd2e-90c7aa270d01"></p>

## Model Training

We train a XGBoost Regressor model using the following parameters:

- base_score = 0.5
- booster = 'gbtree'
- n_estimators = 1000
- early_stopping_rounds = 50
- objective = 'reg:linear'
- max_depth = 3
- learning_rate = 0.01

## Forecast on the Test Set
![image](https://github.com/naik24/MachineLearning/assets/69704762/238cd905-eb6d-4680-b345-5f15b611ee76)


