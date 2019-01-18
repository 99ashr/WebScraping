#!/usr/bin/python3

#!!!import urllib!!!
import urllib.request as req

#!!!import beautifulsoup!!!
from bs4 import BeautifulSoup

#!!!url of the link!!!

link = "https://secure.php.net/"
#dir(link)

webpage = req.urlopen(link)
#dir(webpage)

tags= BeautifulSoup(webpage,'html.parser')

#print(tags.prettify)

a=tags.title.text
#b=tags.title.strings
#c=tags.title.string

#print(a)

#dir(tags)

div_blurb=tags.find('div', class_='blurb')


#tags.getText(" ")
#print(div_blurb)

div_text=div_blurb.get_text()

#all_text=tags.get_text()

file = open("scrapped_data", "w")
file.write(a)
file.write(div_text)
file.close()