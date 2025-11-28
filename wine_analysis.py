import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("WineQT.csv")

print(data.head())
print(data.describe())
print(data.info())
print(data.isnull().sum())

# correlation
plt.figure(figsize = (8,8))
sns.heatmap(data.corr(numeric_only=True), annot = True) # Which feature affects quality the most? = alcohol
plt.show()

# How do you list how many different score types there are in the quality column (e.g. 3, 4, 5, 6...) and how many wines there are with each score?
print(data.columns)
print(data['quality'].unique())