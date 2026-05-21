import streamlit as st
import requests

st.title("AI Research Assistant")

question=st.text_input(
    "Ask your document"
)

if st.button("Submit"):

    response=requests.post(
        "http://localhost:8000/ask",
        json={
            "question":question
        }
    )

    st.write(
        response.json()["answer"]
    )