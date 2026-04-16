import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load data
df = pd.read_csv("Breast Cancer METABRIC.csv")

# Preprocessing
df['event'] = (df['Overall Survival Status'] == 'Deceased').astype(int)

# Keep numeric only
df = df.select_dtypes(include=['number']).dropna()

# Features & target
X = df.drop(['event'], axis=1)
y = df['event']

# Train model
model = RandomForestClassifier()
model.fit(X, y)


# Prediction Function

def predict_patient(input_data):
    prediction = model.predict([input_data])
    
    if prediction[0] == 1:
        return "High Risk (Deceased)"
    else:
        return "Low Risk (Survived)"


# Example Test Run

if __name__ == "__main__":
    
    # Example input (mean values)
    sample_input = X.mean().values.reshape(1, -1)
    
    result = model.predict(sample_input)
    
    if result[0] == 1:
        print("Prediction: High Risk (Deceased)")
    else:
        print("Prediction: Low Risk (Survived)")