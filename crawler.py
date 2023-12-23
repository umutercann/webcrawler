import requests
import webbrowser
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

linkler = []
executionTime = 0 

def openBrowser(urls):
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver=webdriver.Chrome(chrome_options)
    for val in urls:
        driver.get(val)
        time.sleep(1)
def extractLinks(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'xml')
        urls = [url.get_text() for url in soup.find_all('loc')]
    else:
        print('Failed to get the sitemap.')
    return urls
def main():
        start = time.time()
        for value in linkler:
            if "wp-sitemap" in value:
               siteurls=extractLinks(value)
               if "wp-sitemap" not in siteurls[0]:
                openBrowser(siteurls)
        end = time.time()
        global executionTime 
        executionTime = end-start
       
                
print('Linkleri girin: ')
linkler = list(map(str, input("Enter multiple values: ").split()))

while True: 
    main()
    print ("Process time: ", executionTime)    
    time.sleep(86400-executionTime)






