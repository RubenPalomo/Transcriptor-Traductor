import speech_recognition as sr
import googletrans
from colorama import *

exit = False

def transcription():
    with sr.Microphone() as source:
        print(Fore.YELLOW + "Listening...")
        audio = sr.Recognizer().listen(source)
        try:
            transcription = sr.Recognizer().recognize_google(audio, language="en-EN")
            return transcription            
        except:
            return 

def traduction(string):
    translator = googletrans.Translator()
    return translator.translate(string, dest='es').text

def main():
    text = transcription()
    if (text):
        print(Fore.GREEN + text)
        print(Fore.BLUE + traduction(text) + "\n")
        if (text == "exit"):
            global exit
            exit = True

while(not exit):
    main();
