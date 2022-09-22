import speech_recognition as sr
import googletrans
import asyncio
from colorama import *

exit = False

async def transcription(audio):
    try:
        transcription = sr.Recognizer().recognize_google(audio, language="en-EN")
        aux(transcription)
    except:
        print() 

def traduction(string):
    translator = googletrans.Translator()
    return translator.translate(string, dest='es').text

def aux(text):
    if (text):
        print(Fore.GREEN + text)
        print(Fore.BLUE + traduction(text) + "\n")
        if (text == "exit"):
            global exit
            exit = True

def microphone():
    with sr.Microphone() as source:
        audio = sr.Recognizer().listen(source)
        return(audio)


async def main():
    while(not exit):
        audio = microphone()
        if (audio):
            task = asyncio.create_task(transcription(audio))
        await task

if __name__ == '__main__':    
    print(Fore.YELLOW + "Listening...")
    asyncio.run(main())
