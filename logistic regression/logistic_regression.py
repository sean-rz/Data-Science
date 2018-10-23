# https://www.geeksforgeeks.org/confusion-matrix-machine-learning/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

mpl.rcParams['patch.force_edgecolor'] = True # gridlines between bins
sns.set_style('whitegrid')

train = pd.read_csv('titanic_train.csv')
print(train.head())

# missing data
sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis')

sns.countplot(x='Survived', hue='Sex', data=train, palette='RdBu_r')
sns.countplot(x='Survived', hue='Pclass', data=train, palette='rainbow')

sns.distplot(train['Age'].dropna(), kde=False, color='darkred', bins=30) # Age has 20% missing values
train['Age'].hist(bins=30, color='darkred', alpha=0.7) # using pandas plotting

sns.countplot(x='SibSp',data=train)

train['Fare'].hist(color='green', bins=40, figsize=(8,4))

# Data Cleaning
# we use the average age of each Pclass to impute (fill in missing values) the Age

plt.figure(figsize=(12,7))
sns.boxplot(x='Pclass', y='Age', data=train, palette='winter')

def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):

        if Pclass == 1:
            return 37
        elif Pclass == 2:
            return 29
        else:
            return 24
    else:
        return Age

train['Age'] = train[['Age','Pclass']].apply(impute_age,axis=1)

sns.heatmap(train.isnull(), yticklabels=False,cbar=False,cmap='viridis')
#plt.show()

train.drop('Cabin', axis=1, inplace=True) # drop Cabin column
train.dropna(inplace=True) # drop missing Embarked rows

# convert categorical features to dummy variables 

sex = pd.get_dummies(train['Sex'], drop_first=True)
embark = pd.get_dummies(train['Embarked'], drop_first=True)

train.drop(['Sex','Embarked','Name','Ticket', 'PassengerId'], axis=1, inplace=True)

train = pd.concat([train, sex, embark], axis=1)

print(train.head())


# train test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(train.drop('Survived',axis=1), train['Survived'], 
                                                    test_size=0.30, random_state=101)

# Training and Predicting
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)

# evaluation: precision,recall,f1-score

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test,predictions))
print(confusion_matrix(y_test,predictions))

