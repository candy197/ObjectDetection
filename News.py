from bs4 import BeautifulSoup
import requests
import pyttsx3
def speak(tell):
	engine = pyttsx3.init()
	engine.say(str(tell))    
	engine.runAndWait()

res = requests.get('https://www.indiatoday.in/top-stories')
soup = BeautifulSoup(res.text, 'lxml')


news_box = soup.find_all('div', {'class': 'detail'})


for news in news_box:	
    print(news.text)
    speak(news.text)
    print()
   
    
