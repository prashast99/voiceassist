import pyttsx3      #text-to-speech conversion library 
import datetime     
import speech_recognition as speech      #used for speech rcognition
from time import sleep 
import wikipedia as wiki
import webbrowser as web
import random, os
import smtplib
from email.message import EmailMessage
import requests                     #to make http requests
from bs4 import BeautifulSoup
from wikipedia.wikipedia import search       #to parse html documents

engine = pyttsx3.init('sapi5')  #Speech Application Programming Interface
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)      #speech rate

myfile = open('C:\\Users\\D P Vidyarthi\\Documents\\My Scans\\new\\password.txt','r')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening sir")
    speak("I'm Ethan your virtual assistant. How may i help you?")

def command():
    r = speech.Recognizer()
    with speech.Microphone() as source:
        print("Listening...\n")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language = 'en-in')
        print("\nUser Said: ", query)

    except Exception as e:
        print("\nSay that again...\n")
        return "None"
    return query

def email_config(to, subject, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('prashast99@gmail.com', myfile.read())
    server.sendmail('prashast99@gmail.com', to, subject, content)
    email = EmailMessage()
    email['From'] = 'prashast99@gmail.com'
    email['To'] = to
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

email_dict = {
    'me': 'prashast99@gmail.com',
    'professor': 'dpvidyarthi08@gmail.com', 
    'honey': 'aviralsrivastava5@gmail.com',
    'new': 'navyavidyarthi@gmail.com'
    }

def send_email():
    speak('To whom you wanna send email?')
    
    name = command()
    to = email_dict[name]
    print(to)

    speak('What is the Subject of your email?')
    subject = command()
    speak('What message should I write?')
    content = command()
    email_config(to, subject, content)
    speak('Email sent successfully')
    speak('do u want to send More emails?')
    send_more = command()
    if 'yes' in send_more:
        send_email()
    else:
        exit()

def weather():
    speak("Searching Google, please wait")
    to_search = 'weather in delhi'
    url = f'https://www.google.com/search?q={to_search}'    #search weather on google
    r = requests.get(url)                                   #send request to get the url
    data = BeautifulSoup(r.text, 'html.parser')
    temp = data.find("div", class_="BNeawe").text
    speak(f"Current {to_search} is {temp}")

if __name__ == "__main__":
    wish()
    while True:
    # if 1:
        query = command().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...Please Wait")
            query = query.replace("wikipedia","")
            results = wiki.summary(query, sentences = 3)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube...")
            web.open("youtube.com")
        
        elif 'on youtube' in query:
            speak("Okay sir, Searching on youtube")
            query = query.replace("search", "")
            query = query.replace("on youtube", "")
            url = f'https://www.youtube.com/results?search_query={query}'
            web.open(url)

        elif 'open google' in query:
            speak("Opening Google...")
            web.open("google.com")
        
        elif 'open facebook' in query:
            speak("Opening Facebook...")
            web.open("facebook.com")
        
        elif 'open twitter' in query:
            speak("Opening Twitter...")
            web.open("twitter.com")

        elif 'play music' in query:
            my_file = "D:\\Songs\\New folder\\new"
            music = os.listdir(my_file)
            speak("Playing Music")
            os.startfile(os.path.join(my_file,random.choice(music)))

        elif 'the time' in query:
            speak("Sir, The time is")
            time = datetime.datetime.now().strftime("%H:%M:%S:")      #returns a string representing date and time
            speak(time)
            
        elif 'open code' in query:
            path1 = 'C:\\Users\\D P Vidyarthi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(path1)

        elif 'google chrome' in query:
            path2 = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe' 
            os.startfile(path2)
        
        elif 'send mail' in query:
            send_email()
        
        elif 'weather' in query:
            weather()
        
        elif 'bye' in query:
            speak("Okay i am gonna sleep now, bye")
            exit()