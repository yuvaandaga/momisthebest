import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "your-api-key-here"  # Replace with your OpenAI API key

# Set the app title
st.title("Chat with Your Personal Assistant 🤖")

# Sidebar for user input
st.sidebar.header("Chat Settings")
user_name = st.sidebar.text_input("Your Name:", "User")

# Helper function to get GPT response
def get_gpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can also use "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Session state to store the chat history
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Chat history display
for message in st.session_state['messages']:
    if message['role'] == 'user':
        st.markdown(f"**{user_name}:** {message['content']}")
    else:
        st.markdown(f"**Assistant:** {message['content']}")

# User input
user_input = st.text_input(f"Ask {user_name}'s assistant", "")

# Button to send message
if st.button("Send"):
    if user_input:
        # Add the user's message to the history
        st.session_state['messages'].append({"role": "user", "content": user_input})
        
        # Get the assistant's response
        assistant_response = get_gpt_response(user_input)
        
        # Add the assistant's response to the history
        st.session_state['messages'].append({"role": "assistant", "content": assistant_response})
        
        # Clear the user input box
        st.experimental_rerun()

