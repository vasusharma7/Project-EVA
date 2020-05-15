import requests
from modules import *
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome("./drivers/chromedriver.exe",
                          chrome_options=chrome_options)

url = "http://3.87.126.120:7000/response?question="


def chat_response(query="", initialise=False):
    if initialise:
        time.sleep(5)
        res = driver.find_elements_by_xpath(
            '/html/body/form/table/tbody/tr[3]/td[2]')[0].text
        return res
    else:
        inp = driver.find_element_by_name('ENTRY')
        inp.send_keys(query)
        inp.send_keys(Keys.ENTER)
        time.sleep(3)
        res = driver.find_elements_by_xpath(
            '/html/body/form/table/tbody/tr[3]/td[2]')[0].text
        if "elbot" in res.lower():
            res = res[:res.find("Elbot")] + "VVS" + res[res.find("Elbot")+5:]
        return res


def master_chat():
    print("Preparing Chat Engine : ")

    driver.get("http://elbot-e.artificial-solutions.com/cgi-bin/elbot.cgi")
    # driver.find_element_by_class_name("pb-widget__description__chat-now__button").click()
    time.sleep(5)
    print(chat_response(initialise=True))
    system("cls")
    print("I am ready..")
    r = sr.Recognizer()
    while 1:
        with sr.Microphone() as source:
            print("Say something")
            audio = r.listen(source)
            print("Times Up !!")
        try:
            text = r.recognize_google(audio)
        except:
            continue
        print("Text : " + text)
        if "exit" in text:
            return
        else:
            payload = url + text
            response = requests.get(payload)
            try:
                response = json.loads(
                    str(response.__dict__['_content'].decode("utf-8")))
                if response['score'] > 0:
                    print("From Model : ", end=" ")
                    print(response['answer'])
                else:
                    print("From Web : ", end=" ")
                    print(chat_response(query=text))
            except json.decoder.JSONDecodeError:
                print(str(response.__dict__['_content'].decode("utf-8")))


if __name__ == "__main__":
    master_chat()
