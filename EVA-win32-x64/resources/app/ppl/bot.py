# from googlesearch import search
import random
from modules import *
from tkinter import *
import tkinter.messagebox
import tkinter as tk
from tkinter import *
from tkinter import filedialog  # from googlesearch import search
from tkinter import filedialog
import wolframalpha
import shutil
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from PIL import Image
# print(1)
# print(1)
# print(1)
# print(os.path.join(os.getcwd(), "resources/app/ppl/drivers/chromedriver.exe"))
# sys.exit(0)

# print(1)
# print(1)
# print(1)
# print(os.getcwd())
# sys.exit(0)



def image_conversion():
    root = tk.Tk()

    def my_function():
        current_id = variable.get()
        output_format = str(current_id)
        inside = root.filename
        for i in range(len(inside)):
            if inside[i] == '/':
                index = i
            if inside[i] == '.':
                index2 = i
        output = inside[:index]
        outside = inside[:index2]
        outside += output_format
        inside = r"{}".format(inside)
        outside = r"{}".format(outside)
        img = Image.open(inside)
        new_i = img.convert('RGB')
        new_i.save(outside)
        root.destroy()
        os.startfile(output)

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    root.filename = filedialog.askopenfilename(
        initialdir=desktop, title="Select A File")
    print(root.filename)
    my_label = tk.Label(root, text="Select output image format")
    my_label.config(width=25, font=('Helvetica,12'))
    my_label.grid(row=0, column=0)

    OptionList = [".jpg", ".png", ".tiff", ".bmp", ".eps"]
    variable = tk.StringVar(root)
    variable.set(OptionList[0])
    opt = tk.OptionMenu(root, variable, *OptionList)
    opt.config(width=50, font=('Helvetica', 12))
    opt.grid(row=2, column=0)

    my_button = tk.Button(root, text="Submit", command=my_function)
    my_button.config(width=10, font=('Helvetica,12'))
    my_button.grid(row=4, column=0)

    root.mainloop()
class ttt(object):
    def __init__(self, tk):
        self.tk = tk
        self.tk.title("Tic-Tac-Toe")

        self.playera = StringVar()
        self.playerb = StringVar()
        self.p1 = StringVar(value = "Player 1")
        self.p2 = StringVar(value = "Player 2")

        self.player1_name = Entry(self.tk, textvariable=self.p1, bd=2)
        self.player1_name.grid(row=1, column=1, columnspan=8)
        self.player2_name = Entry(self.tk, textvariable=self.p2, bd=2)
        self.player2_name.grid(row=2, column=1, columnspan=8)

        self.cross = PhotoImage(file = 'cross.png')
        self.zero = PhotoImage(file = 'zero.png')

        self.bclick = True
        self.flag = 0
        self.buttons = StringVar()

        self.label = Label(self.tk, text="Player 1:", font='Comic 15 bold', fg='black', height=1, width=8)
        self.label.grid(row=1, column=0)

        self.label = Label(self.tk, text="Player 2:", font='Comic 15 bold', fg='black', height=1, width=8)
        self.label.grid(row=2, column=0)

        self.button1 = Button(self.tk, text = ' ', font='Times 20 bold', bg='#00bfff',height=4, width=8, command=lambda: self.btnClick(self.button1))
        self.button1.grid(row=3, column=0)

        self.button2 = Button(self.tk, text=' ', font='Times 20 bold', bg='#ffff66', height=4, width=8, command=lambda: self.btnClick(self.button2))
        self.button2.grid(row=3, column=1)

        self.button3 = Button(self.tk, text=' ',font='Times 20 bold', bg='#00bfff', height=4, width=8, command=lambda: self.btnClick(self.button3))
        self.button3.grid(row=3, column=2)

        self.button4 = Button(self.tk, text=' ', font='Times 20 bold', bg='#ffff66', height=4, width=8, command=lambda: self.btnClick(self.button4))
        self.button4.grid(row=4, column=0)

        self.button5 = Button(self.tk, text=' ', font='Times 20 bold', bg='#00bfff', height=4, width=8, command=lambda: self.btnClick(self.button5))
        self.button5.grid(row=4, column=1)

        self.button6 = Button(self.tk, text=' ', font='Times 20 bold', bg='#ffff66', height=4, width=8, command=lambda: self.btnClick(self.button6))
        self.button6.grid(row=4, column=2)

        self.button7 = Button(self.tk, text=' ', font='Times 20 bold', bg='#00bfff', height=4, width=8, command=lambda: self.btnClick(self.button7))
        self.button7.grid(row=5, column=0)

        self.button8 = Button(self.tk, text=' ', font='Times 20 bold', bg='#ffff66', height=4, width=8, command=lambda: self.btnClick(self.button8))
        self.button8.grid(row=5, column=1)

        self.button9 = Button(self.tk, text=' ', font='Times 20 bold', bg='#00bfff', height=4, width=8, command=lambda: self.btnClick(self.button9))
        self.button9.grid(row=5, column=2)


    def disableButton(self):
        self.button1.configure(state=DISABLED)
        self.button2.configure(state=DISABLED)
        self.button3.configure(state=DISABLED)
        self.button4.configure(state=DISABLED)
        self.button5.configure(state=DISABLED)
        self.button6.configure(state=DISABLED)
        self.button7.configure(state=DISABLED)
        self.button8.configure(state=DISABLED)
        self.button9.configure(state=DISABLED)

    def btnClick(self, buttons):
        if buttons['text'] == " " and self.bclick == True:
            buttons['image'] = self.zero
            buttons['text'] = 'X'
            buttons['height'] = 141
            buttons['width'] = 131
            self.bclick = False
            self.playerb = self.p2.get() + " Won!"
            self.playera = self.p1.get() + " Won!"
            self.checkForWin()
            self.flag += 1

        elif buttons['text'] == " " and self.bclick == False:
            buttons['image'] = self.cross
            buttons['text'] = 'O'
            buttons['height'] = 141
            buttons['width'] = 131
            self.bclick = True
            self.checkForWin()
            self.flag += 1
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already clicked!")

    def checkForWin(self):
        if (self.button1['text'] == 'X' and self.button2['text'] == 'X' and self.button3['text'] == 'X' or
            self.button4['text'] == 'X' and self.button5['text'] == 'X' and self.button6['text'] == 'X' or
            self.button7['text'] == 'X' and self.button8['text'] == 'X' and self.button9['text'] == 'X' or
            self.button1['text'] == 'X' and self.button5['text'] == 'X' and self.button9['text'] == 'X' or
            self.button3['text'] == 'X' and self.button5['text'] == 'X' and self.button7['text'] == 'X' or
            self.button1['text'] == 'X' and self.button4['text'] == 'X' and self.button7['text'] == 'X' or
            self.button2['text'] == 'X' and self.button5['text'] == 'X' and self.button8['text'] == 'X' or
            self.button3['text'] == 'X' and self.button6['text'] == 'X' and self.button9['text'] == 'X'):
            self.disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", self.playera)

        elif(self.flag == 8):
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It's a Tie!")

        elif(self.button1['text'] == 'O' and self.button2['text'] == 'O' and self.button3['text'] == 'O' or
            self.button4['text'] == 'O' and self.button5['text'] == 'O' and self.button6['text'] == 'O' or
            self.button7['text'] == 'O' and self.button8['text'] == 'O' and self.button9['text'] == 'O' or
            self.button1['text'] == 'O' and self.button5['text'] == 'O' and self.button9['text'] == 'O' or
            self.button3['text'] == 'O' and self.button5['text'] == 'O' and self.button7['text'] == 'O' or
            self.button1['text'] == 'O' and self.button4['text'] == 'O' and self.button7['text'] == 'O' or
            self.button2['text'] == 'O' and self.button5['text'] == 'O' and self.button8['text'] == 'O' or
            self.button3['text'] == 'O' and self.button6['text'] == 'O' and self.button9['text'] == 'O'):
            self.disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", self.playerb)

if not os.path.exists("./audio"):
    os.mkdir("./audio")
if not os.path.exists("./images"):
    os.mkdir("./images")

path, dirs, files = next(os.walk("./images"))
image_count = len(files)

r = sr.Recognizer()
with sr.Microphone() as source:
    playsound.playsound("./audio/init_beep.mp3", True)
    print("Say something")
    audio = r.listen(source)
    print("Time over")
    playsound.playsound("./audio/end_beep.mp3", True)
try:
    text = r.recognize_google(audio)
    text = text.lower()
except:
    print("Something went wrong")
    sys.exit(0)
print("Text :"+text)
if "where to watch" in text:
    text = text.replace("where to watch", "")
    text2 = "https://www.justwatch.com/in/search?q="
    text = text.replace(" ", "%20")
    text2 += text
    webbrowser.open_new_tab(text2)
elif text=="weather forecast":
    for j in search(text, tld="co.in", num=10, stop=10, pause=2):
        if "accuweather" in j:
            webbrowser.open_new_tab(j)
            sys.exit(0)
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
        playsound.playsound("./audio/init_beep.mp3", True)
        audio = s.listen(source)
        playsound.playsound("./audio/end_beep.mp3", True)
    text = s.recognize_google(audio)
    # text=input()
    text2 = "agoodmovietowatch.com"
    text = text+" movie "+text2
    for j in search(text, tld="co.in", num=10, stop=10, pause=2):
        if "mood" or "genre" in j:
            webbrowser.open_new_tab(j)
            sys.exit(0)
elif "stock price" in text:
    for j in search(text, tld="co.in", num=10, stop=10, pause=2):
        if "moneycontrol.com" in j:
            webbrowser.open_new_tab(j)
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
        playsound.playsound("./audio/init_beep.mp3", True)
        audio = s.listen(source)
        playsound.playsound("./audio/end_beep.mp3", True)
    try:
        language = s.recognize_google(audio)
    except:
        speech = gTTS("Language Could Not Be Recognized",
                      lang='en', slow=False)
        speech.save("./audio/failed.mp3")
        playsound.playsound("./audio/failed.mp3", True)
        print("Language Could Not Be Recognized")
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
    sys.exit(0)
elif "repeat after me" in text:
    text = text[16:]
    speak = gTTS(text=text, lang='en', slow=False)
    speak.save("./audio/speech.mp3")
    playsound.playsound("./audio/speech.mp3", True)
    os.remove("./audio/speech.mp3")
elif "convert to pdf" in text:
    Tk().withdraw()
    inside = askopenfilename()
    outside = inside[:len(inside)-4]
    outside += "pdf"
    convert(inside, outside)
    for i in range(len(inside)):
        if inside[i] == '/':
            index = i
    os.startfile(inside[:index])
elif "convert image" in text:
    image_conversion()
elif "compress file" in text:
    Tk().withdraw()
    inside = askopenfilename()
    for i in range(len(inside)):
        if inside[i] == '.':
            index = i
        if inside[i] == '/':
            index2 = i
    output = inside[:index2]
    output += '//'
    name = inside[index2+1:index]
    inside = inside[index2+1:]
    shutil.make_archive(output+name, 'tar', output, inside)
    os.startfile(output)
    speak = gTTS(text="The file is compressed", lang='en', slow=False)
    speak.save("./audio/compress.mp3")
    playsound.playsound("./audio/compress.mp3", True)
    os.remove("./audio/compress.mp3")
elif "compress folder" in text:
    root = Tk()
    root.withdraw()
    inside = filedialog.askdirectory()
    for i in range(len(inside)):
        if inside[i] == '/':
            index2 = i
    outside = inside
    inside = r"{}".format(inside)
    shutil.make_archive(outside, 'zip', inside)
    os.startfile(inside[:index2])
elif "game" in text:
    tk = Tk()
    p = ttt(tk)
    tk.mainloop()
elif "dice" in text:
    num = str(random.randint(1, 6))
    playsound.playsound("dice.wav", True)
    speak = gTTS(text="You rolled a " + num, lang='en', slow=False)
    try:
        os.remove("speech.mp3")
    except FileNotFoundError:
        print(
            "FileNotFoundError: The system cannot find the file specified: 'speech.mp3'")
    speak.save("speech.mp3")
    playsound.playsound("speech.mp3", True)
elif "coin" in text:
    flip = random.randint(0, 1)
    if flip == 0:
        text = "heads"
    elif flip == 1:
        text = "tails"
    playsound.playsound("coin.mp3", True)
    speak = gTTS(text="You got " + text, lang='en', slow=False)
    try:
        os.remove("speech.mp3")
    except FileNotFoundError:
        print(
            "FileNotFoundError: The system cannot find the file specified: 'speech.mp3'")
    speak.save("speech.mp3")
    playsound.playsound("speech.mp3", True)
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
            #driver
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
    #driver
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
            #driver
            sys.exit(0)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            #driver
            sys.exit(0)
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "./images/opencv_frame_{}.png".format(image_count)
            cv2.imwrite(img_name, frame)
            print("{} saved!".format(img_name))
            image_count += 1
    cam.release()
    cv2.destroyAllWindows()
elif "login to gmail" in text:
    details = cred("gmail")
    email = details[0]
    pwd = details[1]

    driver = webdriver.Chrome("./drivers/chromedriver.exe")
    driver.get("https://www.gmail.com")
    driver.find_element_by_xpath(
        "//*[@id='identifierId']").send_keys(email)
    driver.find_element_by_xpath(
        "//*[@id='identifierNext']/span/span").click()

    # driver.implicitly_wait(20)

    password = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")))
    password.send_keys(pwd)
    driver.find_element_by_xpath(
        "//*[@id='passwordNext']/span/span").click()
    os.system('cls')
elif "login to moodle" in text:
    details = cred("moodle")
    uname = details[0]
    pwd = details[1]

    driver = webdriver.Chrome("./drivers/chromedriver.exe")
    driver.get("https://moodle.coep.org.in/moodle/login/index.php")
    driver.find_element_by_xpath("//*[@id='username']").send_keys(uname)

    # driver.implicitly_wait(20)

    password = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='password']")))
    password.send_keys(pwd)
    driver.find_element_by_xpath("//*[@id='loginbtn']").click()
    os.system('cls')
elif "login to instagram" in text:
    details = cred("instagram")
    uname = details[0]
    pwd = details[1]

    driver = webdriver.Chrome("./drivers/chromedriver.exe")
    driver.get("https://www.instagram.com/accounts/login/")
    username = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")))
    username.send_keys(uname)

    # driver.implicitly_wait(20)

    password = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")))
    password.send_keys(pwd)
    driver.find_element_by_xpath(
        "//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]").click()
    os.system('cls')
elif "login to facebook" in text:
    details = cred("facebook")
    email = details[0]
    pwd = details[1]
    driver = webdriver.Chrome("./drivers/chromedriver.exe")
    driver.get("https://m.facebook.com/")
    driver.find_element_by_xpath(
        "//*[@id='m_login_email']").send_keys(email)

    # driver.implicitly_wait(20)

    password = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='m_login_password']")))
    password.send_keys(pwd)
    driver.find_element_by_xpath("//*[@id='u_0_4']/button").click()
    os.system('cls')
elif "login to twitter" in text:
    details = cred("twitter")
    email = details[0]
    pwd = details[1]
    driver = webdriver.Chrome("./drivers/chromedriver.exe")
    driver.get("https://twitter.com/login")
    username = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input")))
    username.send_keys(email)

    # driver.implicitly_wait(20)

    password = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input")))
    password.send_keys(pwd)
    driver.find_element_by_xpath(
        "//*[@id='react-root']/div/div/div[2]/main/div/div/form/div/div[3]/div/div/span/span").click()
    os.system('cls')
elif "login to amazon" in text:
    details = cred("amazon")
    email = details[0]
    pwd = details[1]
    driver = webdriver.Chrome("./drivers/chromedriver.exe")
    driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
    driver.find_element_by_xpath("//*[@id='ap_email']").send_keys(email)
    driver.find_element_by_xpath("//*[@id='continue']").click()

    # driver.implicitly_wait(20)

    password = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='ap_password']")))
    password.send_keys(pwd)
    driver.find_element_by_xpath("//*[@id='signInSubmit']").click()
    os.system('cls')
elif "login to prime" in text:
    details = cred("prime")
    email = details[0]
    pwd = details[1]
    driver = webdriver.Chrome("./drivers/chromedriver.exe")
    driver.get("https://www.amazon.com/ap/signin?accountStatusPolicy=P1&clientContext=257-9778690-6286354&language=en_US&openid.assoc_handle=amzn_prime_video_mobile_us&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_encoding%3DUTF8%26location%3D%252Fref%253Dav_nav_sign_in")
    driver.find_element_by_xpath("//*[@id='ap_email']").send_keys(email)

    # driver.implicitly_wait(20)

    password = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='ap_password']")))
    password.send_keys(pwd)
    driver.find_element_by_xpath("//*[@id='signInSubmit']").click()
    os.system('cls')
elif "login to netflix" in text:
    details = cred("netflix")
    email = details[0]
    pwd = details[1]
    driver = webdriver.Chrome("./drivers/chromedriver.exe")
    driver.get("https://www.netflix.com/in/login")
    driver.find_element_by_xpath(
        "//*[@id='id_userLoginId']").send_keys(email)

    # driver.implicitly_wait(20)

    password = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='id_password']")))
    password.send_keys(pwd)
    driver.find_element_by_xpath(
        "//*[@id='appMountPoint']/div/div[3]/div/div/div[1]/form/button").click()
    os.system('cls')
elif "login to linkedin" in text:
    details = cred("linkedin")
    email = details[0]
    pwd = details[1]
    driver = webdriver.Chrome("./drivers/chromedriver.exe")
    driver.get("https://www.linkedin.com/login")
    driver.find_element_by_xpath("//*[@id='username']").send_keys(email)

    # driver.implicitly_wait(20)

    password = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='password']")))
    password.send_keys(pwd)
    driver.find_element_by_xpath("//*[@type='submit']").click()
    os.system('cls')
elif "login to github" in text:
    details = cred("github")
    email = details[0]
    pwd = details[1]
    driver = webdriver.Chrome("./drivers/chromedriver.exe")
    driver.get("https://github.com/login")
    driver.find_element_by_xpath("//*[@id='login_field']").send_keys(email)

    # driver.implicitly_wait(20)

    password = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='password']")))
    password.send_keys(pwd)
    driver.find_element_by_xpath(
        "//*[@id='login']/form/div[4]/input[9]").click()
    os.system('cls')
elif "calculate" in text:
    # Taking input from user
    #question = input('Question : ')
    app_id = "4LJ6P5-XH7TQG859X"
    # Instance of wolfram alpha client class
    client = wolframalpha.Client(app_id)
    try:
        res = client.query(text)
        # Includes only text from the response
        answer = next(res.results).text
    except:
        print("Sorry, the assistant doesn't understand your query")
    else:
        print("Answer : " + answer)
elif "exit" in text:
    print("GoodBye")
    #driver
    sys.exit(0)
else:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_experimental_option(`
    #     "prefs", {"profile.default_content_se`ttings.cookies": 2})
    driver = webdriver.Chrome(os.path.join(os.getcwd(), "resources/app/ppl/drivers/chromedriver.exe"),
                              chrome_options=chrome_options)
    # driver = webdriver.Chrome("./drivers/chromedriver.exe"),
    #                           chrome_options=chrome_options)
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
