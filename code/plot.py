
# coding: utf-8

# In[1]:

cd /Users/fumengjin/Documents/DATAMIN/train/


# In[2]:

import numpy as np
import pandas as pd
PREVIOUS_MAX_ROWS = pd.options.display.max_rows
pd.options.display.max_rows = 20
np.random.seed(12345)
import matplotlib.pyplot as plt
import matplotlib
plt.rc('figure', figsize=(30, 10))
np.set_printoptions(precision=4, suppress=True)


# In[12]:

norm=pd.read_excel("./tnorm.xlsx")
st=pd.read_excel("./tst.xlsx")
norm = norm.apply(lambda x: (x-x.mean())/x.std())

st = st.apply(lambda x: (x-x.mean())/x.std())


# In[17]:

st[1].plot.bar()
plt.show()


# In[18]:

norm[1].plot.bar()
plt.show()


# In[ ]:



