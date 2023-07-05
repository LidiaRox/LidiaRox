from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from selenium.webdriver.common.by import By

#CSS Variables
titleClass = "h1"
titleName = "p-jAFk Qo+b2C"
ratingClass = "span"
ratingName = "_2me3j1 _23dw7w"
synopsisClass = "div"
synopsisName = "_3qsVvm e8yjMf"

storeFrontURL = "https://www.amazon.com/gp/video/storefront"
vidDownloadURL = "/gp/video/detail/"

videoLinks = []
titles = []
ratings = []
synopsis = []

def scrapeText(list, classType, className):
    findClass = soup.find_all(classType, class_=className)
    if len(findClass)== 0:
        list.append(None)
    else:
        for n in findClass:
            if className == ratingName:
                list.append(float(n.text[-3:]))
            else:
                list.append(n.text)

# Initialize browser to be controlled by Phyton
driver = webdriver.Chrome()
driver.get(storeFrontURL)

elements = driver.find_elements(By.XPATH,'//a[@href]')
for element in elements:
    if vidDownloadURL in element.get_attribute("href"):
        videoLinks.append(element.get_attribute("href"))

videoLinks = list(dict.fromkeys(videoLinks))

for i in range(0,10):
    driver.get(videoLinks[i])
    content = driver.page_source
    soup = BeautifulSoup(content,'features="html.parser"')

scrapeText(titles, titleClass, titleName)
scrapeText(ratings, ratingClass, ratingName)
scrapeText(synopsis, synopsisClass, synopsisName)

print(titles)


