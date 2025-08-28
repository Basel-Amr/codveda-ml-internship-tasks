# 🚀 Machine Learning Internship Projects @ Codveda Technologies  

Welcome to my internship project repository! This repo contains all tasks & projects I implemented during my internship at **Codveda Technologies**, covering **data preprocessing, supervised learning, unsupervised learning, and deep learning**.  

The project is structured into **Levels**, with each level containing multiple **Tasks**.  
All work is implemented in **Google Colab / Python** with **impressive visualizations (Plotly Dark Mode), Rich Console tables, and modular functions** to ensure production-ready standards.  

---

## 📂 Folder Structure  
```
Codveda_ML_Internship/
│
├── data/ # Raw & preprocessed datasets
│ ├── Churn Prediction Data/
│ ├── Iris.csv
│ ├── Stock Prices.csv
│ ├── Sentiment.csv
│ └── House Prediction.csv
│
├── Level_1
│ ├── LIris_data_streamlit_app            Streamlit App
│ ├── 01_Data_Preprocessing_and_Exploration.ipynb
|
├── Level_2
│ ├── 02_Intermediate_Level2.ipynb
|
│
├── Level_3
│ ├── 03_Advanced_Level3.ipynb
|
│
├── models/ # Saved models (Pickle / H5)
│ ├── scaler.pkl
│ ├── KNN_best_Iris.pkl
│ ├── RF_Churn.pkl
│ ├── SVM_Model.pkl
│ └── NN_MNIST.h5
│
└── README.md # This file
```

---
## 🎯 Levels & Tasks 

### 🔹 **Level 1 – Foundations**
- **Task 1:** Data Preprocessing (handling missing values, encoding, scaling, splitting).  
- **Task 2:** Linear Regression (House Price Prediction with model comparison).  
- **Task 3:** KNN Classifier (Iris dataset with Optuna hyperparameter tuning).  

### 🔹 **Level 2 – Intermediate ML**
- **Task 1:** Logistic Regression (Churn dataset with ROC curve & odds ratio analysis).  
- **Task 2:** Decision Tree Classifier (Iris dataset with pruning & tree visualization).  
- **Task 3:** K-Means Clustering (Stock dataset with Elbow Method, Silhouette, MiniBatchKMeans).  

### 🔹 **Level 3 – Advanced ML**
- **Task 1:** Random Forest Classifier (Feature importance analysis, hyperparameter tuning).  
- **Task 2:** Support Vector Machines (SVM with Linear & RBF kernels, decision boundary visualization).  
- **Task 3:** Neural Networks (MNIST digit classification using TensorFlow/Keras, misclassified sample visualization).  

---

## 🛠️ Tools & Libraries  

- **Core ML:** scikit-learn, Optuna, TensorFlow/Keras  
- **Visualization:** Plotly (dark template), Seaborn, Matplotlib  
- **UI/Console:** Rich Console, Streamlit  
- **Data Handling:** Pandas, NumPy  
- **Model Persistence:** joblib, pickle, H5  

---

## 📊 Features & Highlights  

✅ Preprocessing Pipelines (scaling, encoding, saving & reusing scalers)  
✅ Model Training & Hyperparameter Tuning (Optuna, GridSearch)  
✅ Comprehensive Evaluation (Accuracy, Precision, Recall, F1, ROC/AUC, Confusion Matrix)  
✅ Visualization Dashboards (Plotly interactive plots, Feature Importances, Decision Boundaries)  
✅ Streamlit Applications (Interactive Iris Classifier)  
✅ Neural Network Training with **training curves + misclassified examples**  

---

## 🚀 How to Run  

1. Clone repo & navigate:  
   ```bash
   git clone https://github.com/yourusername/Codveda_ML_Internship.git
   cd Codveda_ML_Internship

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run a specific notebook on Google Colab (recommended) or locally.
4. To run Streamlit app:
  ```bash
  streamlit run app/streamlit_app.py
```

---
👨‍💻 Author

Basel Amr Barakat
📧 baselamr52@gmail.com

🎓 Electrical Engineering (Computer & Control), Assiut University
💡 AI / ML Enthusiast | Deep Learning | Computer Vision | Data Science
