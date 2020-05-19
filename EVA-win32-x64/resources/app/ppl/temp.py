from modules import*

text = input()
text = text.replace(' ', '+')
URL = f"https://www.google.co.in/search?q={text}"
driver = webdriver.Chrome("drivers/chromedriver.exe")
data = []
driver.get(URL)
content = driver.page_source
soup = BeautifulSoup(content, features='html.parser')
data = soup.find('div', attrs={'class': 'Z0LcW XcVN5d'})
print(data.text)
