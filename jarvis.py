import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import datetime
import smtplib
import wolframalpha
import subprocess

#sapi5 is a microsoft api for voice assistant
engine = pyttsx3.init('sapi5')

voices =  engine.getProperty('voices')
#print(voices)
#setting id of voices, microsoft by default has 2 voices we can download more
engine.setProperty('voice', voices[1].id)
#print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    speak("Welcome back sir")
    speak("The current time is")
    time()
    speak("The current date is")
    date()
    if hour>= 0 and hour<12:
        speak("Good Morning, Mannan")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, Mannan")
    else:
        speak("Good Evening, Mannan")

    speak("I am Jarvis. How may I help you?")

def takeCommand():
    #fuction takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening. . ")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognising. .")
            query = r.recognize_google(audio, language = 'en-in')
            print(f"user said: {query}\n")

        except Exception as e:
                print(e)
                print("I was not able to catch that. Say that again please. . ")
                return "None"
        return query

def sendEmail(to, content):
    #init gmail SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #identify to server
    server.ehlo()
    #encrypt session
    server.starttls()
    server.login('mannanbhat60@gmail.com', 'redemption#@')
    server.sendmail('mannanbhat60@gmail.com', to, content)
    server.close()

     
        



if __name__ == "__main__":
    #speak("hello Mannan how are you")
    greet()
    
    #logic for executing tasks
    #while True:
    if 1:
        query  = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia. . ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:

            webbrowser.open("youtube.com")

        elif 'open google' in query:

            webbrowser.open("google.com")
            
        
        elif 'open stack overflow' in query:

            webbrowser.open("stackoverflow.com")
             
            
        
        elif 'play music' in query:
             music_dir = 'E:\\Music'
             songs = os.listdir(music_dir)
             print(songs)
             os.startfile(os.path.join(music_dir, songs[random.randint(0,100)]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the Time is {strtime}" )

            
        elif 'email to harry' in query:
                try:
                    speak("What should I say ?")
                    content = takeCommand()
                    to = "mannanbhat60@gmail.com"
                    sendEmail(to, content)
                    speak("email has been sent")
                except Exception as e:
                    print(e)
                    speak("sorry we were not able to send the email")

        elif 'news' in query:

            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            

        elif 'ask' in query:

            speak('I can answer to computational and geographical questions  and what question do you want to ask now?')
            question=takeCommand()
            app_id='QTQ574-4HYK5Y5QAK'
            client = wolframalpha.Client('QTQ574-4HYK5Y5QAK')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        
        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
			  
    


