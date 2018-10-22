import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

mpl.rcParams['patch.force_edgecolor'] = True # gridlines between bins

customers = pd.read_csv("Ecommerce Customers")

print(customers.head())
print(customers.describe())
print(customers.info())

sns.set_palette("GnBu_d")
sns.set_style('whitegrid')

sns.jointplot(x='Time on Website',y='Yearly Amount Spent',data=customers)
sns.jointplot(x='Time on App',y='Yearly Amount Spent',data=customers)
sns.jointplot(x='Time on App',y='Length of Membership',kind='hex',data=customers)
sns.pairplot(customers)
sns.lmplot(x='Length of Membership',y='Yearly Amount Spent',data=customers)
#plt.show()

# Training and Testing Data
y = customers['Yearly Amount Spent']
X = customers[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

lm = LinearRegression() # create an instance of model
lm.fit(X_train,y_train) # train with training data

# The coefficients
print('Coefficients: \n', lm.coef_)

predictions = lm.predict(X_test)

plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')

# Evaluating the Model
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

print(metrics.explained_variance_score(y_test, predictions)) # R^2 score = 1 - (var_res/var_tot)

# histogram of the residuals and make sure it looks normally distributed
sns.distplot((y_test-predictions),bins=50)

coeffecients = pd.DataFrame(lm.coef_, X.columns)
coeffecients.columns = ['Coeffecient']

print(coeffecients)
