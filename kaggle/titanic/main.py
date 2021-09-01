import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import accuracy_score

import sys
import numpy as np
sys.path.append('.')

train = pd.read_csv('kaggle/titanic/train.csv')
test = pd.read_csv('kaggle/titanic/test.csv')
print(train.columns)
train.head(5)

pd.unique(train['Embarked'])
def pre_deal(train):
    train['Age'].fillna(train['Age'].mean(), inplace=True)
    train['Sex'].replace('male', 0, inplace=True)
    train['Sex'].replace('female', 1, inplace=True)
    train['Embarked'] = train['Embarked'].fillna("N")
    train.loc[train['Embarked']=='S', "Embarked"] = 0
    train.loc[train['Embarked']=='Q', "Embarked"] = 1
    train.loc[train['Embarked']=='C', "Embarked"] = 2
    train.loc[train['Embarked']=='N', "Embarked"] = 3
    train['Fare'].fillna(train['Fare'].mean(), inplace=True)
    x_train = train[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
    return x_train
dataset = pre_deal(train)
dataset.isnull().any()
dataset['y'] = train['Survived']
train.columns
dataset.columns
dataset.describe()

logistic = LogisticRegression()

kf = KFold(n_splits=3, random_state=1, shuffle=True)
dataset.shape
for train, test in kf.split(dataset):
    x_train = dataset.iloc[train]
    x_test = dataset.iloc[test]
    y_train = x_train.pop('y')
    y_test = x_test.pop('y')
    logistic.fit(x_train, y_train)
    res = logistic.predict(x_test)
    print(accuracy_score(res, y_test))

test['result'] = res
res = test[['PassengerId', 'result']]
res.rename(columns={'result': "Survived"}, inplace=True)

res.to_csv('kaggle/titanic/submission.csv', index=False)
