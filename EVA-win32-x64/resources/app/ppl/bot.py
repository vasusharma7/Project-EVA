# from googlesearch import search
# print(1)
# print(1)
# print(1)
# print(os.getcwd())
# sys.exit(0
from modules import *
from twitter import tweets
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
prefs={"profile.managed_default_content_settings.images":2}
chrome_options.add_experimental_option("prefs",prefs)
# chrome_options.add_experimental_option(`
#     "prefs", {"profile.default_content_se`ttings.cookies": 2})
driver = webdriver.Chrome(os.path.join(os.getcwd(), "resources/app/ppl/drivers/chromedriver.exe"),
                          chrome_options=chrome_options)
# driver = webdriver.Chrome("./drivers/chromedriver.exe"),
#                           chrome_options=chrome_options)


def image_conversion():
    root = tk.Tk()
    def my_function():
        current_id = variable.get()
        output_format =str(current_id)
        inside=root.filename
        for i in range(len(inside)):
            if inside[i]=='/':
                index=i
            if inside[i]=='.':
                index2=i
        output=inside[:index]
        outside=inside[:index2]
        outside+=output_format
        inside = r"{}".format(inside)
        outside = r"{}".format(outside)
        img = Image.open(inside)
        new_i = img.convert('RGB')
        new_i.save(outside)
        root.destroy()
        os.startfile(output)

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    root.filename = filedialog.askopenfilename(initialdir=desktop, title="Select A File")
    print(root.filename)
    my_label = tk.Label(root, text = "Select output image format")
    my_label.config(width=25,font=('Helvetica,12'))
    my_label.grid(row = 0, column = 0)

    OptionList = [".jpg",".png",".tiff",".bmp",".eps"]
    variable = tk.StringVar(root)
    variable.set(OptionList[0])
    opt = tk.OptionMenu(root, variable, *OptionList)
    opt.config(width=50, font=('Helvetica', 12))
    opt.grid(row = 2, column = 0)

    my_button = tk.Button(root, text = "Submit", command = my_function)
    my_button.config(width=10,font=('Helvetica,12'))
    my_button.grid(row = 4, column = 0)

    root.mainloop()

if not os.path.exists("./audio"):
    os.mkdir("./audio")
if not os.path.exists("./images"):
    os.mkdir("./images")

path, dirs, files = next(os.walk("./images"))
image_count = len(files)

r = sr.Recognizer()
with sr.Microphone() as source:
    playsound.playsound("./audio/init_beep.mp3",True)
    print("Say something")
    audio = r.listen(source)
    print("Time over")
    playsound.playsound("./audio/end_beep.mp3",True)
try:
    text = r.recognize_google(audio)
    text = text.lower()
except:
    print("Something went wrong")
    driver.quit()
    sys.exit(0)
print("Text :"+text)
if "where to watch" in text:
    text = text.replace("where to watch", "")
    text2 = "https://www.justwatch.com/in/search?q="
    text = text.replace(" ", "%20")
    text2 += text
    webbrowser.open_new_tab(text2)
elif "suggest movie" in text:
    speech = gTTS("What genre do you want?", lang='en', slow=False)
    speech.save("./audio/speech_default.mp3")
    playsound.playsound("./audio/speech_default.mp3", True)
    os.remove('./audio/speech_default.mp3')
    s = sr.Recognizer()
    # print("Speak")
    # speech = gTTS("speak",
    #               lang='en', slow=False)
    # speech.save("./audio/speak.mp3")
    # speech = gTTS("over",
    #               lang='en', slow=False)
    # speech.save("./audio/over.mp3")
    with sr.Microphone() as source:
        # playsound.playsound("./audio/speak.mp3")
        # os.remove("./audio/speak.mp3")
        playsound.playsound("./audio/init_beep.mp3",True)
        audio = s.listen(source)
        playsound.playsound("./audio/end_beep.mp3",True)
    text = s.recognize_google(audio)
    # text=input()
    text2 = "agoodmovietowatch.com"
    text = text+" movie "+text2
    for j in search(text, tld="co.in", num=10, stop=10, pause=2):
        if "mood" or "genre" in j:
            webbrowser.open_new_tab(j)
            driver.quit()
            sys.exit(0)
elif "stock price" in text:
    for j in search(text, tld="co.in", num=10, stop=10, pause=2):
        if "moneycontrol.com" in j:
            webbrowser.open_new_tab(j)
            driver.quit()
            sys.exit(0)
elif "translate" in text:
    text = text.replace("translate", '')
    speech = gTTS("Which language should I translate to?",
                  lang='en', slow=False)
    speech.save("./audio/ask_language.mp3")
    playsound.playsound("./audio/ask_language.mp3", True)
    os.remove("./audio/ask_language.mp3")
    # language=input()
    s = sr.Recognizer()
    with sr.Microphone() as source:
        playsound.playsound("./audio/init_beep.mp3",True)
        audio = s.listen(source)
        playsound.playsound("./audio/end_beep.mp3",True)
    try:
        language = s.recognize_google(audio)
    except:
        speech = gTTS("Language Could Not Be Recognized",
                      lang='en', slow=False)
        speech.save("./audio/failed.mp3")
        playsound.playsound("./audio/failed.mp3", True)
        print("Language Could Not Be Recognized")
        driver.quit()
        sys.exit(0)
    language = language[0].lower()+language[1:]
    if language == "chinese" or language == "chinese simplified":
        language = "chinese (simplified)"
    elif language == "chinese traditional":
        language = "chinese (traditional)"
    try:
        trans = Translator()  # translator object
        res = trans.translate(text, language)
        print(res.text)
        language = googletrans.LANGCODES[language]
        speech = gTTS(text=res.text, lang=language, slow=False)
        speech.save("./audio/speech.mp3")
        playsound.playsound("./audio/speech.mp3")
        os.remove("./audio/speech.mp3")
    except:
        speech = gTTS("Something went wrong", slow=False)
        speech.save("./audio/wrong.mp3")
        playsound.playsound("./audio/wrong.mp3")
    driver.quit()
    sys.exit(0)
elif "repeat after me" in text:
    text = text[16:]
    speak = gTTS(text=text, lang='en', slow=False)
    speak.save("./audio/speech.mp3")
    playsound.playsound("./audio/speech.mp3", True)
    os.remove("./audio/speech.mp3")
elif "convert to pdf" in text:
    Tk().withdraw()
    inside= askopenfilename()
    outside=inside[:len(inside)-4]
    outside+="pdf"
    convert(inside,outside)
    for i in range(len(inside)):
        if inside[i]=='/':
            index=i
    os.startfile(inside[:index])
elif "convert image" in text:
    image_conversion()
elif "compress file" in text:
    Tk().withdraw()
    inside= askopenfilename()
    for i in range(len(inside)):
        if inside[i]=='.':
            index=i
        if inside[i]=='/':
            index2=i
    output=inside[:index2]
    output+='//'
    name=inside[index2+1:index]
    inside=inside[index2+1:]
    shutil.make_archive(output+name,'tar',output,inside)
    os.startfile(output)
elif "compress folder":
    root = Tk()
    root.withdraw()
    inside = filedialog.askdirectory()
    for i in range(len(inside)):
        if inside[i]=='/':
            index2=i
    outside=inside
    inside = r"{}".format(inside)
    shutil.make_archive(outside, 'zip',inside)
    os.startfile(inside[:index2])
elif "wikipedia" in text:
    flag = False
    text = text.replace("search on wikipedia", "")
    text = text.replace("on wikipedia", "")
    text = text.replace("wikipedia", "")
    for j in search(text, tld="co.in", num=10, stop=10, pause=2):
        print(j)
        if "en.wikipedia.org" in j:
            webbrowser.open_new_tab(j)
            flag = True
            driver.quit()
            sys.exit(0)
    if flag == False:
        text = text.replace(' ', '+')
        URL = f"https://google.com/search?q={text}"
        webbrowser.open_new_tab(URL)

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
    playsound.playsound("news.mp3")
    os.chdir("../")
    driver.quit()
    sys.exit(0)
elif text == "go to sleep":
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
elif "camera" in text:
    speak = gTTS(text="opening camera", lang='en', slow=False)
    speak.save("./audio/cam.mp3")
    playsound.playsound("./audio/cam.mp3")
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            driver.quit()
            sys.exit(0)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            driver.quit()
            sys.exit(0)
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
    driver.quit()
    sys.exit(0)
else:
    def method1():
        try:
            # webbrowser.open_new_tab(URL)
            data = soup.find(
                'div', attrs={'class': 'ayqGOc kno-fb-ctx KBXm4e'})
            print(data.text)
            speak = gTTS(text=data.text, lang='en', slow=False)
            speak.save("./audio/gogole.mp3")
            playsound.playsound("./audio/gogole.mp3", True)
            driver.quit()
        except:
            return False
        return True

    def method2():
        try:
            data = soup.findAll('div', attrs={'class': 'thODed Uekwlc XpoqFe'})
            # res=(data.text).split(" ")
            count = 0
            for i in data:
                if count > 2:
                    break
                for j in range(2, len(i.text)):
                    if i.text[j] == '.':
                        break
                # if i.text[0] not in ['1', '2', '3']:
                #     print((count+1), end="")
                #     print(". ", end="")
                if i.text[:j+1] != "":
                    print(i.text[:j+1])
                    speak = gTTS(text=i.text[:j+1], lang='en', slow=False)
                    speak.save("./audio/google.mp3")
                    playsound.playsound("./audio/google.mp3", True)
                    os.remove('./audio/google.mp3')
                    flag = False
                else:
                    flag = True
                count += 1
                driver.quit()
                sys.exit(0)
            if flag == False:
                driver.quit()
                sys.exit(0)
            else:
                return True
        except:
            return False

    def method3():
        try:
            data = soup.find('div', attrs={'class': 'z7BZJb XSNERd'})
            res = (data.text).split(" ")
            print(res[1])
            speak = gTTS(text=res[1], lang='en', slow=False)
            speak.save("./audio/google.mp3")
            playsound.playsound("./audio/google.mp3", True)
            os.remove('./audio/google.mp3')
            driver.quit()
        except:
            return False
        return True

    def method4():
        try:
            data = soup.find('div', attrs={'class': 'Z0LcW XcVN5d'})
            print(data.text)
            speak = gTTS(text=data.text, lang='en', slow=False)
            speak.save("./audio/google.mp3")
            playsound.playsound("./audio/google.mp3", True)
            os.remove('./audio/google.mp3')
            driver.quit()
        except:
            return False
        return True

    def method5():
        try:
            data = soup.find('div', attrs={'class': 'Z0LcW XcVN5d AZCkJd'})
            print(data.text)
            speak = gTTS(text=data.text, lang='en', slow=False)
            speak.save("./audio/google.mp3")
            playsound.playsound("./audio/google.mp3", True)
            os.remove('./audio/google.mp3')
            driver.quit()
        except:
            return False
        return True

    text = text.replace('+', '%2B')
    text = text.replace(' ', '+')
    URL = f"https://google.com/search?q={text}"
    data = []
    driver.get(URL)
    content = driver.page_source
    soup = BeautifulSoup(content, features='html.parser')
    if method1() or method2() or method3() or method4() or method5():
        pass
    else:
        webbrowser.open_new_tab(URL)
        driver.quit()
