# 🍷 Wine Quality -- Exploratory Data Analysis (EDA)

This project presents a comprehensive **Exploratory Data Analysis
(EDA)** on the **WineQT** dataset.\
The goal is to explore the chemical properties of wine samples, analyze
their distribution, and understand how these features relate to the wine
**quality score**.

## 📁 Project Structure

    ├── data/
    │   └── WineQT.csv
    ├── visuals/
    │   ├── correlation_heatmap.png
    │   ├── quality_countplot.png
    │   ├── alcohol_distribution.png
    │   └── quality_pie.png
    ├── src/
    │   └── eda.py
    ├── README.md
    └── requirements.txt

## 🎯 Project Objective

The primary objectives of this EDA are:

-   To understand the structure and characteristics of the dataset\
-   To examine missing values, data types, and statistical
    distributions\
-   To analyze correlations between features\
-   To visualize the distribution of wine quality scores\
-   To identify which chemical properties most strongly influence wine
    quality

This analysis also serves as a foundation for future **machine learning
modeling**.

## 🧰 Used Libraries

    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

## 📊 Dataset Overview

The WineQT dataset includes **chemical measurements** of wine samples
along with a quality rating (from 3 to 8).

Key features:

  Feature                Description
  ---------------------- --------------------------------------
  fixed acidity          Fixed acids
  volatile acidity       Volatile acids
  citric acid            Citric acid
  residual sugar         Residual sugar
  chlorides              Chlorides
  free sulfur dioxide    Free SO₂
  total sulfur dioxide   Total SO₂
  density                Density
  pH                     Acidity level
  sulphates              Sulphates
  alcohol                Alcohol percentage
  **quality**            Wine quality score (target variable)

Dataset properties:

-   1143 samples\
-   12 input features\
-   **No missing values**\
-   Quality scores range from **3 to 8**

# 🔍 Analysis Steps

## 1️⃣ Data Loading & Initial Exploration

Performed analyses include:

-   Viewing first rows (`head()`)
-   Generating statistical summaries (`describe()`)
-   Inspecting data types and memory usage (`info()`)
-   Checking missing values (`isnull().sum()`)

Result:\
**The dataset contains no missing values.**

## 2️⃣ Correlation Analysis

📌 **Alcohol has the strongest positive correlation with wine quality.**

(Insert: correlation heatmap image)

## 3️⃣ Wine Quality Distribution

Most wines are scored **5** or **6**, showing an imbalanced dataset.

(Insert: countplot image)

## 4️⃣ Alcohol Percentage Distribution

The alcohol distribution is **right-skewed**.

(Insert: KDE distribution image)

## 5️⃣ Quality Pie Chart

Shows percentage distribution of each quality class.

(Insert: pie chart image)

# 📈 Key Findings & Insights

-   The dataset is clean --- no missing values\
-   **Alcohol** has the strongest correlation with wine quality\
-   Quality values are imbalanced\
-   Alcohol distribution is skewed\
-   Low multicollinearity\
-   Alcohol is the dominant factor influencing wine quality

