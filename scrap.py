#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import csv
import urllib
URL = "http://117.239.154.84:8001/ktuexam/index.html"
baseURL= "http://117.239.154.84:8001/ktuexam/"
# r = requests.get(URL)

soup = BeautifulSoup(requests.get(URL).content, 'html.parser')

links=[]
def scrap():
    for link in soup.find_all('a'):
        current_link = link.get('href')
        if current_link.endswith('FN.pdf') | current_link.endswith('AN.pdf') :
            finalurl = baseURL + urllib.parse.quote(current_link)
            return finalurl
