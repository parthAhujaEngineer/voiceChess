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

# --- Get Move-to Position ---
def toMove():
    info = getInfo().lower()
    if info == 'avon':
        info = 'a1'
    elif info == 'heetu' or info == 'hetu' or info == 'do' or info == 'tattoo' or info == 'airport' or info == 'tetu' or info == 'edu':
        info = 'a2'
    elif info == 'a tree' or info == '83':
        info = 'a3'
    elif info == 'krrish 4':
        info = 'a4'
    elif info == 'before':
        info = 'b4'
    elif info == 'bittu' or info == 'titu':
        info = 'b2'
    elif info == 'ba' or info == 'b.ed':
        info = 'b8'
    elif info == 'shivan' or info == 'shiva' or info == 'civil':
        info = 'c1'
    elif info == 'ceat':
        info = 'c8'
    elif info == 'deewan' or info == 'd 1' or info == 'devon' or info == 'devil':
        info = 'd1'
    elif info == 'even' or info == 'evil' or info == 'evan' or info == 'yuvan' or info == 't1':
        info = 'e1'
    elif info == 'youtube' or info == 'tu':
        info = 'e2'
    elif info == 'mi 4':
        info = 'e4'
    elif info == 'ito':
        info = 'e3'
    elif info == 'mi 5':
        info = 'e5'
    elif info == '8' or info == 'mi 8':
        info = 'e8'
    elif info == 'jivan':
        info = 'g1'
    elif info == 'jeetu' or info == 'jitu':
        info = 'g2'
    elif info == 'zefo':
        info = 'g4'
    return info

# --- Returns Audio-Input Position ---
def getMove(validMove):
    if validMove is False:
        speakText("invalid Move")
        speakText("Enter valid move")
    speakText("Select Piece")
    moveUCI = toMove()
    print(moveUCI)
    speakText("Move to")
    moveUCI += toMove()
    print(moveUCI)
    return moveUCI



