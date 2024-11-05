import speech_recognition as sr
import pyttsx3
import webbrowser
import os

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak out the response
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to process user commands
def process_command(command):
    if command.startswith("open application"):
        # Extract the application name from the command
        application = command.split("open application")[-1].strip()
        speak(f"Opening application {application}")
        os.startfile(application)
    elif command.startswith("open website"):
        # Extract the website name from the command
        website = command.split("open website")[-1].strip()
        speak(f"Opening website {website}")
        webbrowser.open(f"https://www.{website}.com")
    elif command.startswith("search"):
        # Extract the search query from the command
        query = command.split("search")[-1].strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif command.startswith("quit"):
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I couldn't understand that command.")

# Function to handle voice command
def handle_voice_command():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        return command  # Return the recognized command
    except sr.UnknownValueError:
        speak("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        speak(f"Error: {str(e)}")
    return ""  # Return an empty string if command recognition fails



# Function to greet the user
def greet_user():
    speak("Welcome! What command do you have for me?")
