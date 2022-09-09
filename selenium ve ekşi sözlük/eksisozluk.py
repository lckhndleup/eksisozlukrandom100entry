from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


chrome_driver_path="/Users/mehmetaliyildiz/Drivers/chromedriver"

driver = webdriver.Chrome(chrome_driver_path)

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount = 1

entries=[]
entryCount=1

while pageCount <=10:
    randomPage = random.randint(1,2384)
    newUrl = url + str(randomPage)
    driver.get(newUrl)
    elements = driver.find_elements(By.CSS_SELECTOR,'.content')
    for element in elements:
        entries.append(element.text)
    time.sleep(1)
    pageCount += 1


with open("entries.txt","w",encoding= "UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount)+".\n" + entry + ".\n")
        file.write("********************************\n")
        entryCount+=1



driver.close()


