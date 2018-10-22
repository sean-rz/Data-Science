import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


mpl.rcParams['patch.force_edgecolor'] = True # gridlines between bins

usa_housing = pd.read_csv('USA_Housing.csv')
print(usa_housing.head())
print(usa_housing.info())
print(usa_housing.describe())
print(usa_housing.columns)

sns.pairplot(usa_housing)
sns.distplot(usa_housing['Price'])
sns.heatmap(usa_housing.corr(), annot=True)
#plt.show()


# Training model
x = usa_housing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']] # features to train on
y = usa_housing['Price']  # target variable

x_tarin, x_test,  y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=101)

lm = LinearRegression() # instamtiate linear model object
lm.fit(x_tarin, y_train) # train model

print(lm.intercept_)
coeff_df = pd.DataFrame(lm.coef_,x.columns,columns=['Coefficient'])
print(coeff_df)

predictions = lm.predict(x_test) # predictions from our model

plt.scatter(y_test, predictions)

# residual histogram
sns.distplot((y_test - predictions), bins=50)

#plt.show()

# Regression Evaluation Metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))


# boston dataset: http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html
from sklearn.datasets import load_boston
boston = load_boston()
print(boston.DESCR)
boston_df = boston.data
