"""compile_nyc_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lE9ZsWA7k0QmUm6_l6y8kDCbfqYzpZMM

XGBoost binary classification for NYC lead dataset
Issue: requires NVIDIA GPU (e.g. running on AWS)
"""

#import libraries
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder

#import csvs into dataframes
t1 = pd.read_csv('https://raw.githubusercontent.com/eric-r-cooper/NYC_Lead_Locator/master/APP_DATA_address.csv')
t2 = pd.read_csv('https://raw.githubusercontent.com/eric-r-cooper/NYC_Lead_Locator/master/APP_DATA_yr.csv')
t3 = pd.read_csv('https://raw.githubusercontent.com/eric-r-cooper/NYC_Lead_Locator/master/APP_DATA_lat.csv')
t4 = pd.read_csv('https://raw.githubusercontent.com/eric-r-cooper/NYC_Lead_Locator/master/APP_DATA_lon.csv')
df = t1.merge(t2)
df = df.merge(t3)
df = df.merge(t4)
df.drop(columns=['Unnamed: 0'],inplace=True)
print("length of df: " + str(df.shape[0]))

df.head()

#prepare x/y features
X, y = df.drop('Prediction', axis=1), df['Prediction']

#y_encoded = OrdinalEncoder().fit_transform(y)

#convert non numerical data to categorical format for xgboost
non_nums = X.select_dtypes(exclude=np.number).columns.to_list()
for col in non_nums:
  X[col] = X[col].astype('category')

#split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Create classification matrices
dtrain_clf = xgb.DMatrix(X_train, y_train, enable_categorical=True)
dtest_clf = xgb.DMatrix(X_test, y_test, enable_categorical=True)

#set parameters and metrics
params = {"objective": "binary:logistic", "tree_method": "gpu_hist", "num_class": 6}
n = 1000

results = xgb.cv(
   params, dtrain_clf,
   num_boost_round=n,
   nfold=6,
   metrics=["mlogloss", "auc", "merror"],
   early_stopping_rounds=20
)

#output results column maximum
results['test-auc-mean'].max()