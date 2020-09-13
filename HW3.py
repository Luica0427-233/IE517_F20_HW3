# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 00:18:12 2020

@author: Lucia
"""
import pandas as pd
import numpy as np
import pylab
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\Desktop\IE517 ML in Fin Lab\Module3\HW3\HY_Universe_corporate bond.csv")


#QQ plot

df_LIQ_SCORE = df['LIQ SCORE']
stats.probplot(df_LIQ_SCORE, dist="norm", plot=pylab)
plt.title("Quantile‐quantile plot of LIQ SCORE")
plt.show()

#Heat map

#calculate correlations between real-valued attributes
corMat = pd.DataFrame(df.iloc[:,20:29].corr())
#visualize correlations using heatmap
plt.pcolor(corMat)
plt.show()

#Scatter plot

plt.scatter(df['LIQ SCORE'], df['Client_Trade_Percentage'])
plt.xlabel('LIQ SCORE')
plt.ylabel('Client_Trade_Percentage')
plt.show()

#Histogram

sns.set()
plt.hist(df['Industry'])
plt.show()


#Box plot

plt.boxplot(df.iloc[:,30:34].values)
plt.xlabel('Attribute')
plt.ylabel('Quantile Ranges')
plt.title("Box plot")
plt.show()




print("-----------")
print("My name is Lu Yuan")
print("My NetID is: luyuan3")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")