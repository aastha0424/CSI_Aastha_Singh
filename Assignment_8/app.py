# app.py

import streamlit as st
from rag_pipeline import answer_question

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Loan Application AI Assistant",
    layout="wide"
)

# ---- CUSTOM CSS ----
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-size: 32px !important;
        }

        h1, h2, h3 {
            font-size: 64px !important;
            font-weight: bold;
        }

        .stTextInput > div > div > input {
            font-size: 32px !important;
            padding: 0.75rem;
        }

        .stButton button {
            font-size: 32px !important;
            padding: 0.6rem 2rem;
        }

        .chat-box {
            background-color: #1f1f2e;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            font-size: 31px;
            line-height: 1.6;
        }

        .main {
            padding: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.title("📊 Loan Application AI Assistant")

st.markdown("""
Welcome to the **Loan Approval Q&A Chatbot**, powered by **RAG + LLMs** using Groq's blazing-fast LLaMA 3.

> ℹ️ Ask any question about the loan dataset like:
- *What is the average income of approved applicants?*
- *Does education affect approval?*
- *How many people are self-employed and approved?*
""")

# ---- 2-COLUMN LAYOUT ----
left_col, right_col = st.columns([2.2, 1.8])

# LEFT: Chatbot
with left_col:
    st.subheader("🧠 Ask a Question")
    user_input = st.text_input("Enter your question here...", key="input")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if st.button("Ask"):
        if user_input.strip():
            with st.spinner("Thinking..."):
                answer = answer_question(user_input)
                st.session_state.chat_history.append(("🧑 You", user_input))
                st.session_state.chat_history.append(("🤖 AI", answer))

    if st.session_state.chat_history:
        st.markdown("### 💬 Conversation")
        for speaker, msg in reversed(st.session_state.chat_history):
            bubble = f"**{speaker}**: {msg}"
            st.markdown(f"<div class='chat-box'>{bubble}</div>", unsafe_allow_html=True)

# RIGHT: Info Panel with Colors + Better Design
with right_col:
    st.markdown("""
        <div style="background-color: #111827; padding: 1.5rem; border-radius: 12px; border: 1px solid #333;">
        <h3 style='color:#93c5fd; margin-top:0;'>📚 Frequently Asked Questions</h3>

        <p><strong style="color:#facc15;">🤖 What is this chatbot for?</strong><br>
        <span style="color:#e5e7eb;">It helps analyze trends in loan application approvals using your dataset.</span></p>

        <p><strong style="color:#facc15;">🛠️ How does it work?</strong><br>
        <span style="color:#e5e7eb;">Using Retrieval-Augmented Generation (RAG), it fetches the most relevant records and then uses Groq’s LLaMA 3 to answer.</span></p>

        <p><strong style="color:#facc15;">🔍 What can I ask?</strong><br>
        <span style="color:#e5e7eb;">Ask about trends like income levels, credit history, or approval patterns.</span></p>

        <p><strong style="color:#facc15;">🔐 Is my data secure?</strong><br>
        <span style="color:#e5e7eb;">Yes. The data stays local and is only used temporarily for generating answers.</span></p>

        <hr style="margin: 1.5rem 0; border-color: #444;" />

        <h4 style='color:#6ee7b7;'>💡 Try Questions Like:</h4>
        <ul style="color:#e5e7eb; line-height: 1.5;">
            <li>What is the average loan amount?</li>
            <li>How many applicants had good credit history?</li>
            <li>Are self-employed people more likely to be denied?</li>
            <li>What is the most common reason for rejection?</li>
        </ul>

        <hr style="margin: 1.5rem 0; border-color: #444;" />

        <h4 style='color:#fca5a5;'>👩‍💻 About This App</h4>
        <p style="color:#e5e7eb;">This AI chatbot was developed as a demonstration of:</p>
        <ul style="color:#e5e7eb; line-height: 1.5;">
            <li><strong>RAG</strong> (Retrieval-Augmented Generation)</li>
            <li><strong>Groq's LLaMA 3</strong> (super fast LLM)</li>
            <li><strong>Streamlit</strong> for frontend UI</li>
        </ul>
        <p style="color:#a78bfa;">Made by <strong>Aastha Singh 💡</strong></p>
        </div>
    """, unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("""---""")
st.caption("⚙️ Powered by LLaMA 3 on Groq • Made with ❤️ in Streamlit • © 2025 Aastha Singh")
