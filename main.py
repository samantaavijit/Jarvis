import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")   
    speak("I am Jarvis Sir. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("istening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        # print(e)
        print("Say that againg please....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("yourmail@gmail.com","your-password")
    server.sendmail('yourmail@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()
        # logic for executing task
        if 'wikipedia' in query:
            speak("Searching Wikipedia ..")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipwdia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query or 'play song' in query:
            music_dir='E:\\Music & Downloade\\INSTRUMENT MUSIC'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))

        elif 'stop the music' in query or 'stop music' in query:
            pass

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            
        elif 'open code' in query or 'open Visual Studio code' in query:
            code_path="C:\\Users\\Avijit Samanta\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        elif 'open android studio' in query:
            code_path='C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe'
            os.startfile(code_path)

        elif 'open pycharm' in query:
            code_path='C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe'
            os.startfile(code_path)

        elif 'open intellij' in query or 'open java' in query:
            code_path='C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.1.1\\bin\\idea64.exe'
            os.startfile(code_path)

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')

        elif 'open linkedin' in query:
            webbrowser.open('linkedin.com')
        elif 'email to avijit' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="yoursendmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email")

        elif 'quit' in query or 'exit' in query :
            break
