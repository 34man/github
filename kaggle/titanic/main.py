import pandas as pd
from sklearn.linear_model import LogisticRegression
import sys
import numpy as np
sys.path.append('.')

train = pd.read_csv('kaggle/titanic/train.csv')
test = pd.read_csv('kaggle/titanic/test.csv')
print(train.columns)
print(train.dtypes)
def pre_deal(train):
    train.fillna(0, inplace=True)
    train['Sex'].replace('male', 0, inplace=True)
    train['Sex'].replace('female', 1, inplace=True)
    x_train = train[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']]
    return x_train
x_test = pre_deal(test)
logistic = LogisticRegression()
logistic.fit(x_train, y_train)
res = logistic.predict(x_test)
test['result'] = res
res = test[['PassengerId', 'result']]
res.rename(columns={'result': "Survived"}, inplace=True)

res.to_csv('kaggle/titanic/submission.csv', index=False)
