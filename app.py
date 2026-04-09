import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# API Key settings
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

st.set_page_config(page_title="AI Code Refactorer", layout="wide")

st.title("🛠️ Intelligent Code Refactoring Tool")
st.write("Legacy code-ah modern-ah mathalam!")

col1, col2 = st.columns(2)

with col1:
    st.header("Legacy Code")
    legacy_code = st.text_area("Paste code here:", height=300)

if st.button("Refactor Now ✨"):
    if legacy_code:
        with st.spinner("AI is analyzing..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Refactor this code to modern standards, fix security bugs, and add 3 unit tests: {legacy_code}"
            response = model.generate_content(prompt)
            with col2:
                st.header("Refactored Code")
                st.code(response.text)
    else:
        st.error("Pazhaya code-ah paste pannunga!")