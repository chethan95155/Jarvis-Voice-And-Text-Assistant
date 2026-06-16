import speech_recognition as sr
import pyttsx3
import os
import datetime
import subprocess
import sys
import threading
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

tts_lock = threading.Lock()

recognizer  = sr.Recognizer() 

def speak(text):
    print("Jarvis:",text)
    try:
        with tts_lock:
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            if voices:
                index = 1 if len(voices) > 1 else 0
                engine.setProperty('voice', voices[index].id)
            engine.say(text)
            engine.runAndWait()
            engine.stop()
    except Exception:
        pass

def open_software(software_name):
    if 'chrome' in software_name:
        speak('Opening Chrome...')
        program = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])

    elif 'microsoft edge' in software_name:
        speak('Opening Microsoft Edge...')
        program = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        subprocess.Popen([program])

    elif 'youtube' in software_name:
        try:
            import pywhatkit
            speak("Opening YouTube")
            pywhatkit.playonyt(software_name)
        except Exception as e:
            speak("Unable to open YouTube")
            print(e)

    elif 'notepad' in software_name:
        speak('Opening Notepad...')
        subprocess.Popen(['notepad.exe'])
        
    elif 'calculator' in software_name:
        speak('Opening Calculator...')
        subprocess.Popen(['calc.exe'])
        
    else:
        speak(f"I couldn't find the software {software_name}")

def close_software(software_name):
    if 'chrome' in software_name:
        speak('Closing Chrome...')
        os.system("taskkill /f /im chrome.exe")

    elif 'microsoft edge' in software_name:
        speak('Closing Microsoft Edge...')
        os.system("taskkill /f /im msedge.exe")

    elif 'notepad' in software_name:
        speak('Closing Notepad...')
        os.system("taskkill /f /im notepad.exe")
        
    elif 'calculator' in software_name:
        speak('Closing Calculator...')
        os.system("taskkill /f /im calculator.exe")
    elif 'youtube' in software_name:
        speak('Closing YouTube...')
        os.system("taskkill /f /im youtube.exe")
    else:
        speak(f"I couldn't find any open software named {software_name}")

def ai_search(prompt):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(
            f"Give a short answer in 2 sentences: {prompt}"
        )

        answer = response.text.strip()

        print("Gemini Response:", answer)

        speak(answer)

        return answer

    except Exception as e:
        print("Gemini Error:", e)
        return f"Error: {e}"


def process_command(query):
    text = (query or "").lower().strip()

    if not text:
        return ""

    if 'stop' in text:
        message = 'Stopping the program. Goodbye!'
        speak(message)
        return message
    elif 'open' in text:
        software_name = text.replace('open', '').strip()
        open_software(software_name)
        return f"Opening {software_name}"
    elif 'close' in text:
        software_name = text.replace('close', '').strip()
        close_software(software_name)
        return f"Closing {software_name}"
    elif 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(current_time)
        return current_time
    elif 'who is your programmer' in text:
        speak('Chethan')
        return 'Chethan'
    elif 'what is your name' in text:
        message = 'My name is Jarvis Your Artificial Intelligence'
        speak(message)
        return message
    elif 'search' in text:
        prompt = text.replace("search", "").strip()
        speak("Searching")

        answer = ai_search(prompt)

        return answer

    message = "I can help with open, close, time, programmer info, and search commands."
    speak(message)
    return message

def listen_for_wake_word():
    with sr.Microphone() as source:
        print('Listening for wake word...')
        while True:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recorded_audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(recorded_audio, language='en_US')
                text = text.lower()
                if 'jarvis' in text:
                    print('Wake word detected!')
                    speak('Hi Sir, How can I help you?')
                    return True
            except Exception as ex:
                print("Could not understand audio, please try again.")

def cmd():
    with sr.Microphone() as source:
        print('Clearing background noise... please wait!')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('Ask me anything...')
        recorded_audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(recorded_audio, language='en_US')
        text = text.lower()
        print('Your message:', text)
    except:
        speak("Please say that again")
        return

    if 'stop' in text:
        speak('Stopping the program. Goodbye!')
        sys.exit()
    elif 'open' in text:
        software_name = text.replace('open', '').strip()
        open_software(software_name)
    elif 'close' in text:
        software_name = text.replace('close', '').strip()
        close_software(software_name)
    elif 'time' in text:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        print(current_time)
        speak(current_time)
    elif 'who is your programmer' in text:
        speak('Chethan')
    elif 'what is your name' in text:
        speak('My name is Jarvis Your Artificial Intelligence')
    elif 'search' in text:
        prompt = text.replace("search", "")
        speak("Searching")
        ai_search(prompt)
        speak("What else can I do for you")

def main():
    while True:
        if listen_for_wake_word():
            while True:
                if cmd():
                    break


if __name__ == "__main__":
    main()