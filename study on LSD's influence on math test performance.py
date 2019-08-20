#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt
data = pd.read_csv('lsd_math_score_data.csv')


# In[30]:


print(data)


# In[31]:


onlyMathScores = data['Avg_Math_Test_Score']


# In[32]:


print(onlyMathScores)


# In[33]:


data['High_Score'] = '100'
print(data)


# Challenge: overwrite values in rows for high_score to equal average score + 100

# Challenge: Square the values stored inside High_Score

# In[34]:


print(data)


# In[35]:


# or data['High_Score'] = data['High_Score'] ** 2
# ** means raise to exp


# In[36]:


print(data)


# In[37]:


type(onlyMathScores)


# Series: One column(single dimension), may have an attribute/name/column heading

# Chanllenge: Create a list called columnList. put 'LSD_ppm' and 'Avg_Math_Test_Score' inside.

# In[38]:


columnList = ['LSD_ppm', 'Avg_Math_Test_Score']


# In[39]:


print(columnList)


# In[40]:


cleanData = data[columnList]
print(cleanData)


# In[41]:


type(cleanData)


# In[42]:


y = data[['Avg_Math_Test_Score']]


# if we provide list to datafram we get dataframe
# but if we provide str to dataframe we get series

# In[43]:


type(y)


# In[44]:


y = data['Avg_Math_Test_Score']


# In[45]:


type(y)


# #challenge:
# 1. creat variable X
# 2. set x equal to the values of LSD_ppm
# 3. makesure x is dataframe
# 4. print the value of x
# 5. show the type of x

# In[46]:


X = data[['LSD_ppm']]


# In[47]:


type(X)


# In[48]:


print(X)


# In[51]:


del data['High_Score']


# In[52]:


print(data)


# In[56]:


import pandas


# In[59]:


import math


# from keyword copies the variable into current notebook, no need for dot. notation

# In[60]:


import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# In[61]:


data


# In[62]:


time = data[['Time_Delay_in_Minutes']]
LSD = data[['LSD_ppm']]
Score = data[['Avg_Math_Test_Score']]


# In[63]:


get_ipython().run_line_magic('matplotlib', 'inline')

plt.title('Tissue Concentration of LSD over time', fontsize = 17)
plt.xlabel('Time in Minutes', fontsize = 14)
plt.ylabel('LSD Concentration', fontsize = 14)
plt.text(x = 0, y = -0.5, s = 'Wagner et al. (1968)', fontsize = 12)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)

plt.ylim(1, 7)
plt.xlim(0, 500)

plt.style.use('classic')
plt.plot(time, LSD, color = '#ee5253', lw = 3)
plt.show()


# In[64]:


regr = LinearRegression()
regr.fit(LSD, Score)
print('theta1 : ', regr.coef_[0][0])
print('Intercept: ', regr.intercept_[0])
print('r-square: ', regr.score(LSD, Score))

predicted_score = regr.predict(LSD)


# In[65]:


get_ipython().run_line_magic('matplotlib', 'inline')

plt.title('Arithmetic vs LSD-25', fontsize = 17)
plt.xlabel('Tissue LSD ppm', fontsize = 14)
plt.ylabel('Performance Score', fontsize = 14)
plt.ylim(25, 85)
plt.xlim(1, 6.5)
plt.style.use('fivethirtyeight')
plt.plot(LSD, predicted_score, c = 'r', lw = 2)

plt.scatter(LSD, Score, c = 'b', s = 155, alpha = 0.7)
plt.show()

