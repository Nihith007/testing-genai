import streamlit as st
from google import genai
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
