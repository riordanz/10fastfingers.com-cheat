from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from random import randint
from time import sleep

driver = webdriver.Chrome('./chromedriver')
driver.get('https://10fastfingers.com/')
wait = WebDriverWait(driver, 600)
wait.until(EC.presence_of_element_located((
	By.ID, 'inputfield')))
sleep(4)
inp = driver.find_element_by_css_selector('#inputfield')
f = open('dataq').read()
i = 0
for msg in f:
	inp.send_keys(msg)
