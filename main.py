import speech_recognition as sr
import pyttsx3
import pytgpt.phind as phind


def speak(text):
    engine.say(text)
    engine.runAndWait()


for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f'{index}, {name}')

mic = int(input("Choose a microphone: "))
bot = phind.PHIND()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

r = sr.Recognizer()
while True:
    with sr.Microphone(device_index=mic) as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio,language = "ro-RO")
            print("H: " + command)
            response = bot.chat(command)
            print("R: " + str(response))
            speak(response)
        except:
            print("*****************************************************")
