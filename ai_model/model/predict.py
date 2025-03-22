import pandas as pd
import joblib

# ✅ Load the trained model and encoder
model = joblib.load('model/fraud_model.pkl')
encoder = joblib.load('model/label_encoder.pkl')

# ✅ New transactions for prediction
new_data = pd.DataFrame({
    'TransactionID': [10001, 10002, 10003],
    'Amount': [1500.75, 75.50, 300.0],
    'Location': ['California', 'New York', 'Texas']  # ✅ Includes new locations
})

# ✅ Handle unseen labels
known_labels = set(encoder.classes_)  # Get known labels
new_data['Location'] = new_data['Location'].apply(lambda x: x if x in known_labels else 'Unknown')

# ✅ Encode locations
new_data['Location'] = encoder.transform(new_data['Location'])

# ✅ Make predictions
predictions = model.predict(new_data[['Amount', 'Location']])

# ✅ Display results
new_data['Prediction'] = predictions

print("\n🛡️ Prediction Results:")
print(new_data[['TransactionID', 'Amount', 'Location', 'Prediction']])
