import streamlit as st
import pandas as pd
import joblib
from textblob import TextBlob
import os
import sys
from models_utils import extract_text, extract_skills

model = joblib.load("resume_classifier_model.sav")
st.title("Smart Resume Screening Tool")
uploaded_file = st.file_uploader("Upload a resume (PDF, DOCX, or TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    text = extract_text(uploaded_file)
    if text:
        prediction = model.predict([text])[0]
        sentiment = TextBlob(text).sentiment.polarity
        sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"

        st.markdown(f"**Predicted Job Role:** {prediction}")
        st.markdown(f"**Sentiment:** {sentiment_label}")
        st.markdown("**Extracted Skills:**")
        skills = extract_skills(text)
        st.write(", ".join(skills) if skills else "No matching skills found.")
    else:
        st.error("Unable to extract text from the uploaded file.")
