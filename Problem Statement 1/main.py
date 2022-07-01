import speech_recognition as sr
import webbrowser
from constants import WIKIPEDIA_URL, GOOGLE_SEARCH_URL, STACKOVERFLOW_URL, YOUTUBE_URL, GOOGLE_URL, GMAIL_URL,\
    GOOGLE_MAP_URL, JOKE_URL, COVID_URL
import json
import requests
import tkinter
from tkinter import *
import random
import os
from gtts import gTTS
import playsound
from time import ctime
import datetime
from utils import DesktopAssistant

obj = DesktopAssistant()
r = sr.Recognizer()


def is_present(terms, voice_data):
    for term in terms:
        if term in voice_data:
            return True


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en-in')
    r = random.randint(1, 20000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def record_audio(ask=False):
    with sr.Microphone() as source:
        r.energy_threshold = 500  # voice level number increase more sensitive
        r.adjust_for_ambient_noise(source, 1.2)  # noise cancel rate
        r.pause_threshold = 1
        r.energy_threshold = 400
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio, language='en-in')

        except sr.RequestError:
            speak('Sorry, the service is down')
        except sr.UnknownValueError:
            print('Recognizing..')
        print(f">> {voice_data.lower()}")
        return voice_data.lower()


def wishMe(start):
    hour = int(datetime.datetime.now().hour)
    if start == True:
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<16:
            speak("Good Afternoon!")
        elif hour>=16 and hour<20:
            speak("Good Evening!")
        else:
            speak("Good Night!")
        c_time = obj.tell_time()
        speak("Initializing WAVE")
        speak("Starting all systems applications")
        speak(f"Currently it is {c_time}")
        speak("I am Wave. Your desktop assistant. Good to see you again.")
    else:
        speak('Goodbye sir')
        if hour>=0 and hour<12:
            speak("Have a good day!")

        elif hour>=18 and hour<24:
            speak("Have a good night!")
    pass

def callAssistant():
    wishMe(True)
    while True:
        voice_data = record_audio()
        if is_present(["hey", "hi", "hello", "wake up", "hai","hay"], voice_data):
            greetings = ["hey", "hey, what's up? ", " how can I help you", "I'm listening", "hello"]
            greet = greetings[random.randint(0, len(greetings) - 1)]
            speak(greet)


        if is_present(["your name", "what i call you", "what is your good name"], voice_data):
            name = record_audio("my name is Wave stand for virtual assistance version One. what's your name?")
            speak('Nice to meet you ' + name)
            speak('how can i help you ' + name)


        if is_present(["who are you", "your inventor", "invented you", "created you", "who is your developer"],
                      voice_data):
            greetings = ["I am Virtual Voice Assistant",
                         "I am developed by sayali as a voice assistance"]  # You can Add your name
            greet = greetings[random.randint(0, len(greetings) - 1)]
            speak(greet)

        if is_present(["what is your age", "how old are you", "when is your birthday"],
                      voice_data):
            greetings = ["I came into this world in June 2022"]
            greet = greetings[random.randint(0, len(greetings) - 1)]
            speak(greet)


        if is_present(
                ["how's everything", "how ia everything", "how are you", "how are you doing", "what's up", "whatsup"],
        voice_data):
            greetings = ["I am well ...thanks for asking ", "i am well", "Doing Great"]
            greet = greetings[random.randint(0, len(greetings) - 1)]
            speak(greet)


        if is_present(["What are you doing", "what you doing", "doing"], voice_data):
            greetings = ["nothing", "nothing...,just working for you", "Nothing much"]
            greet = greetings[random.randint(0, len(greetings) - 1)]
            speak(greet)


        if is_present(
                ["what's  the time", "tell me the time", "what time is it", "what is the time", "time is going on"],
        voice_data):
            time = ctime().split(" ")[3].split(":")[0:2]
            if time[0] == "00":
                hours = '12'
            else:
                hours = time[0]
            minutes = time[1]
            time = f'{hours} {minutes}'
            speak(time)


        if is_present(["wikipedia"],voice_data):
            search = record_audio('What do you want to search for?')
            url = WIKIPEDIA_URL + search
            webbrowser.get().open(url)
            speak('Here is what I found for' + search)


        if is_present(["do google", "search google", "on google", "search for", "in google", "open google search"],
                      voice_data):
            search = record_audio('What do you want to search for?')
            url = GOOGLE_SEARCH_URL + search
            webbrowser.get().open(url)
            speak('Here is what I found for' + search)

        elif is_present(["open stackoverflow"], voice_data):
            try:
                webbrowser.open(STACKOVERFLOW_URL)
                speak('Opening')
            except:
                speak('Could not perform the task. Please try again.')


        if is_present(["open the youtube", "open youtube"], voice_data):
            webbrowser.get().open(YOUTUBE_URL)
            speak('Opening')


        if is_present(["open the  google", "open google"], voice_data):
            webbrowser.get().open(GOOGLE_URL)
            speak('Opening')


        if is_present(["open gmail", "open email", "open my email", "check email"], voice_data):

            webbrowser.get().open(GMAIL_URL)
            speak('Opening')


        if is_present(["search youtube", "search the youtube", "search in youtube", "in youtube", "on youtube", "youtube"
                       "youtube search"],voice_data):
            search = record_audio('What do you want to search for?')
            r.pause_threshold = 2
            url = YOUTUBE_URL + 'results?search_query=' + search
            webbrowser.get().open(url)
            speak('Here is what I found')

        if is_present(["location"], voice_data):
            location = record_audio('What is the location?')
            url = GOOGLE_MAP_URL + location + '/&amp;'
            webbrowser.get().open(url)
            speak('Opening map of' + location)

            # OS shutdown
        if is_present(["shutdown system", "system off", "shutdown the system", "system shutdown"], voice_data):
            speak('Okay system will off in 30 seconds')
            os.system("shutdown /s /t 30")

        if is_present(["good", "thank you", "thanks", "well done"], voice_data):
            greetings = ["my pleasure", "Don't mention", "Thanks for your compliment", "No problem.",
                         "Thank you, it makes my day to hear that."]
            greet = greetings[random.randint(0, len(greetings) - 1)]
            speak(greet)

        if is_present(["exit", "quit", "sleep", "shut up", "close"], voice_data):
            greetings = ["Going offline ! you can call me Anytime", "Okay ,you can call me Anytime", "See you later",
                         "See you soon", "Have a good day."]
            greet = greetings[random.randint(0, len(greetings) - 1)]
            speak(greet)
            exit()

        if is_present(['love'], voice_data):
            speak('Wave loves you too')


        if is_present(['joke'], voice_data):
            speak("Fetching one...")
            data = requests.get(JOKE_URL).text
            parse = json.loads(data)
            if parse['type'] == 'single':
                speak(f"{parse['joke']}")
            else:
                speak(f"{parse['setup']}")
                speak(f"{parse['delivery']}")

        elif is_present(['corona cases', 'covid cases'], voice_data):
            data = requests.get(COVID_URL).text
            parser = json.loads(data)
            l = parser[::-1]
            today = (l[0])
            speak(f"There are {today['Cases']} confirmed corona cases in India.")

        elif is_present(['system'], voice_data):
            sys_info = obj.system_info()
            print(sys_info)
            speak(sys_info)
        elif is_present(['buzzing', 'news', 'headlines'], voice_data):
            news_res = obj.news()
            speak('Source: The Times Of India')
            speak('Todays Headlines are..')
            for index, articles in enumerate(news_res):
                speak(articles['title'])
                if index == len(news_res) - 2:
                    break
            speak('These were the top headlines, Have a nice day!!..')


def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    wn.after(100, update, ind)

# Creating the main window

wn = tkinter.Tk()
label1 = Label(wn, text = 'Wave Your Desktop Assistant', bg = 'black')
label1.config(font=("Comic Sans MS", 20))
label1.pack()

frames = [PhotoImage(file='assist.gif',format = 'gif -index %i' %(i)) for i in range(100)]
wn.title("Wave Desktop Assistant")

wn.geometry('700x300')
wn.config(bg='LightBlue1')
label = Label(wn, width = 500, height = 500)
label.pack()
wn.after(0, update, 0)

btn_call = Button(text = 'Start',width = 20, command = callAssistant, bg = '#5C85FB')
btn_call.config(font=("Courier", 15))
btn_call.pack()

btn_exit = Button(text = 'EXIT',width = 20, command = wn.destroy, bg = '#5C85FB')
btn_exit.config(font=("Courier", 15))
btn_exit.pack()

showCommand = StringVar()
cmdLabel = Label(wn, textvariable=showCommand, bg='LightBlue1',
                 fg='black', font=('Courier', 20))
cmdLabel.place(x=250, y=150)

# Runs the window till it is closed
wn.mainloop()