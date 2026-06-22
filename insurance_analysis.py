# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
df=pd.read_csv(r"C:\Users\HP\Downloads\insurance.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.groupby("smoker")["charges"].mean())
print(df.groupby("region")["charges"].mean())
print(df.groupby("sex")["charges"].mean())
print(df.loc[df["charges"].idxmin()])
print(df[df["smoker"]=="yes"]["bmi"].mean())
print(df["smoker"].value_counts())
print(df.groupby("children")["charges"].mean())

import matplotlib.pyplot as plt
df["smoker"].value_counts().plot(kind="hist")
plt.show()
df["age"].plot(kind="hist")
plt.show()



df.plot(x="bmi",y="charges", kind="scatter")
plt.show()
df.groupby("sex")["charges"].mean().plot(kind="bar")
plt.show()
df["age"].plot(kind="hist")
plt.show()
df.groupby("region")["charges"].mean().plot(kind="bar")
plt.show()
df.groupby(["region","smoker"])["bmi"].mean().plot(kind="bar")
plt.show()

df.groupby("region")["age"].mean().plot(kind="bar")
plt.show()
print(df.groupby("region")["charges"].mean().idxmax())

print(df.loc[df["charges"].idxmax()])

