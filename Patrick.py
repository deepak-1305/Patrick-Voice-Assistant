import speech_recognition as sr
import pyttsx3
import datetime
import pyjokes
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import random
import pyfirmata
from pyfirmata import Arduino
from time import sleep
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate',150)
engine.setProperty('volume',1.0)
engine.setProperty('voice',voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
#we can add text to speak in speak()
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello sir,Good Morning")
        print("Hello sir,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello sir,Good Afternoon")
        print("Hello sir,Good Afternoon")
    else:
        speak("Hello sir,Good Evening")
        print("Hello sir,Good Evening")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Sorry, I could not understand. Could you please say that again?")
            return "None"
        return statement
wishMe()
print("im Patrick ")
speak("im Patrick")
def proverbs():
    import random
    a=["The apple doesn’t fall far from the tree","All that glitters is not gold. "," Better safe than sorry.","Two wrongs don’t make a right"," Time waits for no one.","When there’s smoke, there’s fire","You can’t have your cake and eat it too"," The pen is mightier than the sword."]
    b=a[random.randint(0,7)]
    print(b)
    speak(b)
def search_on_google(query):
    kit.search(query)

if __name__=='__main__':


    def jarvis():
      import os
      import random
      from random import randint
      while True:
        speak(" how can I help you sir?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('jarvis is shutting down,Good bye')
            print('jarvis is shutting down,Good bye')
            break
        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)
        elif 'what is the time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")
        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        elif 'can you answer me' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="Paste your unique ID here "
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            print(answer)
            speak(answer)
           
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by perumal raja")
            print("I was built by perumal raja")
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
        elif "play music" in statement or "play song" in statement:
            speak("Here you go with music")
            music_dir = "C:\\Users\\perumal raja\\Music\\eng"
            songs = os.listdir(music_dir)
            print(os.startfile(os.path.join(music_dir, songs[random.randint(1,30)])))
        elif "search" in statement:
            statement =statement.replace("search", "")
            search_on_google(statement)
        elif "god exist or not" in statement:
            speak("yes im created by perumal raja hence god is exist")
            print("Yes Im created by Perumal raja hence god is exist")
        elif "joke" in statement:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif " who I am" in statement:
            speak("If you talk then definitely your human.")
        elif " who are you" in statement:
             speak("I am Virtual being, My name is patrick")
             speak("My creator is perumal raja further my identity, It's a secret")
            
        elif " how are you" in statement:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif "i love you" in statement:
            speak("Hmmmm... I understand, but I am engaged with siri, I'll let you know in case of breakup, till then i can play some videos for you")
            webbrowser.open("https://www.youtube.com/watch?v=KmxOeAaBCpY")
        elif "what is the largest prime number" in statement:
            speak("the largest known prime number is 282,589,933−1")
        elif "play national anthem" in statement:
            webbrowser.open_new_tab("https://www.youtube.com/watch?v=HtMF973tXIY")
        elif "proverb" in statement:
            proverbs()
    jarvis()
            

        
            
        

        


        