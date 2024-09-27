import streamlit as st
from PIL import Image
import json
from main import load_qa_pairs, get_response

# Load the JSON file
qa_pairs = load_qa_pairs('../assets/qa_pairs.json')


# Initialize session state for messages if not already done
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Sidebar for image upload
st.sidebar.title("Food Image Upload")
image_file = st.sidebar.file_uploader("Upload a food image", type=['jpg', 'png'])

# Show the uploaded image on the sidebar if any
if image_file:
    image = Image.open(image_file)
    st.sidebar.image(image, caption="Uploaded Food Image", use_column_width=True)

# User input for the chatbot
user_question = st.chat_input("How may I assist you?")

# Handle user input
if user_question:
    # Append user question to the message history
    st.session_state.messages.append({"role": "user", "content": user_question})

    # Get response based on the question
    response = get_response(user_question, qa_pairs)
    
    # Append the assistant's response to the message history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Clear the input field after submission
    user_question = ""  # This line clears the input field

# Display chat messages after updating
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Message when no image is uploaded
if not image_file:
    st.sidebar.write("Please upload a food image to display it here.")