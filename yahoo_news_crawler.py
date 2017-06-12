#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
import time

### Get news categories on Yahoo News
req = requests.get('https://news.yahoo.com/')
soup = BeautifulSoup(req.text, 'lxml')

categories = []
for category in soup.select(".nr-applet-nav-item.nr-list-link.openSubNav"):
    categories.append(category.attrs['href'].strip('/').split('/')[3:len(category.attrs['href'])])
    print(category.attrs['href'].strip('/').split('/')[3:len(category.attrs['href'])])
    

def get_news_links(category):
    page_url = 'https://www.yahoo.com/{}'.format('/'.join(category))
    req = requests.get(page_url)
    soup = BeautifulSoup(req.text, 'lxml')

    return {urljoin(page_url, article.attrs['href']) for article in soup.select("#YDC-Stream > ul > li > div > div > div > h3 > a")}

def get_new_content(url):
    content = []
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    title = soup.select_one('#YDC-Side-Stack > div > div > div > div > div > div > header > h1')
    if title is not None:     
        content.append(title.text)
        for p in soup.select('#Col1-0-ContentCanvas > article > div > p'):
            content.append(p.text)
        return '\n'.join(content)

### Use selenium to automate get News links
from selenium import webdriver
chrome_path = "/YOUR_CHROMEDRIVER_PATH..."
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_path,chrome_options=chrome_options)

urls = set()
for k in range(0, 10):
    driver.get('https://www.yahoo.com/{}'.format('/'.join(categories[k])))
    
    for i in range(1, 15):
        time.sleep(2.5)
        for article in driver.find_elements_by_css_selector("#YDC-Stream > ul > li > div > div > div > h3 > a"):
            if article.text:
                urls.add(article.get_attribute('href'))
        print(len(urls))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
import re
url_re = re.compile('-(\d{7,10})')

def parse_nid(url):
    m = url_re.search(url)
    if m is not None:
        return m.group(1)
            
### Save each news
count = 1
for url in urls:
    print(count)
    count+=1
    print(url)
    nid = parse_nid(url)
    if nid is not None:
        filename = '/YOUR_DIRECTORY...' + nid
    else:
        continue
        
    if os.path.isfile(filename):
        continue

    content = get_new_content(url)
    if content is not None: 
        with open(filename, 'w') as f:
            print(content.encode('utf-8', 'ignore'), file = f)