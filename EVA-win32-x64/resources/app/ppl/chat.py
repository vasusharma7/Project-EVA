import requests
from modules import *
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
if not os.path.exists("./audio"):
    os.mkdir("./audio")

# driver = webdriver.Chrome("C:/VIRUS/Projects/electron/bot/ppl/drivers/chromedriver.exe",
#                           chrome_options=chrome_options)

url = "http://3.87.126.120:7000/response?question="


# def chat_response(query="", initialise=False):
#     if initialise:
#         time.sleep(5)
#         res = driver.find_elements_by_xpath(
#             '/html/body/form/table/tbody/tr[3]/td[2]')[0].text
#         return res
#     else:
#         inp = driver.find_element_by_name('ENTRY')
#         inp.send_keys(query)
#         inp.send_keys(Keys.ENTER)
#         time.sleep(3)
#         res = driver.find_elements_by_xpath(
#             '/html/body/form/table/tbody/tr[3]/td[2]')[0].text
#         if "elbot" in res.lower():
#             res = res[:res.find("Elbot")] + "VVS" + res[res.find("Elbot")+5:]
#         return res


# driver.get("http://elbot-e.artificial-solutions.com/cgi-bin/elbot.cgi")
# driver.find_element_by_class_name("pb-widget__description__chat-now__button").click()
# time.sleep(5)
# print(chat_response(initialise=True))
# system("cls")
try:
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Chat with me !!")
        playsound.playsound("./audio/init_beep.mp3",True)
        audio = r.listen(source)
        playsound.playsound("./audio/end_beep.mp3",True)
        print("Times Up !!")
    try:
        text = r.recognize_google(audio)
        print("Text : " + text)
    except:
        sys.exit(0)

    if "exit" in text:
        sys.exit(0)
    else:
        payload = url + text
        response = requests.get(payload)
        try:
            response = json.loads(
                str(response.__dict__['_content'].decode("utf-8")))

            # print("From Model : ", end=" ")
            print(response['answer'])
            speech = gTTS(response['answer'], lang='en', slow=False)
            if(os.path.exists("./audio/chat_default.mp3")):
                os.remove("./audio/chat_default.mp3")
            speech.save("./audio/chat_default.mp3")
            playsound.playsound("./audio/chat_default.mp3", True)
        except json.decoder.JSONDecodeError:
            print(str(response.__dict__['_content'].decode("utf-8")))
except:
    print("Something went wrong")
    pass
