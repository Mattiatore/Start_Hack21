# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:38:59 2021

@author: Mattia
"""


import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import GradientBoostingClassifier

#German market
one_hour= pd.read_csv("C:/Users/Mattia/Desktop/Start_Hack21/dataset/Intraday/De/143289.csv", names= ["Time", "Vwap_1"], skiprows=1)
three_hour= pd.read_csv("C:/Users/Mattia/Desktop/Start_Hack21/dataset/Intraday/De/143325.csv", names= ["Time", "Vwap_3"], skiprows=1)


"""France market
one_hour= pd.read_csv("C:/Users/Mattia/Desktop/Start_Hack21/dataset/Intraday/FR/143297.csv", names= ["Time", "Vwap_1"], skiprows=1)
three_hour= pd.read_csv("C:/Users/Mattia/Desktop/Start_Hack21/dataset/Intraday/FR/143333.csv", names= ["Time", "Vwap_3"], skiprows=1)
"""

df = pd.merge(one_hour, three_hour, on='Time')

#Naive comparison as baseline

# compare vwap 1 hour with vwap 3 hours to predict if increasing or decreases in the next hour

#True implies increasing in both Prediction and Occurence
df["Prediction"]=(df.Vwap_1<df.Vwap_3).values

temp=df.Vwap_1[1:]
#print(temp)

df.drop(df.tail(1).index,inplace=True)
df["Occurence"]=(df.Vwap_1.values<temp).values

df.fillna(df.mean(), inplace=True)

print(confusion_matrix(df.Occurence, df.Prediction, normalize="true"))

#Random forest

y = df.Occurence
X = df.drop(columns=["Time", "Prediction", "Occurence"])

clf = GradientBoostingClassifier(n_estimators=75, learning_rate=1.0, max_depth=1, random_state=42).fit(X, y)

clf.fit(X, y)

print(confusion_matrix(y, clf.predict(X) , normalize="true"))

