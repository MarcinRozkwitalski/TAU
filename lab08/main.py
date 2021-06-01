from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.remote.webelement import WebElement

PATH = "D:\Studia\semestr 6\TAU\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://google.com")

agreement = driver.find_element_by_xpath('//*[@id="L2AGLb"]/div')
agreement.click()
driver.find_element_by_xpath('//input[@name = "q"]').send_keys("hello world")
driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.ENTER)
driver.find_element_by_xpath('//h3[contains(text(), "Hello world")]').click()
driver.find_element_by_xpath('//a[contains(text(), "Zaloguj się")]').click()
login = driver.find_element_by_xpath('//input[@id="wpName1"]')
login.click()
login.send_keys("tojestmojlogin")
password = driver.find_element_by_xpath('//input[@id="wpPassword1"]')
time.sleep(3)
password.click()
password.send_keys("tojestmojehaslo")
driver.find_element_by_xpath('//button[@id="wpLoginAttempt"]').click()
time.sleep(5)
driver.minimize_window()
driver.quit()

driver2 = webdriver.Chrome(PATH)
driver2.get("https://www.youtube.com/")
agreement2 = driver2.find_element_by_xpath('//*[@class="VfPpkd-dgl2Hf-ppHlrf-sM5MNb"]/div')
agreement2.click()
forgotEmail = driver2.find_element_by_xpath('//*[@jsname="Cuz2Ue"]')
forgotEmail.click()
driver2.find_element_by_xpath('//a[@href="https://support.google.com/accounts?hl=en"]').click()
time.sleep(3)
driver2.minimize_window()
driver2.quit()