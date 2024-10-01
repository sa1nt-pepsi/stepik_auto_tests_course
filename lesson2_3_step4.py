from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    
link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
button.click()

alert = browser.switch_to.alert
alert.accept()

x_element = browser.find_element(By.ID,'input_value')
x = x_element.text

answer = browser.find_element(By.ID,'answer')
answer.send_keys(calc(int(x)))

button2 = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
button2.click()

time.sleep(5)
browser.quit()
     