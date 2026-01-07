import streamlit as st
from google import genai

try:
    # Create Gemini client (Streamlit secrets auto-load as env vars)
    client = genai.Client()
    st.write("✅ Gemini API client configured.")

    prompt = "Benefits of API key management?"

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    st.write(f"Response: {response.text}")

except Exception as e:
    st.error(f"❌ Error: {e}. Check your 'GEMINI_API_KEY' in secrets.")
   
API_KEY = "AIzaSyB1eTCDDXH5O4iru21pxwmWtWspSUUlMyQ"
client = genai.Client(api_key=API_KEY)
chat = client.chats.create(model="gemini-2.5-flash")
print("Gemini Chat (type 'exit' to stop)\n")
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    response = chat.send_message(user_input)
    print("Gemini:", response.text)
