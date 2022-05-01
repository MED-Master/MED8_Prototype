## Run this command in terminal  before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## rasa run actions

#Libraries
import requests
import speech_recognition as sr     # import the library
from gtts import gTTS
from playsound import playsound
import os
import pyttsx3

class RASA:
    #mircophone setup
    #print(s_r.__version__)
    #sr.Microphone.list_microphone_names()
    # print(s_r.Microphone.list_microphone_names()) #print all the microphones connected to your machine
    my_mic = sr.Microphone(device_index=1)

    #API setup
    WIT_AI_KEY = 'IQAXGNZQWIAZL5VAI7GUT6JK3P3RJ3TZ' #wit API key
    #RASA setup
    engine = pyttsx3.init(driverName='sapi5')
    engine.setProperty("rate", 200)
    voices = engine.getProperty("voices")
    engine.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
    #engine.setProperty("voice", voices[1].id)
    bot_message = ""
    message = ""
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

    def VArecord(self):
        r = sr.Recognizer()  # initialize recognizer
        with self.my_mic as source:  # mention source it will be either Microphone or audio files.
            #print("Speak Anything :")
            r.adjust_for_ambient_noise(self.my_mic, duration=0.2)
            audio = r.listen(source)  # listen to the source

            try:
                self.message = r.recognize_wit(audio, key=self.WIT_AI_KEY)  # use recognizer to convert our audio into text part.
                #Logging.reply_logger.append(self.message)  # storing message string
                #print("You said : {}".format(self.message))

            except sr.UnknownValueError:
                print("I did not catch that, can you please say it again")
                r = sr.Recognizer()

            except sr.RequestError as e:
                print("Could not request results from API; {0}".format(e))
        return self.message

    def VAnlu(self, message):
        va_msg = []
        r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

        for i in r.json():
            self.bot_message = i['text']
            #print(f"{self.bot_message}")
            #Logging.reply_logger.append(self.bot_message)
            va_msg.append(self.bot_message)

        return va_msg

    def VAspeak(self, va_msg):
        #myobj = gTTS(text=va_msg, slow=False)
        #myobj.save("welcome.mp3")
        #playsound("welcome.mp3")
        #os.remove("welcome.mp3")
        self.engine.say(va_msg)
        self.engine.runAndWait()
        self.engine.stop()
