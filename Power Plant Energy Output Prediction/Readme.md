# Power Plant Energy Output Prediction [![access-code-here](https://img.shields.io/badge/Access%20Code-Here-1f425f.svg)](https://github.com/naik24/MachineLearning/blob/master/Power%20Plant%20Energy%20Output%20Prediction/Power%20Plant%20Energy%20Output%20Prediction.ipynb)

**Objective**: Predict combined energy output of a power plant

## Filde Descriptions
- powerplantdata.csv: complete dataset

## Data Fields
- Temperature (T) in the range 1.81°C and 37.11°C
- Ambient Pressure (AP) in the range 992.89-1033.30 milibar
- Relative Humidity (RH) in the range 25.56% to 100.16%
- Exhaust Vacuum (V) in teh range 25.36-81.56 cm Hg
- Net hourly electrical energy output (EP) 420.26-495.76 MW

## Data Preprocessing
- Data Loading: We start by loading the data using the Pandas library
- Data Splitting: We split the data into features and target
- Standardization: Since the range of features varies from one another, we bring them to a common scale using StandardScaler() library from Scikit-learn
- Training and Test Set: We split the data into and training and test sets

## Linear Regression

- **R2 Score**: 0.9298994694436788
- **Mean Absolute Error (MAE)**: 3.630457657633138

## Support Vector Regression
- Best Parameters:  {'degree': 1, 'kernel': 'rbf'}
- R2 Score: 0.9399144198187595
- Mean Absolute Error (MAE): 3.243724596733692

## Decision Tree Regression

- Best Parameters:  {'criterion': 'friedman_mse', 'max_features': 'sqrt', 'min_samples_split': 3, 'splitter': 'best'}
- R2 Score: 0.9316469233468714
- Mean Absolute Error (MAE): 3.075381400208986

## Random Forest Regression

- Best Parameters:  {'max_depth': 5, 'min_samples_split': 3, 'n_estimators': 100}
- R2 Score: 0.9395283394768524
- Mean Absolute Error (MAE): 3.2807245334839754

## XGBoost

- Best Parameters:  {'colsample_bytree': 1, 'eta': 0.1, 'max_depth': 7, 'n_estimators': 300, 'subsample': 1}
- R2 Score: 0.9701050030370023 ⭐
- Mean Absolute Error (MAE): 2.1224856111373023 ⭐

## References:

[1] Combined Cycle Power Plant Dataset, https://archive.ics.uci.edu/dataset/294/combined+cycle+power+plant
