from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import time


#taking input
print('Whats your question: ')
interested_question=input('>')
question=interested_question.replace(' ','+')

session = HTMLSession()
#creating path to destination page
folder_path='https://old.reddit.com/search?q='
path=folder_path+question+'&restrict_sr=&sort=relevance&t=all'

r = session.get(path)

r.html.render(sleep=1, timeout=35)

targetDivs= r.html.find('.contents')

#targeting wanted elements
Divsoup = BeautifulSoup(targetDivs[-1].html, features="html.parser")
headings=Divsoup.find_all('a',class_='search-title may-blank')

#printing using format string
for i in range(len(headings)):
    title=headings[i].text
    link=headings[i]['href']
    print(f'''HeadLine : {title}''')
    print(f'''Learn More: {link}''')


