import streamlit as st
from gtts import gTTS
import os
import base64

# App Title & Config
st.set_page_config(page_title="Text-to-Speech App", page_icon="🔊", layout="centered")

st.markdown("<h1 style='text-align: center; color: blue;'>🗣 Text to Speech Converter</h1>", unsafe_allow_html=True)

# Text Input
text = st.text_area("✍ Enter text to convert into speech:", max_chars=500)

# Live Character Count
st.write(f"📝 *{len(text)} / 500 characters used*")

# Language Selection
lang_options = {
    "English": "en",
    "Urdu": "ur",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es"
}
lang = st.selectbox("🌍 Choose Language:", list(lang_options.keys()))

# Voice Style (For now, this just acts as an accent selector)
voice_style = st.radio("🎙 Select Voice Style:", ["Male", "Female"])

# Function to Download Audio
def get_audio_download_link(audio_file, file_label="Download Audio"):
    with open(audio_file, "rb") as file:
        data = file.read()
        b64 = base64.b64encode(data).decode()
        return f'<a href="data:audio/mp3;base64,{b64}" download="{audio_file}">{file_label}</a>'

# Convert & Play Audio
if st.button("🔊 Convert & Play"):
    if text.strip():
        tts = gTTS(text=text, lang=lang_options[lang])
        audio_file = "output.mp3"
        tts.save(audio_file)

        # Display Audio Player
        st.audio(audio_file, format="audio/mp3")

        # Provide Download Link
        st.markdown(get_audio_download_link(audio_file), unsafe_allow_html=True)

    else:
        st.warning("⚠ Please enter some text before converting!")

# Footer
st.markdown("<hr><p style='text-align: center;'>Made with ❤ using Streamlit & gTTS</p>", unsafe_allow_html=True)