import joblib

model = joblib.load("model/sentiment_analysis_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def classify_sentiment(text):
    text = text.lower()
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return "Positive" if prediction[0] == 1 else "Negative"