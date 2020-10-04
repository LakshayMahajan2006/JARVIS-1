import pyttsx3
#sapi5 is a microsoft api for voice assistant
engine = pyttsx3.init('sapi5')

voices =  engine.getProperty('voices')
print(voices)
#setting id of voices, microsoft by default has 2 voices we can download more
engine.setProperty('voice', voices[1].id)
print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
if __name__ == "__main__":
    speak("hello Mannan how are you")