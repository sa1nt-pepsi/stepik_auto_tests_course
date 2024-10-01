from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR,'#input_value')
x = x_element.text
y = calc(x)

element1 = browser.find_element(By.CSS_SELECTOR,'#answer')
element1.send_keys(y)

button1 = browser.find_element(By.CSS_SELECTOR,"[for='robotCheckbox']")
button1.click()
button2 = browser.find_element(By.CSS_SELECTOR,"#robotsRule")
button2.click()
button3 = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
button3.click()

time.sleep(5)
browser.quit()
