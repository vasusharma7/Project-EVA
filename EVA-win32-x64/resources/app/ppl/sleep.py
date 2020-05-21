from modules import *

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    text = text.lower()
    if text == "pluto":
        print("activate")
    else:
        print("deactivate")
except:
    print("error")
    sys.exit(0)
