import streamlit as st
from google import genai

st.set_page_config(page_title="Gemini Chat")
st.title("💬 Gemini Chat")

# Create Gemini client
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type a message")

if user_input:
    # Store and display user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    try:
        # Gemini response
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # ✅ FIXED MODEL
            contents=user_input
        )

        reply = response.text.strip()

    except Exception:
        reply = "❌ Gemini API error. Please try again."

    # Store and display assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
    with st.chat_message("assistant"):
        st.markdown(reply)
