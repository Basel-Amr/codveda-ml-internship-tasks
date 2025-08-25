# 📊 Exploratory Data Analysis (EDA) Report

This report summarizes the **exploratory data analysis** performed on the datasets used in the Codveda Technologies internship.  
The goal is to understand data quality, patterns, correlations, and distributions before applying machine learning models.  

---

## 🔹 1. House Prices Dataset (`house_prices.csv`)
- **Shape:** (rows = XXX, columns = XX)  
- **Missing Values:**  
  - `LotArea`: 3 missing  
  - `GarageType`: 25 missing  
- **Key Insights:**  
  - House price distribution is **right-skewed**.  
  - Larger house area strongly correlates with higher price.  
  - Location features are highly influential.  

📊 *Visuals:* Histogram of house prices, correlation heatmap of numerical features.  

---

## 🔹 2. Sentiment Dataset (`sentiment.csv`)
- **Shape:** (rows = XXX, columns = XX)  
- **Classes:** Positive (XX%), Negative (XX%)  
- **Key Insights:**  
  - Dataset is slightly imbalanced towards **positive reviews**.  
  - Common positive words: *good, great, excellent*.  
  - Common negative words: *bad, poor, terrible*.  

📊 *Visuals:* Word clouds for positive & negative reviews, class distribution bar chart.  

---

## 🔹 3. Customer Churn Dataset (`churn-bigml-20.csv`, `churn-bigml-80.csv`)
- **Shape:** (rows = XXX, columns = XX)  
- **Missing Values:** Few in `TotalCharges` column.  
- **Key Insights:**  
  - Customers with **month-to-month contracts** churn more.  
  - Higher monthly charges increase churn probability.  
  - Tenure has an inverse relationship with churn.  

📊 *Visuals:* Pie chart of churn vs. no churn, boxplots of monthly charges by churn status.  

---

## 🔹 4. Iris Dataset (`iris.csv`)
- **Shape:** (150 rows, 5 columns)  
- **Classes:** Setosa, Versicolor, Virginica (balanced)  
- **Key Insights:**  
  - Petal length and width clearly separate Setosa from other species.  
  - Versicolor and Virginica overlap slightly in measurements.  

📊 *Visuals:* Pairplot (seaborn), scatter plot of petal length vs. petal width.  

---

## 🔹 5. Stock Prices Dataset (`stock_prices.csv`)
- **Shape:** (rows = XXX, columns = XX)  
- **Key Insights:**  
  - Stock prices show **seasonal trends**.  
  - Some stocks are highly correlated (same sector).  
  - High volatility detected in tech-related stocks.  

📊 *Visuals:* Line plots of stock price trends, rolling averages, correlation heatmap.  

---

## 🏆 General Observations
- All datasets required **missing value treatment**.  
- Encoding categorical variables was essential for ML models.  
- Normalization/standardization improved model stability.  
- EDA revealed strong correlations and patterns that guided **feature selection** and **model choice**.  

---
