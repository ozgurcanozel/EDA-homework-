import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from numpy.ma.extras import column_stack

data = pd.read_csv("WineQT.csv")


# print(data.head())
# print(data.describe())
print(data.info())
print(data.shape)
# print(data.isnull().sum())
print(data[data.duplicated()])

# # correlation
# plt.figure(figsize = (10,6))
# sns.heatmap(data.corr(numeric_only=True), annot = True) # Which feature affects quality the most? = alcohol
# plt.show()

print(data.groupby("quality").mean())
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

#### EXTRA ####

# sns.pairplot(data) # heatmap to plot
# plt.show()

# sns.boxplot(x = "quality", y="alcohol",data = data)
# plt.show()
#
# sns.scatterplot(x = "pH", y = "alcohol",hue = "quality", data = data)
# plt.show()
#
# sns.scatterplot(x = "fixed acidity", y = "density",hue = "quality", data = data)
# plt.show()

print(data.head())

## distrubution of all columns

columns= data.columns
(fig,ax) = plt.subplots(4,4, figsize=(16,15),layout = 'constrained') # layout kismi grafikleri boyutlarini ayarliyor
ax = ax.flatten()

for i, columns in enumerate(columns):
    sns.kdeplot(
        data=data,
        x=columns,
        hue=data.quality,
        ax = ax[i]
    )
    ax[i].set_title(f"{columns} Distribution")
    ax[i].set_xlabel(None)

plt.show()

for i in range (i+1, len(ax)):
    ax[i].axis("off")



