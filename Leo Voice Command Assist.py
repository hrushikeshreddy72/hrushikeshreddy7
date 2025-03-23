import speech_recognition as sr
import webbrowser
import pyttsx3  # Ensure this is defined with a dictionary of songs
import requests
import openai  # Correct OpenAI import
from gtts import gTTS
import pygame
import os

# Replace with your actual API key
newsapi = "<Your NewsAPI Key>"
openai.api_key = "<Your OpenAI API Key>"

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[ 
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "news" in c.lower():
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                for article in articles:
                    speak(article['title'])
            else:
                speak("Sorry, I couldn't retrieve the news.")
        except requests.exceptions.RequestException as e:
            speak("There was an error retrieving the news.")
            print(f"Error: {e}")
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":  # Corrected initialization
    speak("Initializing Leo....")
    while True:
        # Listen for the wake word "leo"
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "leo":
                speak("Yes Leo is here?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Leo is Active...")
                    audio = r.listen(source)
                    try:
                        command = r.recognize_google(audio)
                        print(f"Command: {command}")
                        processCommand(command)
                    except sr.UnknownValueError:
                        speak("Sorry, I didn't understand that.")
                    except sr.RequestError as e:
                        speak("Sorry, there was an error with the speech service.")
                        print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
