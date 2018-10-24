import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# set index_col=0 to use the first column as the index
df = pd.read_csv("Classified Data", index_col=0)
print(df.head())

#########################################################
# Standardize the Variables
#########################################################
'''
Because the KNN classifier predicts the class of a given test observation by identifying 
the observations that are nearest to it, the scale of the variables matters. Any variables 
that are on a large scale will have a much larger effect on the distance between the observations, 
and hence on the KNN classifier, than variables that are on a small scale.

Standardize features by removing the mean and scaling to unit variance

Centering and scaling happen independently on each feature by computing the relevant statistics on 
the samples in the training set. Mean and standard deviation are then stored to be used on later data 
using the transform method.

Standardization of a dataset is a common requirement for many machine learning estimators. They might 
behave badly if the individual features do not more or less look like standard normally distributed data 
(e.g. Gaussian with 0 mean and unit variance).

Many elements used in the objective function of a learning algorithm assume that all features are centered
around 0 and have variance in the same order. If a feature has a variance that is orders of magnitude larger 
than others, it might dominate the objective function and make the estimator unable to learn from other features 
correctly as expected.

fit basically just calculates the mean and std, then transform actually changes the data
'''
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(df.drop('TARGET CLASS',axis=1))
scaled_features = scaler.transform(df.drop('TARGET CLASS',axis=1))

df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1]) # -1 means except the last column
df_feat.head()

# Train Test Split

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(scaled_features,df['TARGET CLASS'], test_size=0.30, random_state=101)


# Using KNN

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)  # k=1
knn.fit(X_train,y_train)
pred = knn.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))


# choosing a good k value

error_rate = []

for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(y_test != pred_i))

plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)

plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

# after arouns K>23 the error rate just tends to hover around 0.06-0.05

# FIRST A QUICK COMPARISON TO OUR ORIGINAL K=1
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('WITH K=1')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))


# NOW WITH K=17
knn = KNeighborsClassifier(n_neighbors=17)

knn.fit(X_train,y_train)
pred = knn.predict(X_test)

print('WITH K=17')
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(classification_report(y_test,pred))
