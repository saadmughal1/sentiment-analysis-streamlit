import streamlit as st
from utils import classify_sentiment


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
        sentiment_result = classify_sentiment(data)

        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 20px;">
                <h2 style="color: #4CAF50;">Sentiment Analysis Result</h2>
                <p style="font-size: 18px;">Sentiment: <b>{sentiment_result}</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("Please enter some text to analyze.")
st.markdown("</div>", unsafe_allow_html=True)
