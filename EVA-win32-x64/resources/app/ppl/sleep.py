from modules import*

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    text = text.lower()
except:
    sys.exit(0)
if text=="wake up":
    print("Activate")
else:
    print("Sleep")
