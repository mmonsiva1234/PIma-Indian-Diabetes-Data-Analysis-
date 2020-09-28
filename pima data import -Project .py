#!/usr/bin/env python
# coding: utf-8

# # Directory

# In[7]:


get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('cd', 'Desktop')
get_ipython().run_line_magic('pwd', '')


# # Library

# In[8]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# # Reading and Cleaning

# In[9]:


pima = pd.read_csv("diabetes.csv")


# In[10]:


pima.head()


# In[50]:


pima.shape


# In[51]:


pima["Outcome"]= pd.Categorical(pima["Outcome"]) 


# In[52]:


pima.dtypes


# In[53]:


pima.describe()


# # Analysis

# In[54]:


# How does glucose affect insulin levels?
c = pima[["Glucose","Insulin"]]

corrmat = c.corr() 
corrmat


# In[55]:


#How does skin thickness affect insulin level?

t = pima[["SkinThickness","Insulin"]]
 
t.head()
cor_t = t.corr()
cor_t


# In[56]:


# What is the average number of pregnancies for people with diabetes?

g = pima[["Outcome", "Pregnancies"]]
g = g[g["Outcome"]==1]
g["Pregnancies"].mean()


# In[57]:



#What is the average pregnancies with people without diabetes?
without_diabetes = pima[["Outcome", "Pregnancies"]]
without_diabetes = without_diabetes[without_diabetes["Outcome"]==0]
without_diabetes["Pregnancies"].mean()


# In[58]:


#How does glucose levels affect blood pressure with the outcome of diabetes 

g = pima[["Glucose","BloodPressure", "Outcome"]]
g = g[g["Outcome"]==1]
cor_g = g.corr()
cor_g


# In[59]:


#What is the average glucose level for people with diabetes?
avg_glucose = pima[["Glucose", "Outcome"]]
avg_glucose = avg_glucose[avg_glucose["Outcome"] == 1]
avg_glucose["Glucose"].mean()


# In[60]:


#What is the average glucose level for people without diabetes?
avg_wodiabetes = pima[["Glucose","Outcome"]]
avg_wodiabetes = avg_wodiabetes[avg_wodiabetes["Outcome"] == 0]
avg_wodiabetes["Glucose"].mean()


# In[61]:


#What is the average BMI for people with diabetes?
avg_bmi = pima[["BMI","Outcome"]]
avg_bmi = avg_bmi[avg_bmi["Outcome"] == 1]
avg_bmi["BMI"].mean()


# In[62]:


#What is the average BMI for people without diabetes?
avg_wobmi = pima[["BMI","Outcome"]]
avg_wobmi = avg_wobmi[avg_wobmi["Outcome"] == 0]
avg_wobmi["BMI"].mean()


# In[63]:


age_count = pd.DataFrame(pima.groupby('Age').size())
age_count.reset_index(inplace= True)
age_count.columns =["Age", "Count"] 
age_count


# In[64]:



#What age group is more likely to get prone to having diabetes? 
# youre going to have to make categories from age group of 10 years old.

average = pd.DataFrame(pima.groupby("Age").mean())
average.reset_index(inplace = True)
average


# In[65]:


#How does BMI affect age or does age affect BMI? 
#can talk about the metabolism system?

ab = pima[["Age","BMI"]]
cor_ab = ab.corr()
cor_ab


# In[66]:


# Diabetes by Age

diab_age = pima[["Age", "Outcome"]]
diab_age[diab_age["Outcome"] == 1]
diab_age = diab_age.groupby("Age").agg(sum)
diab_age = pd.DataFrame(diab_age).reset_index()
diab_age.columns = ["Age", "DiabetesCount"]
diab_age


# In[67]:


# Correlation Plot

corr = pima.corr()
plt.figure(figsize=(10, 10))
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, annot=True).set_title("Pima Correlations", fontsize=30)


# In[68]:


# Histogram 

sns.distplot(pima["BMI"], kde=True)


# In[69]:


sns.pairplot(pima)


# In[70]:


outcome_pima = pima[["Outcome", ]]
outcome_pima = outcome_pima.groupby("Outcome").agg("count")
outcome_pima


# In[71]:


# People that have and don't have diabetes
labels = 'With Diabetes', 'Without Diabetes'
sizes = [69.54, 30.46]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)


plt.show()


# In[73]:


sns.regplot(x = 'Age',y ='DiabetesCount',data= diab_age)


# In[74]:


sns.boxplot(x = "Outcome", y = "Insulin", data = pima)


# In[75]:


diab_blood = pima[["BloodPressure","Outcome"]]
diab_blood[diab_blood["Outcome"] == 1]
diab_blood = diab_blood.groupby("BloodPressure").agg(sum)
diab_blood = pd.DataFrame(diab_blood).reset_index()
diab_blood.columns = ["BloodPressure", "DiabetesCount"]
diab_blood


# In[76]:


sns.boxplot(x ="Pregnancies", y = "Insulin", hue = "Outcome", data = pima)


# In[77]:


sns.boxplot(x ="Age", y = "BloodPressure", hue = "Outcome", data = pima)


# In[78]:


sns.regplot(x = 'BloodPressure',y ='DiabetesCount',data=diab_blood)


# In[79]:


sns.boxplot(x ="Pregnancies", y = "Age", hue = "Outcome", data = pima)


# In[80]:


#Diabetes by Pregnancies 
diab_preg = pima[["Pregnancies", "Outcome"]]
diab_preg[diab_preg["Outcome"] == 1]


# In[82]:


#pregnacies for data with no diabetes 
nodiab_preg = pima[["Pregnancies", "Outcome"]]
nodiab_preg[nodiab_preg["Outcome"] == 0]

# tried to get data from non diabetic population 


# In[83]:


#BMI for data with diabetes 
diab_bmi = pima[["BMI", "Outcome"]]
diab_bmi.reset_index(inplace = True)
diab_bmi = diab_bmi[["BMI","Outcome"]]
diab_bmi


# In[85]:


avg_bmi = pima[["BMI","Outcome"]]
avg_bmi = avg_bmi[avg_bmi["Outcome"] == 0]
avg_bmi["BMI"].mean()


# In[87]:


preg = pima[["Pregnancies", "Outcome"]]
preg[preg["Outcome"] == 0]
preg.sum()


# In[88]:


total = pima["Pregnancies"].sum()
print (total)


# In[89]:


avg_bmi2 = pima[["BMI","Outcome"]]
avg_bmi2 = avg_bmi2[avg_bmi2["Outcome"] == 1]
avg_bmi2["BMI"].mean()

