
# coding: utf-8

# In[44]:

cd /Users/fumengjin/Documents/DATAMIN/train


# In[45]:

import numpy as np
import pandas as pd
import types
from libsvm.svmutil import *

norm=pd.read_excel("./tnorm.xlsx")
st=pd.read_excel("./tst.xlsx")
#x的变换
norm = norm.T.apply(lambda x: (x-x.mean())/x.std())
st = st.T.apply(lambda x: (x-x.mean())/x.std())
dn = norm.to_dict()
ln = []
for i in range (0,158):
    ln.append(dn[i])
ds = st.to_dict()
ls = []
for i in range (0,152):
    ls.append(ds[i])
x = ln+ls
#y的变换
positive_labels = [1 for i in range (0,158)]
negative_labels = [0 for i in range (0,152)]
y = positive_labels+negative_labels


# In[50]:

x_train = x[50:260]
y_train = y[50:260]
x_test = x[0:50]+x[260:310]
y_test = y[0:50]+y[260:310]


# In[51]:

prob = svm_problem(y_train, x_train)
param = ('-s 0 -t 2 ')
m = svm_train(y_test, x_test)
p_label, p_acc, p_val = svm_predict(y_test, x_test,m)


# In[ ]:



