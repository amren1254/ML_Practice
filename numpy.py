#This is a numpy tutorial script file where all the practice questions are solved.


#Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#set the url you want to scrap data from
url = 'http://web.mta.info/developers/turnstile.html'

#connect to the url
response = requests.get(url)

#parse html and save to beautiful soup object 
soup = BeautifulSoup(response.text, "html.parser")

#'a' tags for the links
soup.findAll('a')

#extract data for a single link
one_a_tag = soup.findAll('a')[36]
link = one_a_tag['href']
download_url = 'http://web.mta.info/developers/'+ link
print(urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]))
time.sleep(1)
