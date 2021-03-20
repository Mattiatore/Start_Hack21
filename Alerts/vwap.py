# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import GradientBoostingClassifier

#German market Vwap data extracted from Volue
one_hour= pd.read_csv("C:/Users/Mattia/Desktop/Start_Hack21/dataset/Intraday/De/143289.csv", names= ["Time", "Vwap_1"], skiprows=1)
three_hour= pd.read_csv("C:/Users/Mattia/Desktop/Start_Hack21/dataset/Intraday/De/143325.csv", names= ["Time", "Vwap_3"], skiprows=1)

df = pd.merge(one_hour, three_hour, on='Time')

"""Baseline model to predict if price will increase in the next hour. 
Simply compares the 1 hour vwap with the 3 hour vwap, 
if it's lower we predict that the price will increase in the next our.
"""

#True implies Increasing Price while False implies decreasing price
df["Prediction"]=(df.Vwap_1<df.Vwap_3).values

temp=df.Vwap_1[1:]

df.drop(df.tail(1).index,inplace=True)
df["Occurence"]=(df.Vwap_1.values<temp).values

df.fillna(df.mean(), inplace=True)

# Confusion Matrix for baseline, 0th row decreasing prediction 1th row increasing prediction
# 0th column observed decreased price, 1th column observed increased price
print(confusion_matrix(df.Occurence, df.Prediction, normalize="true"))

# accuracy of baseline
print(accuracy_score(df.Occurence, df.Prediction))

#XGboost model

y = df.Occurence
X = df.drop(columns=["Time", "Prediction", "Occurence"])

clf = GradientBoostingClassifier(n_estimators=150, learning_rate=0.95, max_depth=2, random_state=42).fit(X, y)

clf.fit(X, y)

# Confusion Matrix for XGboost
print(confusion_matrix(y, clf.predict(X) , normalize="true"))

# accuracy of XGboost
print(accuracy_score(y, clf.predict(X)))

# new data
# clf.predict_proba(X)


