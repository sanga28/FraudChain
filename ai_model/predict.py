import torch

def predict(transaction):
    # Load the model
    model = torch.load('./models/fraud_model.pt')
    model.eval()

    # Example inference
    result = model(transaction)
    print("Prediction:", result)