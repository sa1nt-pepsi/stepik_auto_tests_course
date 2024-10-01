from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element(By.CSS_SELECTOR,"[name='firstname']")
button1.send_keys('Name')
button2 = browser.find_element(By.CSS_SELECTOR,"[name='lastname']")
button2.send_keys('LastName')
button3 = browser.find_element(By.CSS_SELECTOR,"[name='email']")
button3.send_keys('email')
button4 = browser.find_element(By.ID,"file")
    
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'test.txt')
button4.send_keys(file_path)

button = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
button.click()
time.sleep(5)
browser.quit()


    