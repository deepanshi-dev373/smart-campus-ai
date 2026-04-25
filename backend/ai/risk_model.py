def predict(att):
    if att < 50:
        return "High Risk ❌"
    elif att < 75:
        return "Medium Risk ⚠️"
    return "Low Risk ✅"