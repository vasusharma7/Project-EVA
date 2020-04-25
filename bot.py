from modules import *
from twitter import tweets
from chat import master_chat


while 1:
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")
        audio=r.listen(source,timeout = 10)
        print("Time over")
    try:
        text=r.recognize_google(audio)
    except:
        continue
    print("Text :"+text)
    if "stock" in text:
        for j in search(text, tld="co.in", num=10,stop=10,pause=2):
            if "moneycontrol.com" in j:
                break
    elif "chat mode" in text:
        # system("clear")
        master_chat()
    elif "news" in text:
        data = tweets(1,"EconomicTimes")
        speak = ""
        for i in data:
            speak += i.text
        speak = speak.replace("#","")
        speak=gTTS(text=speak,lang='en',slow=False)
        speak.save("./audio/news.mp3")
        os.system("./audio/news.mp3")
        continue
    elif "sleep" in text:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "translate" in text:
        text.replace("translate",'')
        browser=webdriver.Chrome()
        browser.get("https://translate.google.com/")
        src = browser.find_element_by_id('source')
        src.send_keys(text)
    elif "repeat" in text:
        text.strip()
        text.strip('repeat')
        text.strip('after')
        text.strip("me")
        print(text+" newwwwww")
        speak=gTTS(text=text,lang='en',slow=False)
        speak.save("./audio/welcome.mp3")
        os.system("./audio/welcome.mp3")
    elif "suggest" in text and "movie" in text:
        print("What genre would you like?")
        with sr.Microphone() as source:
            print("Speak")
            audio=r.listen(source)
            print("Over")
        text=r.recognize_google(audio)
        browser=webdriver.Chrome()
        text2="agoodmovietowatch.com"
        text2=text2+text
        for j in search(text2, tld="co.in", num=10,stop=10,pause=2):
            if "agoodmovietowatch.com" in j:
                break
    elif "exit" in text:
        print("GoodBye")
        break
    else:
        for j in search(text, tld="co.in", num=10,stop=1,pause=2):
            webbrowser.open_new_tab(j)
            pass
