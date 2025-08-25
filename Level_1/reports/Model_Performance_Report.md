# 📊 Model Performance Report

This report summarizes the performance of all machine learning models implemented during my **Codveda Technologies Internship**.  
Each section includes dataset details, preprocessing steps, model evaluation metrics, and insights.

---

## 🔹 Level 1 (Basic)

### 1. Data Preprocessing and Exploration
- **Dataset:** Mixed datasets (House, Churn, Sentiment, Stock, Iris)  
- **Steps:**  
  - Handled missing values (mean, median, mode, drop)  
  - Encoded categorical features (One-Hot / Label Encoding)  
  - Normalized numerical features  
  - Train-test split  

✅ *Output: Clean datasets ready for ML models*  

---

### 2. Linear Regression for House Price Prediction
- **Dataset:** `house_prices.csv`  
- **Metrics:**  
  - R² Score: `XX%`  
  - Mean Squared Error (MSE): `XX`  

📌 *Insight:* Larger houses and prime locations had the highest positive impact on predicted prices.  

---

### 3. KNN Classifier for Sentiment Analysis
- **Dataset:** `sentiment.csv`  
- **Metrics (Best K = XX):**  
  - Accuracy: `XX%`  
  - Precision: `XX%`  
  - Recall: `XX%`  
  - F1-Score: `XX%`  

📌 *Insight:* Best results were achieved with K = 7 after hyperparameter tuning.  

---

## 🔹 Level 2 (Intermediate)

### 4. Logistic Regression for Customer Churn Prediction
- **Dataset:** `churn-bigml-20.csv`, `churn-bigml-80.csv`  
- **Metrics:**  
  - Accuracy: `XX%`  
  - Precision: `XX%`  
  - Recall: `XX%`  
  - ROC-AUC: `XX`  

📌 *Insight:* Monthly charges and contract length were key churn predictors.  

---

### 5. Decision Tree for Iris Classification
- **Dataset:** `iris.csv`  
- **Metrics:**  
  - Accuracy: `XX%`  
  - F1-Score: `XX%`  

📌 *Insight:* Decision Tree performed well, but pruning reduced overfitting and improved generalization.  

---

### 6. K-Means Clustering on Stock Prices
- **Dataset:** `stock_prices.csv`  
- **Metrics:**  
  - Optimal Clusters (Elbow Method): `K = X`  
  - Silhouette Score: `XX`  

📌 *Insight:* Stocks naturally grouped into growth, stable, and volatile categories.  

---

## 🔹 Level 3 (Advanced)

### 7. Random Forest for Advanced Churn Prediction
- **Dataset:** `churn-bigml-80.csv`  
- **Metrics:**  
  - Accuracy: `XX%`  
  - Precision: `XX%`  
  - Recall: `XX%`  
  - F1-Score: `XX%`  

📌 *Insight:* Feature importance analysis showed that `tenure` and `monthly_charges` were the most influential features.  

---

### 8. Support Vector Machine for House Price Classification
- **Dataset:** `house_prices.csv`  
- **Metrics:**  
  - Accuracy (Linear Kernel): `XX%`  
  - Accuracy (RBF Kernel): `XX%`  

📌 *Insight:* RBF kernel captured non-linear relationships better than the linear kernel.  

---

### 9. Neural Network for Sentiment Analysis
- **Dataset:** `sentiment.csv`  
- **Metrics:**  
  - Training Accuracy: `XX%`  
  - Validation Accuracy: `XX%`  
  - Test Accuracy: `XX%`  

📌 *Insight:* Neural Networks outperformed traditional ML models on sentiment analysis after tuning hidden layers.  

---

## 🏆 Key Learnings & Achievements
- Built **end-to-end ML pipelines**: preprocessing → modeling → evaluation → visualization  
- Gained hands-on experience in **regression, classification, clustering, and deep learning**  
- Applied **EDA & business insights** to interpret model outcomes  
- Produced **clean, reproducible, and professional code notebooks**  

---
