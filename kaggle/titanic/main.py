import pandas as pd
from sklearn.linear_model import LogisticRegression
import sys
sys.path.append('./')
train = pd.read_csv('train.csv')

train.head()
train.plot.scatter('', y)
