import requests, webbrowser
from bs4 import BeautifulSoup
link='https://www.google.com//search?q=weather+report+of+'
print('Enter the name of the city: ')
city=input()
link=link+city
htmlform=requests.get(link).text
print('\n\nGoogling......')
soupform=BeautifulSoup(htmlform,'lxml')
#print(soupform.prettify())
heading=soupform.find('div',class_="ZINbbc xpd O9g5cc uUPGi")
#print(heading.prettify())
weather=heading.find('div',class_="BNeawe iBp4i AP7Wnd")
if weather is None:
    print('''Error 404. Couldn't find the weather update of the city''')
else:
    weather=heading.find('div',class_="BNeawe iBp4i AP7Wnd").text
    time_and_condition=heading.find('div',class_="BNeawe tAd8D AP7Wnd").text
    print(weather)
    print(time_and_condition)

