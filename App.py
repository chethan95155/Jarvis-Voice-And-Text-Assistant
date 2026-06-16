import streamlit as st
import speech_recognition as sr
from jarvis import process_command

st.set_page_config(
    page_title="Jarvis AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Jarvis AI Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Text Input Section
user_input = st.chat_input("Type a command...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Process command
    response = process_command(user_input)

    # Show assistant response
    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

st.divider()

# Voice Command Section
st.subheader("🎤 Voice Command")

if st.button("Start Listening"):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            st.info("Listening... Speak now")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

            voice_text = recognizer.recognize_google(
                audio,
                language="en-US"
            )

            st.success(f"You said: {voice_text}")

            st.session_state.messages.append(
                {"role": "user", "content": voice_text}
            )

            response = process_command(voice_text)

            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )

            st.rerun()

    except sr.UnknownValueError:
        st.error("Could not understand your speech.")

    except sr.RequestError:
        st.error("Speech Recognition service unavailable.")

    except Exception as e:
        st.error(f"Error: {e}")

# Sidebar
with st.sidebar:
    st.header("🤖 Jarvis Commands")

    st.markdown("""
    **Available Commands**
    
    - open chrome
    - open notepad
    - open calculator
    - open microsoft edge
    - open youtube
    - close chrome
    - close notepad
    - close calculator
    - close microsoft edge
    - close youtube
    - what is your name
    - who is your programmer
    - time
    - search [your query]
    - search python
    - search artificial intelligence
    """)

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()