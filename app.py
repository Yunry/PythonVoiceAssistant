import webbrowser

import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio


# gets audio from mic
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
            speak("Sorry, I did not get that.")
        except sr.RequestError:
            print("Sorry, this service is not available.")
    return said.lower()


# converts the said to speech using gtts
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)


# debugging
# text = get_audio()
# speak(text)

while True:
    text = get_audio().lower()
    if 'youtube' in text:
        speak("Opening Youtube")
        webbrowser.open_new_tab("https://www.youtube.com")
    elif 'search' in text:
        speak("Searching Wikipedia...")
        query = text.replace("search", "")
        result = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(result)
        speak(result)
    elif 'joke' in text:
        speak(pyjokes.get_joke())
    elif 'exit' in text:
        speak("Goodbye, till next time")
        exit()