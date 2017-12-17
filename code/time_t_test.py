
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd
import math
from scipy.stats import ttest_ind


# In[4]:

cd /Users/fumengjin/Documents/DATAMIN/


# In[5]:

norm=pd.read_excel("./step3/Norm_F_num.xls")
st=pd.read_excel("./step3/st_F_num.xlsx")


# In[6]:

normF01201401=norm[norm.feature_num==1]["y_2014_1"]


# In[7]:

lnormF01201401=[i for i in normF01201401 if (math.isnan(i) == False)]


# In[8]:

stF01201401=st[st.feature_num==1]["y_2014_1"]
lstF01201401=[i for i in stF01201401 if (math.isnan(i) == False)]


# In[9]:

result=[]


# In[10]:

result.append(ttest_ind(lnormF01201401,lstF01201401).pvalue)


# In[53]:

sum_f=[]


# In[54]:

result=[]
sum0=0
for i in range(1,32):
    tn=norm[norm.feature_num==i]["y_2014_1"]
    ln=[j for j in tn if (math.isnan(j)==False)]
    tst=st[st.feature_num==i]["y_2014_1"]
    lst=[j for j in tst if (math.isnan(j)==False)]
    result.append(ttest_ind(ln,lst).pvalue)
    if (ttest_ind(ln,lst).pvalue<0.05):
        sum0=sum0+1
sum_f.append(sum0)


# In[55]:

result=[]
sum1=0
for i in range(1,32):
    tn=norm[norm.feature_num==i]["y_2014_2"]
    ln=[j for j in tn if (math.isnan(j)==False)]
    tst=st[st.feature_num==i]["y_2014_2"]
    lst=[j for j in tst if (math.isnan(j)==False)]
    result.append(ttest_ind(ln,lst).pvalue)
    if ttest_ind(ln,lst).pvalue<0.05:
        sum1=sum1+1
sum_f.append(sum1)


# In[56]:

result=[]
sum2=0
for i in range(1,32):
    tn=norm[norm.feature_num==i]["y_2014_3"]
    ln=[j for j in tn if (math.isnan(j)==False)]
    tst=st[st.feature_num==i]["y_2014_3"]
    lst=[j for j in tst if (math.isnan(j)==False)]
    result.append(ttest_ind(ln,lst).pvalue)
    if (ttest_ind(ln,lst).pvalue<0.05):
        sum2=sum2+1
sum_f.append(sum2)


# In[57]:

result=[]
sum3=0
for i in range(1,32):
    tn=norm[norm.feature_num==i]["y_2014_4"]
    ln=[j for j in tn if (math.isnan(j)==False)]
    tst=st[st.feature_num==i]["y_2014_4"]
    lst=[j for j in tst if (math.isnan(j)==False)]
    result.append(ttest_ind(ln,lst).pvalue)
    if (ttest_ind(ln,lst).pvalue<0.05):
        sum3=sum3+1
sum_f.append(sum3)


# In[58]:

result=[]
sum4=0
for i in range(1,32):
    tn=norm[norm.feature_num==i]["y_2015_1"]
    ln=[j for j in tn if (math.isnan(j)==False)]
    tst=st[st.feature_num==i]["y_2015_1"]
    lst=[j for j in tst if (math.isnan(j)==False)]
    result.append(ttest_ind(ln,lst).pvalue)
    if (ttest_ind(ln,lst).pvalue<0.05):
        sum4=sum4+1
sum_f.append(sum4)


# In[59]:

result=[]
sum5=0
for i in range(1,32):
    tn=norm[norm.feature_num==i]["y_2014_2"]
    ln=[j for j in tn if (math.isnan(j)==False)]
    tst=st[st.feature_num==i]["y_2015_2"]
    lst=[j for j in tst if (math.isnan(j)==False)]
    result.append(ttest_ind(ln,lst).pvalue)
    if (ttest_ind(ln,lst).pvalue<0.05):
        sum5=sum5+1

sum_f.append(sum5)


# In[60]:

result=[]
sum6=0
for i in range(1,32):
    tn=norm[norm.feature_num==i]["y_2015_3"]
    ln=[j for j in tn if (math.isnan(j)==False)]
    tst=st[st.feature_num==i]["y_2015_3"]
    lst=[j for j in tst if (math.isnan(j)==False)]
    result.append(ttest_ind(ln,lst).pvalue)
    if (ttest_ind(ln,lst).pvalue<0.05):
        sum6=sum6+1

sum_f.append(sum6)


# In[61]:

result=[]
sum7=0
for i in range(1,32):
    tn=norm[norm.feature_num==i]["y_2015_4"]
    ln=[j for j in tn if (math.isnan(j)==False)]
    tst=st[st.feature_num==i]["y_2015_4"]
    lst=[j for j in tst if (math.isnan(j)==False)]
    result.append(ttest_ind(ln,lst).pvalue)
    if (ttest_ind(ln,lst).pvalue<0.05):
        sum7=sum7+1
sum_f.append(sum7)


# In[62]:

print(sum_f)


# In[82]:

d={}
d["y_2014_1"]=result
d["y_2014_2"]=result1
d["y_2014_3"]=result2
d["y_2014_4"]=result3
d["y_2015_1"]=result4
d["y_2015_2"]=result5
d["y_2015_3"]=result6
d["y_2015_4"]=result7


# In[83]:

df=pd.DataFrame(d)


# In[84]:

df.to_excel("./ttest_result.xlsx")


# In[ ]:



