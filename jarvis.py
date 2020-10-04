import pyttsx3
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



if __name__ == "__main__":
    #speak("hello Mannan how are you")
    greet()