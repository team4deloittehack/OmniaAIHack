# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 14:57:03 2019

@author: Krishna Chaitanya Gopaluni
"""


import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt




data = pd.read_csv("completion_rate_199798-201718.csv")

data = data[data['DISTRICT_NUMBER'].isin([92.0, 48.0])]

data = data[data['YEAR_6_OF_COHORT'].isin(['2013/2014', '2014/2015', '2015/2016', '2016/2017', '2017/2018'])]



#sns.set(style="whitegrid")

data = data[data["ESTIMATED_COMPLETION_RATE"] != 'MSK']

data[["ESTIMATED_COMPLETION_RATE"]] = data[["ESTIMATED_COMPLETION_RATE"]].apply(pd.to_numeric)
data[["DISTRICT_NUMBER"]] = data[["DISTRICT_NUMBER"]].astype(int)
plt.figure(figsize=(20,10))
ax = sns.lineplot(x="YEAR_6_OF_COHORT", y="ESTIMATED_COMPLETION_RATE", data=data, style = "DISTRICT_NUMBER", linewidth = 2.5)

#plt.plot("YEAR_6_OF_COHORT", "ESTIMATED_COMPLETION_RATE", data =data )

plt.title("Rate of Completion by district for the past 6 years")

