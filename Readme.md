# 🎗️ Breast Cancer Risk Prediction using Machine Learning

## 📌 Overview
Breast cancer is one of the leading causes of death among women worldwide. Early detection plays a crucial role in improving survival rates.

This project aims to build a machine learning model that predicts whether a patient is at **high risk or low risk** of breast cancer using clinical data.

---
## 📌 Problem Statement
Breast cancer is one of the leading causes of mortality worldwide.
Early identification of high-risk patients can significantly improve treatment outcomes.
Predicting survival risk in advance allows healthcare professionals to:


-Identify high-risk patients early
- Optimize treatment strategies
- Improve patient monitoring and care

This project predicts whether a patient is:
- High Risk (Deceased)
- Low Risk (Survived)
based on historical clinical and tumor data.

---

## 🚀 Key Features
- End-to-end machine learning pipeline
- Data cleaning & exploratory analysis using Jupyter Notebooks
- Feature engineering & preprocessing
- Survival analysis using Kaplan-Meier & Cox models
- Multiple ML models trained and compared
- Best-performing model selected for deployment
- Streamlit-based UI for real-time predictions
- Clean, production-ready project structure

---

## App Capabilities
- Enter patient clinical details
- Predict survival risk (High / Low)
- Instant real-time inference
- Simple and user-friendly interface


---
## 🧠 Machine Learning Workflow

Raw Clinical Data
   ↓
Data Cleaning & Feature Engineering
   ↓
Exploratory Data Analysis (EDA)
   ↓
Survival Analysis (Kaplan-Meier & Cox)
   ↓
Model Training & Evaluation
   ↓
Best Model Selection
   ↓
Streamlit Deployment
---

---
## 📁 Project Structure

Breast_Cancer_Risk_Prediction/
│
├── app.py                          # Streamlit application (ROOT)
├── best_model.pkl                  # Trained ML model
├── requirements.txt                # Dependencies (ROOT)
├── README.md
├── .gitignore
│
├── SRV/                            # Core ML logic
│   └── Model training.py           # Model training pipeline
│
├── Data/                           # Dataset (not uploaded)
│   └── Breast Cancer METABRIC.csv
│
├── Notebooks/                      # Analysis & experimentation
│   ├── Preprocessing.ipynb
│   ├── EDA.ipynb
│   ├── Kaplan-Meier Model.ipynb
│   ├── Cox Model.ipynb
│   └── Machine learning Models.ipynb
│
└── venv/                           # Virtual environment (ignored)
---


## 🎯 Objectives
- Predict breast cancer risk using ML models  
- Compare multiple algorithms  
- Identify the best performing model  
- Assist in early diagnosis and decision-making  

---

## 📊 Dataset Information
- **Dataset:** METABRIC (Molecular Taxonomy of Breast Cancer International Consortium)  
- **Type:** Clinical + Genomic Data  
- **Samples:** ~2000 patients  
- **Features:** Age, tumor size, lymph nodes, gene expression, etc.  
- **Target Variable:** `event` (Survival / Risk)

---

## ⚙️ Data Preprocessing
- Handling missing values  
- Encoding categorical variables  
- Feature selection  
- Target variable creation  

---

## 📈 Exploratory Data Analysis (EDA)
- Histogram (data distribution)  
- Heatmap (correlation analysis)  
- Feature relationship analysis  

---

## 🤖 Machine Learning Models
- Logistic Regression  
- Decision Tree  
- Random Forest  

---

## 🧪 Model Training & Evaluation
- Train-Test Split applied  
- Models trained on training data  
- Performance evaluated using:
  - Accuracy  
  - Confusion Matrix  

---

## 📊 Model Performance Comparison

| Model               | Accuracy |
|--------------------|----------|
| Logistic Regression| 73.97%   |
| Decision Tree      | 74.89%   |
| Random Forest      | 79.91%   |

🏆 **Best Model: Random Forest**

---

## 📊 Confusion Matrix

|               | Predicted Low | Predicted High |
|---------------|--------------|----------------|
| Actual Low    | 76 (TN)      | 21 (FP)        |
| Actual High   | 27 (FN)      | 95 (TP)        |

### 🔍 Insights
- Model correctly predicts majority of cases  
- False Negatives are critical in medical context  
- Overall performance is reliable  

---

## 📊 Technologies Used
- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Lifelines (Survival Analysis)
- Matplotlib / Seaborn
- Streamlit
- Joblib
- Jupyter Notebook

---

## 🚀 Future Enhancements
- Probability-based risk scoring
- Model explainability (SHAP)
- REST API using FastAPI
- Docker containerization
- Advanced hyperparameter tuning

---
## 🤝 Contributing
Contributions, suggestions, and feature requests are welcome.
Feel free to open an issue or submit a pull request.

---

## 👩‍💻 Author
Saloni Sharma
Course: Data Science & AI
---

## 🙏 Acknowledgements
-METABRIC Dataset
- Open-source machine learning community
- Survival analysis libraries

---
