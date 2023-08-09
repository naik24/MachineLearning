# Housing Prices Prediction [![access-code-here](https://img.shields.io/badge/Access%20Code-Here-1f425f.svg)](https://github.com/naik24/MachineLearning/blob/master/Housing%20Prices%20Prediction/Housing_Prices_Prediction.ipynb)

**Objective**: Predict final price a house

## File Descriptions

**train.csv**: training set </br> 
**test.csv**: test set </br>
**data_description.txt**: full description of each column, originally prepared by Dean De Cock

## Data Fields
- **SalePrice** - the property's sale price in dollars. This is the target variable that you're trying to predict.</br>
- **MSSubClass**: The building class</br>
- **MSZoning**: The general zoning classification</br>
- **LotFrontage**: Linear feet of street connected to property</br>
- **LotArea**: Lot size in square feet</br>
- **Street**: Type of road access</br>
- **Alley**: Type of alley access</br>
- **LotShape**: General shape of property</br>
- **LandContour**: Flatness of the property</br>
- **Utilities**: Type of utilities available</br>
- **LotConfig**: Lot configuration</br>
- **LandSlope**: Slope of property</br>
- **Neighborhood**: Physical locations within Ames city limits</br>
- **Condition1**: Proximity to main road or railroad</br>
- **Condition2**: Proximity to main road or railroad (if a second is present)</br>
- **BldgType**: Type of dwelling</br>
- **HouseStyle**: Style of dwelling</br>
- **OverallQual**: Overall material and finish quality</br>
- **OverallCond**: Overall condition rating</br>
- **YearBuilt**: Original construction date</br>
- **YearRemodAdd**: Remodel date</br>
- **RoofStyle**: Type of roof</br>
- **RoofMatl**: Roof material</br>
- **Exterior1st**: Exterior covering on house</br>
- **Exterior2nd**: Exterior covering on house (if more than one material)</br>
- **MasVnrType**: Masonry veneer type</br>
- **MasVnrArea**: Masonry veneer area in square feet</br>
- **ExterQual**: Exterior material quality</br>
- **ExterCond**: Present condition of the material on the exterior</br>
- **Foundation**: Type of foundation</br>
- **BsmtQual**: Height of the basement</br>
- **BsmtCond**: General condition of the basement</br>
- **BsmtExposure**: Walkout or garden level basement walls</br>
- **BsmtFinType1**: Quality of basement finished area</br>
- **BsmtFinSF1**: Type 1 finished square feet</br>
- **BsmtFinType2**: Quality of second finished area (if present)</br>
- **BsmtFinSF2**: Type 2 finished square feet</br>
- **BsmtUnfSF**: Unfinished square feet of basement area</br>
- **TotalBsmtSF**: Total square feet of basement area</br>
- **Heating**: Type of heating</br>
- **HeatingQC**: Heating quality and condition</br>
- **CentralAir**: Central air conditioning</br>
- **Electrical**: Electrical system</br>
- **1stFlrSF**: First Floor square feet</br>
- **2ndFlrSF**: Second floor square feet</br>
- **LowQualFinSF**: Low quality finished square feet (all floors)</br>
- **GrLivArea**: Above grade (ground) living area square feet</br>
- **BsmtFullBath**: Basement full bathrooms</br>
- **BsmtHalfBath**: Basement half bathrooms</br>
- **FullBath**: Full bathrooms above grade</br>
- **HalfBath**: Half baths above grade</br>
- **Bedroom**: Number of bedrooms above basement level</br>
- **Kitchen**: Number of kitchens</br>
- **KitchenQual**: Kitchen quality</br>
- **TotRmsAbvGrd**: Total rooms above grade (does not include bathrooms)</br>
- **Functional**: Home functionality rating</br>
- **Fireplaces**: Number of fireplaces</br>
- **FireplaceQu**: Fireplace quality</br>
- **GarageType**: Garage location</br>
- **GarageYrBlt**: Year garage was built</br>
- **GarageFinish**: Interior finish of the garage</br>
- **GarageCars**: Size of garage in car capacity</br>
- **GarageArea**: Size of garage in square feet</br>
- **GarageQual**: Garage quality</br>
- **GarageCond**: Garage condition</br>
- **PavedDrive**: Paved driveway</br>
- **WoodDeckSF**: Wood deck area in square feet</br>
- **OpenPorchSF**: Open porch area in square feet</br>
- **EnclosedPorch**: Enclosed porch area in square feet</br>
- **3SsnPorch**: Three season porch area in square feet</br>
- **ScreenPorch**: Screen porch area in square feet</br>
- **PoolArea**: Pool area in square feet</br>
- **PoolQC**: Pool quality</br>
- **Fence**: Fence quality</br>
- **MiscFeature**: Miscellaneous feature not covered in other categories</br>
- **MiscVal**: $Value of miscellaneous feature</br>
- **MoSold**: Month Sold</br>
- **YrSold**: Year Sold</br>
- **SaleType**: Type of sale</br>
- **SaleCondition**: Condition of sale</br>

## Data Preprocessing

- **Data Loading**:We start by loading the data using the Pandas library. After loading the dataset, we remove the irrelevant columns.
- **Data Exploration**: In this step we get more familiar with the data. We identify the datatype of each feature and also determine the missing values from different features.
- **Imputing Missing Values**: Once all the missing values are identified, we impute the missing values with values depending on the type of data. For example, the missing values in the feature LotFrontage are replaced by the mean of the feature since there are varying sizes of Lot Frontages.
- **Encoding Categorical Variables**: After all the missing values are imputed, we encode the categorical variables using the getdummies() function of the Pandas library
- **Splitting Data into Train and Test Set**: Finally, we split the data into training and testing set where training set will be used to train the model and testing set will be used to evaluate predictions.

## Linear Regression

- **R2 Score**: 0.8811433982648353
- **Mean Absolute Error (MAE)**: 18053.572344074524

## Support Vector Regression

- **Best Parameters (using Grid Search)**:  {'degree': 1, 'kernel': 'linear'}
- **R2 Score**: 0.7796873450211113
- **Mean Absolute Error (MAE)**: 24332.061036062158

## Decision Tree Regression

- **Best Parameters (using Grid Search)**:  {'criterion': 'absolute_error', 'max_features': 0.5, 'min_samples_split': 3, 'splitter': 'best'}
- **R2 Score**: 0.7451960949127842
- **Mean Absolute Error (MAE)**: 28223.755136986303

## Random Forest Regression

- **Best Parameters (Using Grid Search)**:  {'max_depth': 5, 'min_samples_split': 3, 'n_estimators': 200}
- **R2 Score**: 0.8428823251541103
- **Mean Absolute Error (MAE)**: 21381.583523691235

## XGBoost

- **Best Parameters**:  {'colsample_bytree': 0.5, 'eta': 0.1, 'max_depth': 3, 'n_estimators': 300, 'subsample': 1}
- **R2 Score**: 0.927513948978635 ⭐
- **Mean Absolute Error (MAE)**: 14120.409581014555 ⭐

## References:
[1] House Prices - Advanced Regression Techniques, https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/overview
