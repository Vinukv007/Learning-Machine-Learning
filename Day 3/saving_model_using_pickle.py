# -*- coding: utf-8 -*-
"""ML yt vid 5 pickle save model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11f5zrmQAVulIJTYOQ0346AcHVZ6qdJ6O
"""

import pandas as pd
import numpy as np
from sklearn import linear_model


# opening filre and fitting them using linear regression
df=pd.read_csv('homeprices.csv')
df.head()

lreg=linear_model.LinearRegression()

lreg.fit(df[['area']],df.price)

lreg.predict([[6000]])

lreg.coef_

# installing and loading pickle 
pip install pickle

import pickle

#writing and reading as binary as pickle saves the model as binary.
with open('lreg_pickle','wb') as f:
  pickle.dump(lreg,f)

# loading the pickle file and loading the model to linreg.
with open ('lreg_pickle','rb') as f:
  linreg=pickle.load(f)

linreg.predict([[6000]])


# Another way to save and use model. much more prefered and used.

from sklearn.externals import joblib

import sklearn.externals.joblib as exjb

import joblib

with open('lreg_job','wb') as f:
  joblib.dump(lreg,f)

with open('lreg_job','rb') as f:
  linregjb=joblib.load(f)

linregjb

linregjb.predict([[6000]])


# or
#Ease of loading a model.

linregjb2=joblib.load('lreg_job')
linregjb2

linregjb2.predict([[6000]])
