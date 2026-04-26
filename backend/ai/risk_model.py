def predict(att):
    if att < 50:
        return "High Risk"
    return "Safe"