import streamlit as st
from transformers import pipeline

model_name = "cardiffnlp/twitter-roberta-base-sentiment"
sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)

st.set_page_config(page_title="Sentiment Analysis", page_icon="💬", layout="centered")
st.markdown(
    """
    <style>
        .main {
            background-color: #f4f6f9;
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #4CAF50;
            text-align: center;
            margin-top: -20px;
        }
        .stButton{
            display:flex;
            justify-content: end;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border: None;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .button-container {
            display: flex;
            justify-content: flex-end;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Sentiment Analysis App 💬")

data = st.text_area(
    "Enter text below to analyze sentiment:",
    height=150,
    placeholder="Type your text here...",
)

st.markdown('<div class="button-container">', unsafe_allow_html=True)
if st.button("Analyze Sentiment"):
    if data.strip():
        result = sentiment_pipeline(data)
        sentiment = result[0]["label"]
        score = result[0]["score"]

        if sentiment == "LABEL_0":
            sentiment = "Negative"
        elif sentiment == "LABEL_2":
            sentiment = "Positive"
        elif sentiment == "LABEL_1":
            sentiment = "Neutral"

        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 20px;">
                <h2 style="color: #4CAF50;">Sentiment Analysis Result</h2>
                <p style="font-size: 18px;">Sentiment: <b>{sentiment}</b></p>
                <p style="font-size: 18px;">Confidence Score: <b>{score:.2f}</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("Please enter some text to analyze.")
st.markdown("</div>", unsafe_allow_html=True)
