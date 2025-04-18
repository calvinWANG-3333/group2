import streamlit as st

st.set_page_config(page_title="Group2 LLM Chatbot", layout="wide")
st.title("🧠 Welcome to Your Parisian LLM Chatbot, bonne journee")
st.markdown("2 page sur votre sidebar a gauche: (Homepage / Chat Page)")


st.markdown("""
    <style>
        .stApp {
            background-image: url("https://i.imgur.com/j6CjBvn.jpeg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        .title {
            font-size: 40px;
            font-weight: bold;
            color: #ffecec;
            text-shadow: 2px 2px 4px #000000;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #fff0f0 !important;
            text-shadow: 1px 1px 2px #000;
        }

        .stAlert-success {
            color: #004d00 !important;
            background-color: rgba(232, 255, 232, 0.95) !important;
        }

        button[kind="primary"] {
            background-color: #ff6699 !important;
            color: white !important;
            border: None;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)
