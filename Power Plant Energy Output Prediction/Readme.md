# Power Plant Energy Output Prediction

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

- Best Parameters:  {'criterion': 'squared_error', 'max_features': 0.5, 'min_samples_split': 3, 'splitter': 'best'}
- R2 Score: 0.9345983117683193
- Mean Absolute Error (MAE): 2.9181138975966574

## Random Forest Regression

- Best Parameters:  {'max_depth': 5, 'min_samples_split': 3, 'n_estimators': 200}
- R2 Score: 0.9396165809806046
- Mean Absolute Error (MAE): 3.281809800817834
