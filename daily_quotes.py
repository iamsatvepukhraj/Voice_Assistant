import requests
import random
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to retrieve a random quote from the ZenQuotes API
def get_random_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']  # Extract the quote text
        return quote
    else:
        return "Failed to retrieve a quote."


# Function to speak out the quote and update GUI label
def speak_quote(quote):
    engine.say(quote)
    engine.runAndWait()
    


# Function to handle the "Give me a quote" voice command
def handle_quote_command():
    quote = get_random_quote()
    speak_quote(quote)


# Function to greet the user and provide the daily quote
def greet_user():
    speak_quote("Welcome! Here's your daily quote:")
    handle_quote_command()
