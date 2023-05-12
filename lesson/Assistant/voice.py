import pywhatkit
import wikipedia
import requests
import speech_recognition as sr
import pyttsx3
import googletrans
from googletrans import Translator

translator = Translator()
#tr = translator.translate('안녕하세요.')
to = translator.translate('Hello.', dest='ja')
fro = translator.translate('veritas lux mea', src='la')
#print(tr)
print(to, fro)

def talk(text):
    engine.say(text)
    engine.runAndWait()
engine = pyttsx3.init()

'''inp = input("Type what you wnat to search: ")
inp1 = input("Type the talking speed rate: ")

engine. setProperty("rate", inp1)
wikipedia.set_lang("en")
wi = wikipedia.summary(inp, sentences=2)
print(wi)
talk(wi)
#pywhatkit.playonyt("PyWhatKit")
#pywhatkit.search("How to learn Python")

JOKE_API = 'http://rzhunemogu.ru/RandJSON.aspx?1'
VOICE_RU = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice', VOICE_RU)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("Microphone On")
with sr.Microphone(device_index=1) as source:
    listener.adjust_for_ambient_noise(source)
    voice = listener.listen(source)
    command = listener.recognize_google(voice, language="ru-RU").lower()
    print(command)

command = "хорошо выглядишиь"
if "как дела" in command:
    talk("хорошо, а у тебя?")
elif "рассмеши меня" in command:
    response = requests.get(JOKE_API)
    data = response.json(strict=False)
    joke = data['content']
    talk(joke)
elif 'привет' in command or 'здравствуйте' in command:
    talk('привет, давно не виделись!')
elif "хорошо выглядишиь" in command:
    talk('спасибо за комплимент!')
'''