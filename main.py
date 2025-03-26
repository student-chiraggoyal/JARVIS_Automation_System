import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkdein" in c.lower():
        webbrowser.open("https://www.linkedin.com/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fin%2Foscar-de-la-torre-tenorsoloist%3FmidToken%3DAQEaLRphTzRIdw%26midSig%3D16d1n68ZJqzq01%26trk%3Deml-email_pymk_02-header-109-profile%26trkEmail%3Deml-email_pymk_02-head")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initilaizing Jarvis.....")
    while True:
        # listen for the wake word "jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        # recognize speech 
        print("recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening......")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)

            word = recognizer.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Ya")

                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))