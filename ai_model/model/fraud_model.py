import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# ✅ Load dataset
data = pd.read_csv('data/fraud_data.csv')

# ✅ Ensure 'Unknown' exists in the training data
if 'Unknown' not in data['Location'].values:
    data.loc[len(data)] = [99999, 0.0, 'Unknown', 0]  # Add dummy row with 'Unknown'

# ✅ Encode categorical features
encoder = LabelEncoder()
data['Location'] = encoder.fit_transform(data['Location'])  # Fit encoder with 'Unknown'

# ✅ Save the encoder
joblib.dump(encoder, 'model/label_encoder.pkl')  # Save the encoder

# ✅ Prepare dataset
X = data.drop(['IsFraud', 'TransactionID'], axis=1)
y = data['IsFraud']

# ✅ Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# ✅ Save the trained model
joblib.dump(model, 'model/fraud_model.pkl')

print("\n✅ Model trained and saved successfully!")
print("✅ LabelEncoder saved successfully!")
