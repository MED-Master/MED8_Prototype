## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

import requests
import speech_recognition as sr     # import the library
import subprocess
from gtts import gTTS
from playsound import playsound
import os
import pyttsx3
import keyboard
import pandas as pd
import numpy
#mircophone setup
#print(s_r.__version__)
#sr.Microphone.list_microphone_names()
# print(s_r.Microphone.list_microphone_names()) #print all the microphones connected to your machine
my_mic = sr.Microphone(device_index=1)

#API setup
WIT_AI_KEY = 'IQAXGNZQWIAZL5VAI7GUT6JK3P3RJ3TZ' #wit API key

#data logging
reply_logger = []

#RASA setup
engine = pyttsx3.init()
bot_message = ""
message=""

r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

print("Bot says, ", end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

myobj = gTTS(text=bot_message)
myobj.save("welcome.mp3")
print('saved')
playsound("welcome.mp3")
os.remove("welcome.mp3")

#engine.say(bot_message)
#engine.runAndWait()



while bot_message != "Bye" or bot_message != 'thanks':
    r = sr.Recognizer()  # initialize recognizer
    with my_mic as source:  # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        r.adjust_for_ambient_noise(my_mic, duration=0.2)
        audio = r.listen(source)  # listen to the source

        try:
            message = r.recognize_wit(audio, key=WIT_AI_KEY) # use recognizer to convert our audio into text part.
            reply_logger.append(message) #storing message string
            print("You said : {}".format(message))

        except sr.UnknownValueError:
            print("I did not catch that, can you please say it again")
            r = sr.Recognizer()
            continue

        except sr.RequestError as e:
            print("Could not request results from API; {0}".format(e))
            continue

    if len(message) == 0:
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")
        reply_logger.append(bot_message)
        myobj = gTTS(text=bot_message)
        myobj.save("welcome.mp3")
        print('saved')
        playsound("welcome.mp3")
        os.remove("welcome.mp3")
    if keyboard.is_pressed('l'):
        dict = {'Replies': reply_logger}
        df = pd.DataFrame(dict)
        df.to_csv('Transcriptions.csv')
        print("Logging complete")
