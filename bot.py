from modules import *
from twitter import tweets
from chat import master_chat,driver


# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# driver = webdriver.Chrome("drivers/chromedriver",options=chrome_options)
if not os.path.exists("./audio"):
    os.mkdir("./audio")
if not os.path.exists("./images"):
    os.mkdir("./images")

path, dirs, files = next(os.walk("./images"))
image_count = len(files)

while 1:
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Say something")
    #     audio = r.listen(source, timeout=10)
    #     print("Time over")
    try:
        # text = r.recognize_google(audio)
        text=input()
    except:
        continue
    print("Text :"+text)
    if "where to watch" in text:
        text=text.replace("where to watch","")
        text2="https://www.justwatch.com/in/search?q="
        text=text.replace(" ","%20")
        text2+=text
        webbrowser.open_new_tab(text2)
    elif "suggest movie" in text:
        speech=gTTS("What genre do you want?",lang='en',slow=False)
        speech.save("speech_default.mp3")
        playsound.playsound("speech_default.mp3",True)
        s=sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak")
            audio=s.listen(source)
            print("Over")
        text=s.recognize_google(audio)
        # text=input()
        text2="agoodmovietowatch.com"
        text=text+" movie "+text2
        for j in search(text, tld="co.in", num=10,stop=10,pause=2):
            if "agoodmovietowatch.com" in j:
                webbrowser.open_new_tab(j)
                break
    elif "stock price" in text:
        for j in search(text, tld="co.in", num=10, stop=10, pause=2):
            if "moneycontrol.com" in j:
                webbrowser.open_new_tab(j)
                break
    elif "translate" in text:
        text=text.replace("translate",'')
        speech=gTTS("What language should I translate to?",lang='en',slow=False)
        os.remove("speech_default.mp3")
        speech.save("speech_default.mp3")
        playsound.playsound("speech_default.mp3",True)
        language=input()
        # s=sr.Recognizer()
        # with sr.Microphone() as source:
        #     print("Say something")
        #     audio=s.listen(source)
        # print("Time over")
        # language=s.recognize_google(audio)
        language=language[0].lower()+language[1:]
        print(language)
        if language=="chinese" or language=="chinese simplified":
            language="chinese (simplified)"
        elif language=="chinese traditional":
            language="chinese (traditional)"
        trans=Translator()                                  #translator object
        res=trans.translate(text,language)
        print(res.text)
        language=googletrans.LANGCODES[language]
        speech=gTTS(text=res.text,lang=language,slow=False)
        os.remove("speech.mp3")
        speech.save("speech.mp3")
        playsound.playsound("speech.mp3")
    elif "repeat after me" in text:
        text=text[16:]
        speak=gTTS(text=text,lang='en',slow=False)
        speak.save("speech.mp3")
        playsound.playsound("speech.mp3",True)
    elif "convert" in text:
        print("What would you like to convert?")
        print("1. doc to pdf")
        print("2. pdf to doc")
        print("3. Image format conversion")
        choice=int(input())
        if choice==1:
            print("1. Convert docx file")
            print("2. Convert all docx files in a folder")
            ch=int(input())
            if ch==1:
                inside=input("Enter file name")
                outside=input("What would you like to name output file?")
                inside+=".docx"
                outside+=".pdf"
                convert(inside,outside)
                subprocess.Popen('explorer "C:\path\of\folder"')
            else:
                inside=input("Enter folder path")
                convert(inside)
                subprocess.Popen('explorer '+'"'+inside+'"')
        elif choice==3:
                inside=input("Enter input image with extension: ")
                outside=input("Enter output image with extension: ")
                inside = r"{}".format(inside)
                outside = r"{}".format(outside)
                img = Image.open(inside)
                img.save(outside)
    elif "compress" in text:
        print("Select compression format:")
        print("1. .tar.gz")
        print("2. .zip")
        choice=int(input())
        if choice==1:
            inside=input("Enter path with file extension: ")
            outside=input("Enter output file name: ")
            outside+=".tar.gz"
            inside = r"{}".format(inside)
            with tarfile.open(outside,"w:gz") as tar:
                tar.add(inside, arcname=os.path.basename(inside))
            tar.close()
        elif choice==2:
            inside=input("Enter path with file extension: ")
            outside=input("Enter output path with file extension: ")
            inside = r"{}".format(inside)
            comp= zipfile.ZipFile(outside, 'w')
            comp.write(inside,arcname=os.path.basename(inside), compress_type=zipfile.ZIP_DEFLATED)
            comp.close()
    elif "wikipedia" in text:
        flag=False
        text=text.replace("search on wikipedia","")
        text=text.replace("on wikipedia","")
        text=text.replace("wikipedia","")
        for j in search(text, tld="co.in", num=10,stop=10,pause=2):
            print(j)
            if "en.wikipedia.org" in j:
                webbrowser.open_new_tab(j)
                flag=True
                break
        if flag==False:
            text = text.replace(' ', '+')
            URL = f"https://google.com/search?q={text}"
            webbrowser.open_new_tab(URL)
    elif "chat mode" in text:
        # system("clear")
        master_chat()
    elif "news" in text:
        print("Fetching News....Please Wait")
        data = tweets(1, "EconomicTimes")
        speak = ""
        for i in data:
            speak += i.text
        speak = speak.replace("#", "")
        speak = gTTS(text=speak, lang='en', slow=False)
        speak.save("./audio/news.mp3")
        os.chdir("./audio/")
        os.system("news.mp3")
        os.chdir("../")
        continue
    elif text=="go to sleep":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "camera" in text:
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")
        while True:
            ret, frame = cam.read()
            cv2.imshow("test", frame)
            if not ret:
                break
            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "./images/opencv_frame_{}.png".format(image_count)
                cv2.imwrite(img_name, frame)
                print("{} saved!".format(img_name))
                image_count += 1
        cam.release()
        cv2.destroyAllWindows()
    elif "exit" in text:
        print("GoodBye")
        break
    else:
        text = text.replace('+', '%2B')
        text = text.replace(' ', '+')
        URL = f"https://google.com/search?q={text}"
        data=[]
        driver.get(URL)
        content=driver.page_source
        soup=BeautifulSoup(content,features='html.parser')
        try:
            # webbrowser.open_new_tab(URL)
            data=soup.find('div', attrs={'class':'ayqGOc kno-fb-ctx KBXm4e'})
            print(data.text)
            continue
        except:
            pass
        try:
            data=soup.findAll('div', attrs={'class':'thODed Uekwlc XpoqFe'})
            # res=(data.text).split(" ")
            count=0
            for i in data:
                if count>2:
                    break
                for j in range(2,len(i.text)):
                    if i.text[j]=='.':
                        break
                if i.text[0] not in ['1','2','3']:
                    print((count+1),end="")
                    print(". ",end="")
                if i.text[:j+1] != "":
                    print(i.text[:j+1])
                    flag=False
                else:
                    flag=True
                count+=1
                # print(i.text)
            if flag==False:
                continue
            else:
                pass
        except:
            pass
        try:
            data=soup.find('div', attrs={'class':'z7BZJb XSNERd'})
            res=(data.text).split(" ")
            print(res[1])
            continue
        except:
            pass
        try:
            data=soup.find('div', attrs={'class':'Z0LcW XcVN5d'})
            print(data.text)
            continue
        except:
            pass
        try:
            data=soup.find('div', attrs={'class':'Z0LcW XcVN5d AZCkJd'})
            print(data.text)
            continue
        except:
            pass
        try:
            webbrowser.open_new_tab(URL)
            continue
        except:
            pass
