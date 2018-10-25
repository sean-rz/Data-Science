# https://towardsdatascience.com/enchanted-random-forest-b08d418cb411
'''
Random forest uses bagging (picking a sample of observations rather than all of them) and random subspace method 
(picking a sample of features rather than all of them, in other words - attribute bagging) to grow a tree. 
If the number of observations is large, but the number of trees is too small, then some observations will be 
predicted only once or even not at all. If the number of predictors is large but the number of trees is too small, 
then some features can (theoretically) be missed in all subspaces used. Both cases results in the decrease of 
random forest predictive power. But the last is a rather extreme case, since the selection of subspace is performed 
at each node
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# get the data
df = pd.read_csv('kyphosis.csv')
print(df.head())

# EDA
sns.pairplot(df, hue='Kyphosis', palette='Set1', diag_kind='hist')
#plt.show()

# train test split 
from sklearn.model_selection import train_test_split

X = df.drop('Kyphosis',axis=1)
y = df['Kyphosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# single decision tree
from sklearn.tree import DecisionTreeClassifier

d_tree = DecisionTreeClassifier()
d_tree.fit(X_train, y_train)

predictions = d_tree.predict(X_test)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))


# Tree Visualization

from IPython.display import Image  
from sklearn.externals.six import StringIO  
from sklearn.tree import export_graphviz
import pydot 

features = list(df.columns[1:])

dot_data = StringIO()  
export_graphviz(d_tree, out_file=dot_data,feature_names=features,filled=True,rounded=True)

graph = pydot.graph_from_dot_data(dot_data.getvalue())  
Image(graph[0].create_png())  

# Random forests

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=100) # set the number of trees to use in the random forest
rfc.fit(X_train, y_train)

rfc_pred = rfc.predict(X_test)
print(confusion_matrix(y_test,rfc_pred))
print(classification_report(y_test,rfc_pred))
