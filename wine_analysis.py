import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("WineQT.csv")

print(data.head())
print(data.describe())
print(data.info())
print(data.isnull().sum())
