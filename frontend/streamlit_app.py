import streamlit as st
import requests

st.title("🇮🇳 Tamil Nadu Smart Govt Assistant")

query = st.text_input("Ask your government service question:")

if st.button("Assist"):

    res = requests.post(
        "http://localhost:8000/assist",
        json={"query": query}
    )

    data = res.json()

    st.subheader("Plan")
    st.write(data["plan"])

    st.subheader("Scheme Info")
    st.write(data["scheme"])

    st.subheader("Application Draft")
    st.write(data["application_draft"])
