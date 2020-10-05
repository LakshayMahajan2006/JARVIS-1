import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime

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


if __name__ == "__main__":
    #speak("hello Mannan how are you")
    greet()
    
    #logic for executing tasks
    while True:
        query  = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia. . ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowseropen("youtube.com")

        elif 'open google' in query:
            webbrowseropen("google.com")
        
         elif 'open stackoverflow' in query:
            webbrowseropen("stackoverflow.com")
        
    


