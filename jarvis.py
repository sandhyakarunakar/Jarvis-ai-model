import sys
import time

import pyautogui # pip install PyAutoGUI
import pyttsx3 #pip install pyttsx3
import requests
import speech_recognition as sr # pip install SpeechRecognition
import datetime
import os
import cv2
import wikipedia
# import random
from requests import get
import webbrowser
import pywhatkit as kit  #pip install pywhatkit
import smtplib  #pip install smtplib
from twilio.rest import Client


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)  =>0   jarvis
engine.setProperty('voices', voices[0].id)


# text to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# taking command touser
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en_in')
        print(f'user said : {query}')
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


# for wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt=time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"Good Morning, it's {tt}")
    elif hour > 12 and hour < 18:
        speak(f"Good Afternoon, it's {tt}")
    else:
        speak(f"Good Evening, it's {tt}")
    speak(" I am Stella sir, Please tell me How can i help you")


# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.google.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your email id', 'your password')
    server.sendmail('your email id', to, content)
    server.close()

#for news
def news():
    main_url= "https://newsapi.org/v2/top-headlines?country=us&apiKey=5c8357b92d414a298453d18ad10297b3"
    main_page =requests.get(main_url).json()
    print(main_page)
    articels=main_page["articels"]
    print(articels)
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for a in articels:
        head.append(a["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: ",{head[i]})


if __name__ == "__main__":
    # takecommand()
    # speak("hello karunakar")
    wish()
    # while True:
    if 1:

        query = takecommand().lower()

        # logic building for tasks
        if "open notepad" in query:
            note_path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(note_path)

        elif "open command prompt" in query:
            # os.startfile("C:\\Windows\\system32\\cmd.exe")
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitkey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\Paul\\Desktop\\karna intern\\songs"
            songs = os.listdir(music_dir)
            # rd=random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            try:
                ip = get('https://api.ipfy.org').text
                speak(f"Your IP address is {ip}")
            except requests.exceptions.ConnectionError:
                speak(
                    "Sorry, I couldn't retrieve your IP address at the moment. Please check your internet connection.")

        elif "wikipedia" in query:
            speak("searching wikipedia............")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")

        elif "open google" in query:
            speak("Sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message to ravi" in query:
            # kit.sendwhatmsg("+918919188616","Hello dude",17,37)
            speak("sir, what should i send message to him")
            wc = takecommand().lower()
            kit.sendwhatmsg_instantly("+918919188616", wc)

        elif "text on whatsapp" in query:
            speak("sir, tell me the number")
            wc1 = takecommand().lower()
            speak("sir, what should i text")
            wc2 = takecommand().lower()
            kit.sendwhatmsg_instantly("+91" + str(wc1), wc2)

        elif "play song on youtube" in query:
            speak("Sir, what should i search on Youtube")
            yc = takecommand().lower()
            kit.playonyt(yc)
        # mail is on progress.....
        elif "send email" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "sandykarunakar@gmail.com"
                sendEmail(to, content)
                speak("email has been sent ")
            except Exception as e:
                print(e)
                speak("Sorry sir, i am not able to sent this mail")

        #for closing the tab's
        elif "close notepad" in query:
            speak("ok sir, Closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close cmd" in query:
            speak("ok sir, closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        # for alarm
        elif "set alarm" in query:
            NN=int(datetime.datetime.now().hour)
            if NN==24:
                music_dir="C:\\Users\\Paul\\Desktop\\karna intern\\songs"
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "you can rest" in query:
            speak("Thanks for using me, see u again ")
            sys.exit()

        #-----------------------------------switching the tabs------------------------------
        elif "change the tab" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        # for news information
        elif "any news" in query:
            speak("Please wait sir, feteching the latest news")
            news()
        elif "hello" in query:
            speak("hello sir, how can i help you?")
        elif "how are you" in query:
            speak("yeah! i'm fine sir, what about you?")
        elif "fine" in query:
            speak("i'm glad")
        elif "what are you doing" in query:
            speak("waiting for your command sir")

        # elif "call to ravi" in query:
        #     # Download the helper library from https://www.twilio.com/docs/python/install
        #
        #     # Set environment variables for your credentials
        #     # Read more at http://twil.io/secure
        #
        #     account_sid = "AC44c2904b754ccf1f3de8f43a46af331a"
        #     auth_token = "22009fa8be03c370845b9ab22972d79b"
        #     client = Client(account_sid, auth_token)
        #
        #     call = client.calls.create(
        #         url="http://demo.twilio.com/docs/voice.xml",
        #         to="+919182606802",
        #         from_="+15393287713"
        #     )
        #
        #     print(call.sid)


        # speak("Do you need anything sir")

