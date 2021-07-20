import speech_recognition as sr
import pyttsx3
import pyaudio
import socket

# --- Checks Online/Offline ---
def isConnected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

# --- Converts Text - Speech ---
def speakText(sentance):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(sentance, 'Luna')
    engine.setProperty('volume', 0.9)# --- Set Volume 0 - 1
    engine.runAndWait()
    
# --- Converts Speech - Text ---
def getInfo(): 
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=0.2)
            print("Please Speak Now ...")
            audio = listener.listen(source, phrase_time_limit = 3)
            if isConnected():
                info = listener.recognize_google(audio, language="en-IN")
            else:
                info = listener.recognize_sphinx(audio)
            print(info)
            return info.lower()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except:
        return ""
        pass

