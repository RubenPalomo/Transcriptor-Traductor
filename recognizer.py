import speech_recognition as sr
import googletrans
import asyncio
from colorama import *

exit = False

# Function to transcribe the audio to a string using Google
async def transcription(audio):
    try:
        transcription = sr.Recognizer().recognize_google(audio, language="en-EN")
        print_result(transcription)
    except:
        print() 

# Function to translate the string using Google
def translation(string):
    translator = googletrans.Translator()
    return translator.translate(string, dest='es').text

#Function to print all the results and change the boolean exit
def print_result(text):
    if (text):
        print(Fore.GREEN + text)
        print(Fore.BLUE + translation(text) + "\n")
        if (text == "exit"):
            global exit
            exit = True

# Function to capture audio
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
