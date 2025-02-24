import streamlit as st
import pyttsx3
from gtts import gTTS
import os

# Custom Styles
st.set_page_config(page_title="Text to Speech App", page_icon="🗣", layout="centered")
st.markdown(
    """
    <style>
        .main { background-color: #f4f4f4; }
        h1 { color: #2E8B57; text-align: center; }
        div.stButton > button:first-child { background-color: #0084ff; color: white; border-radius: 10px; padding: 10px; }
        div.stButton > button:hover { background-color: #0060cc; }
        div.stSelectbox, div.stRadio, div.stSlider { background-color: white; padding: 10px; border-radius: 10px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# App UI
st.title("🗣 Text to Speech Converter")
st.write("Convert text into speech instantly!")

# Input Text
text = st.text_area("📝 Enter your text:", "Hello, how are you?", height=150)

# Select Voice Type
voice_type = st.radio("🎙 Choose Voice:", ["Male", "Female"], horizontal=True)

# Speech Speed
speed = st.slider("⏩ Adjust Speech Speed:", min_value=100, max_value=250, value=150, step=10)

# Choose Engine
engine_type = st.selectbox("🔧 Select TTS Engine:", ["pyttsx3 (Offline)", "gTTS (Online)"])

# Speak Button
if st.button("🔊 Speak Now"):
    if text.strip():
        if engine_type == "pyttsx3 (Offline)":
            # Using pyttsx3 (Offline)
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('rate', speed)

            # Set Voice Gender
            if voice_type == "Male":
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)

            # Speak
            engine.say(text)
            engine.runAndWait()
            st.success("✅ Speech is playing...")

        else:
            # Using gTTS (Google TTS - Online)
            tts = gTTS(text=text, lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3")  # Windows
            # os.system("afplay output.mp3")  # MacOS
            # os.system("mpg321 output.mp3")  # Linux
            st.success("✅ Playing speech using gTTS...")

    else:
        st.warning("⚠ Please enter some text to speak.")

# Footer
st.markdown("---")
st.markdown("🔹 *Created with ❤ using Python & Streamlit* | ✨ Enjoy your TTS experience! ✨")