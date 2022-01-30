import requests,datetime
from bs4 import BeautifulSoup

def homeareaScrape(url):
    try:
        # url = "https://www.worldometers.info/coronavirus/"
        req = requests.get(url)
        bsObj = BeautifulSoup(req.text, "html.parser")
        return bsObj
    except Exception as e: print(e)

print(homeareaScrape('https://www.homearea.com/place/abanda-cdp-alabama/0100100/'))