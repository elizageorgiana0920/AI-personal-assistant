import webbrowser
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia


engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""
    return command.lower()


def assistant():
    speak("Hello! I am your personal assistant. How can I help you today?")
    while True:
        command = listen()
        if 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            speak(f"The time is {time}")
        elif 'wikipedia' in command:
            speak("Searching Wikipedia...")
            query = command.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
        elif 'exit' in command or 'quit' in command:
            speak("Goodbye!")
            break
        else:
            speak("I can not handle that yet.")

if __name__ == "__main__":
    assistant()
