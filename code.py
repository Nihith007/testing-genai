import streamlit as st
from google import genai

# Set page title
st.set_page_config(page_title="Gemini Streamlit App")
st.title("🤖 Gemini Chat App")

try:
    # Get API key from Streamlit secrets
    api_key = st.secrets["GEMINI_API_KEY"]

    # Create Gemini client
    client = genai.Client(api_key=api_key)
    st.success("✅ Gemini API client configured")

    # Text input for user prompts
    prompt = st.text_input(
        "Ask Gemini something:",
        "Type your question here..."
    )

    if prompt:
        # Generate response from Gemini
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        st.markdown("### Gemini says:")
        st.write(response.text)

except KeyError:
    st.error("❌ GEMINI_API_KEY not found in Streamlit secrets.")
except Exception as e:
    st.error(f"❌ Error: {e}")
