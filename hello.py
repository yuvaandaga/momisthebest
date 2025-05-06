import streamlit as st
import random

# Title and Introduction
st.title("Thanks for Everything You Have Done for Me 💖")
st.write("Here are some reasons that make you the best mom ever:")

# List of reasons
reasons = [
    "You always try to lead me to the right path!",
    "You always want my wellbeing!",
    "You make the best aamras!",
    "You are the best!",
    "You always want us to have fun!",
    "You always think of us before yourself!",
    "Sanjeev Kapoor is no match for your cooking!"
]

# When the button is clicked
if st.button("Show me a reason 💌"):
    # Show a random reason
    reason = random.choice(reasons)
    st.success(reason)

    # Load and play audio without showing file name
    try:
        with open("Bulleya-Sultan.mp3", "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3", start_time=0)
    except FileNotFoundError:
        st.error("⚠️ Audio file not found. Please make sure 'Bulleya-Sultan.mp3' is in the same folder.")
