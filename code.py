import streamlit as st
from google import genai

st.set_page_config(page_title="Gemini Streamlit App")

st.title("🤖 Gemini Streamlit App")

try:
    # Read API key from Streamlit secrets
    api_key = st.secrets["GEMINI_API_KEY"]

    # Create Gemini client
    client = genai.Client(api_key=api_key)
    st.success("✅ Gemini API client configured")

    # User input box (THIS replaces input())
    prompt = st.text_input(
        "Ask Gemini something:",
        "Benefits of API key management"
    )

    if prompt:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        st.write("### Gemini says:")
        st.write(response.text)

except KeyError:
    st.error("❌ GEMINI_API_KEY not found in Streamlit secrets.")
except Exception as e:
    st.error(f"❌ Error: {e}")
