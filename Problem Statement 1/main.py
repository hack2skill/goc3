import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import wikipedia
import datetime
import webbrowser

user = sr.Recognizer()                          # Using the Speech Recognition
viaa = pyttsx3.init()                           # Initialising the text to speech library
voices = viaa.getProperty('voices')
viaa.setProperty('voice', voices[1].id)         # Setting female voice


def speak(text):
    viaa.say(text)          # Using text to speech to say the required term
    viaa.runAndWait()


def start():
    try:
        with sr.Microphone() as source:
            print('--Started--')
            voice = user.listen(source)                 # Getting the input from the microphone
            command = user.recognize_google(voice)      # Recognizing the voice
            command = command.lower()
            if 'viaa' or 'via' or 'vea' or 'viia' or 'iia' or 'illa' or 'villa' in command:
                print('How can I help you?')
                speak("How can I help you?")
                run_viaa()
    except:
        pass


def run_viaa():
    with sr.Microphone() as source:
        voice = user.listen(source)
        command = user.recognize_google(voice)
        command = command.lower()
    if 'play' in command:                           # If the same command found
        song = command.replace('play', '')
        print('playing' + song)
        speak('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:                         # If the same command found
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        speak('Current time is ' + time)
    elif 'wiki' or 'who' in command:                         # If the same command found
        search = command.replace('wiki' or 'who is', '')
        info = wikipedia.summary(search, 1)
        print(info)
        speak(info)
    elif 'search' in command:                         # If the same command found
        search = command.replace('search', '')
        info = webbrowser.get(search)
        print(info)
        speak(info)
    elif 'are you single' in command:                         # If the same command found
        print('Sorry, I am in relationship with your Wi-Fi')
        speak('Sorry, I am in relationship with your Wi-Fi')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    else:                                       # Could not understand the voice
        print('Sorry, I could not understand')
        print('Please say the command again')
        speak('Sorry, I could not understand')
        speak('Please say the command again')


start()                # Calling the start function
