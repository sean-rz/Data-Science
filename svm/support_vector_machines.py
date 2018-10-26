# https://www.youtube.com/watch?v=-Z4aojJ-pdg
# https://www.youtube.com/watch?v=3liCbRZPrZA

import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

print(cancer.keys()) # dataset in dictionary form
print(cancer['DESCR'])
print(cancer['feature_names'])

df_feat = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
df_target = pd.DataFrame(cancer['target'],columns=['Cancer'])

print(df_feat.info())
print(cancer['target'])

print(df_feat.head())
print(df_target.head())

# trian test split
from sklearn.model_selection import train_test_split
# np.ravel() is used to return a contiguous flattened array of input data
X_train, X_test, y_train, y_test = train_test_split(df_feat, np.ravel(df_target), test_size=0.30, random_state=101)


# Train the Support Vector Classifier
from sklearn.svm import SVC
model = SVC()
model.fit(X_train,y_train)
predictions = model.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

####################################################################
# Gridsearch: This idea of creating a 'grid' of parameters and just 
# trying out all the possible combinations is called a Gridsearch.
####################################################################
# C controls the cost of misclassfication on the training data
# large C results in low bias and high variance
# gamma is a param for radio basis function (rbf) kernel
# large gamma value means Gaussian with low variance which means svm does not have wide-spread influence
from sklearn.model_selection import GridSearchCV

param_grid = {'C': [0.1,1, 10, 100, 1000], 'gamma': [1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']} 
grid = GridSearchCV(SVC(),param_grid,refit=True,verbose=3)
grid.fit(X_train,y_train)

'''
fit runs the same loop with cross-validation, to find the best parameter combination. 
Once it has the best combination, it runs fit again on all data passed to fit (without cross-validation),
to built a single new model using the best parameter setting
'''

print(grid.best_params_)
print(grid.best_estimator_)

# Re-run predictions on the grid
grid_predictions = grid.predict(X_test)
print(confusion_matrix(y_test,grid_predictions))
print(classification_report(y_test,grid_predictions))











