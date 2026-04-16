## 🎗️ Breast Cancer Risk Prediction using Machine Learning
A machine learning project that predicts breast cancer patient survival risk using clinical data.
The model is trained using classical ML algorithms and deployed as an interactive Streamlit web application for real-time predictions.
🔗 Live App:
👉 (Add your Streamlit deployment link here)

## 📌 Problem Statement
Breast cancer is one of the leading causes of mortality worldwide.
Early identification of high-risk patients can significantly improve treatment outcomes.
Predicting survival risk in advance allows healthcare professionals to:


-Identify high-risk patients early
-Optimize treatment strategies
-Improve patient monitoring and care

This project predicts whether a patient is:
-High Risk (Deceased)
-Low Risk (Survived)
based on historical clinical and tumor data.

## 🚀 Key Features
-End-to-end machine learning pipeline
-Data cleaning & exploratory analysis using Jupyter Notebooks
-Feature engineering & preprocessing
-Survival analysis using Kaplan-Meier & Cox models
-Multiple ML models trained and compared
-Best-performing model selected for deployment
-Streamlit-based UI for real-time predictions
-Clean, production-ready project structure



## 🌐 Live Application
🔗 Try the app here:
👉 (Add your Streamlit link after deployment)

## App Capabilities
-Enter patient clinical details
-Predict survival risk (High / Low)
-Instant real-time inference
-Simple and user-friendly interface



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



## 📊 Dataset
-Breast Cancer METABRIC Dataset (not included)
The dataset contains:
-Patient demographic and clinical information
-Tumor characteristics
-Survival time and status
⚠️ Dataset is not uploaded due to size and privacy considerations.
Please place the dataset manually inside the Data/ folder.

## ⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/yourusername/Breast_Cancer_Risk_Prediction.gitcd Breast_Cancer_Risk_Prediction

2️⃣ Create and activate virtual environment
python -m venv venvvenv\Scripts\activate      # Windowssource venv/bin/activate   # macOS/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

## 🧹 Data Preparation
Data cleaning and preprocessing are performed in:
-Notebooks/Preprocessing.ipynb
-Notebooks/EDA.ipynb

Survival analysis:
-Kaplan-Meier Model
-Cox Proportional Hazards Model


## 🤖 Model Training
Run training from the project root:
python SRV/Model training.py

Training pipeline:
-Load dataset
-Preprocess features
-Train-test split
-Train multiple ML models
-Evaluate and compare performance

Models trained:
-Logistic Regression
-Decision Tree
-Random Forest

Best model is saved as:
best_model.pkl

## 🖥️ Run Streamlit App
From the project root:
streamlit run app.py


## ⚡ Features
-Real-time prediction
-Clean UI interface
-Numerical input handling
-Fast inference using trained model



## 📦 Deployment & Prediction
Deployment:
-Streamlit Cloud (recommended)

Prediction:
-Model loaded using joblib
-Input features processed
-Output returned as risk classification


## 📊 Technologies Used
-Python 3.x
-Pandas, NumPy
-Scikit-learn
-Lifelines (Survival Analysis)
-Matplotlib / Seaborn
-Streamlit
-Joblib
-Jupyter Notebook


## 🚀 Future Enhancements
-Probability-based risk scoring
-Model explainability (SHAP)
-REST API using FastAPI
-Docker containerization
-Advanced hyperparameter tuning


## 🤝 Contributing
Contributions, suggestions, and feature requests are welcome.
Feel free to open an issue or submit a pull request.

## 👩‍💻 Author
Saloni Sharma
Course: Data Science & AI

## 🙏 Acknowledgements
-METABRIC Dataset
-Open-source machine learning community
-Survival analysis libraries



