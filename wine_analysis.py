import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("WineQT.csv")

print(data.head())
print(data.describe())
print(data.info())
print(data.isnull().sum())

# # correlation
# plt.figure(figsize = (8,8))
# sns.heatmap(data.corr(numeric_only=True), annot = True) # Which feature affects quality the most? = alcohol
# plt.show()
#
# # How do you list how many different score types there are in the quality column (e.g. 3, 4, 5, 6...) and how many wines there are with each score?
# print(data.columns)
# print(data['quality'].unique())
#
# # Can you draw a histogram to see the distribution of quality scores for the wines? (Is the data balanced or clustered at specific scores?)
# sns.countplot(x='quality', data=data)
# plt.title("Count of quality")
# plt.xlabel("Quality")
# plt.ylabel("Count")
# plt.show()
#
# # Can you draw the distribution of alcohol percentages and add the density curve to it?
#
# sns.displot(x="alcohol", data=data, kind = "kde")
# plt.xlabel("Alcohol")
# plt.show()
#
# data["quality"].value_counts().plot(kind="pie")
# plt.show()
#
# sns.boxplot( x="free sulfur dioxide", y="quality", data=data)
# plt.show()

column = data.columns
(fig, ax) = plt.subplots(4,4, figsize = (25,25))
ax = ax.flatten()

for i,column in enumerate(column):
    sns.kdeplot(
        data= data,
        x = column,
        hue= data.quality,
        ax= ax[i]

    )
    ax[i].set_title(f"{column} Distrubution")
    ax[i].set_xlabel(None)



for i in range(i+1, len(ax)):
    ax[i].axis("off")
plt.show()