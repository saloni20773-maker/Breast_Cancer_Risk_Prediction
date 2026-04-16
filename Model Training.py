import pandas as pd

# =========================
# 1. Load Data
# =========================
df = pd.read_csv(r"C:\Users\HP\Desktop\BIA\Breast_Cancer_Risk_Prediction\Data\Breast Cancer METABRIC.csv")

# =========================
# 2. Create event & time
# =========================
df['event'] = (df['Overall Survival Status'] == 'Deceased').astype(int)
df['time'] = df['Overall Survival (Months)']

# =========================
# 3. Target
# =========================
df['target_10yr'] = df['event']

# =========================
# 4. Drop missing values
# =========================
df = df.dropna()

# =========================
# 5. Features & Target
# =========================
X = df.drop(['target_10yr', 'time', 'event'], axis=1)
y = df['target_10yr']

# 🔥 IMPORTANT (remove text data)
X = X.select_dtypes(include=['number'])

# =========================
# 6. Train-Test Split
# =========================
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# =========================
# 7. Models
# =========================
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
acc_lr = accuracy_score(y_test, lr.predict(X_test))

# Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
acc_dt = accuracy_score(y_test, dt.predict(X_test))

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
acc_rf = accuracy_score(y_test, rf.predict(X_test))

# =========================
# 8. Results
# =========================
print("\nModel Results:")
print("Logistic Regression:", acc_lr)
print("Decision Tree:", acc_dt)
print("Random Forest:", acc_rf)

# Best model
best = max(acc_lr, acc_dt, acc_rf)

if best == acc_lr:
    print("Best Model: Logistic Regression")
elif best == acc_dt:
    print("Best Model: Decision Tree")
else:
    print("Best Model: Random Forest ⭐")

# =========================
# 9. Save Best Model
# =========================
import joblib
import os

model_dir = r"C:\Users\HP\Desktop\BIA\Breast_Cancer_Risk_Prediction\best_model"
os.makedirs(model_dir, exist_ok=True)

# Save Random Forest as the best model
joblib.dump(rf, os.path.join(model_dir, 'random_forest_model.pkl'))
print(f"\nBest model saved to: {model_dir}")