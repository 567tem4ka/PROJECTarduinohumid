import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path=r"D:\project arduinointrface\directory\Chrome\chromedriver.exe")
browser.get('https://www.hivemq.com/demos/websocket-client/')
assert 'Client' in browser.title
time.sleep(2)
elem = browser.find_element(By.ID, 'connectButton').click()
time.sleep(2)
elem = browser.find_element(By.ID, 'addSubButton').click()
time.sleep(2)
elem = browser.find_element(By.ID, 'subscribeTopic')
elem.clear()
time.sleep(1)
elem.send_keys('bop')
time.sleep(1)
elem = browser.find_element(By.ID, 'subscribeButton').click()

while True:
    time.sleep(10)
    #mes = browser.find_element(By.CLASS_NAME, 'large-12 columns message break-words')
    time.sleep(1)
    #print(mes)
