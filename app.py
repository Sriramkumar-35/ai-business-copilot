"""
app.py
------
Streamlit chat UI for the AI Business Decision Copilot.

Run with:
    streamlit run app.py

Make sure you've already run:
    python db_setup.py
and that Ollama is running locally with the llama3.1 model pulled.
"""

import streamlit as st
from sql_agent import get_agent

st.set_page_config(page_title="AI Business Decision Copilot", page_icon="📊", layout="centered")

st.title("📊 AI Business Decision Copilot")
st.caption("Ask natural-language questions about your sales data — powered by a local open-source LLM.")

# Cache the agent so it isn't rebuilt on every rerun
@st.cache_resource
def load_agent():
    return get_agent(verbose=False)

agent = load_agent()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! Ask me anything about the sales data — e.g. 'What are the top 5 products by revenue?'"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Example question buttons
st.write("**Try an example:**")
example_cols = st.columns(3)
examples = [
    "Top 5 products by revenue",
    "Which region sold the most?",
    "Total revenue by category",
]
for col, example in zip(example_cols, examples):
    if col.button(example):
        st.session_state.pending_question = example

# Chat input
user_question = st.chat_input("Ask a question about your business data...")

question_to_ask = user_question or st.session_state.pop("pending_question", None)

if question_to_ask:
    st.session_state.messages.append({"role": "user", "content": question_to_ask})
    with st.chat_message("user"):
        st.markdown(question_to_ask)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                result = agent.invoke({"input": question_to_ask})
                answer = result.get("output", str(result))
            except Exception as e:
                answer = f"⚠️ Something went wrong: {e}"
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
