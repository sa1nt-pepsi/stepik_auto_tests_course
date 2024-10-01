from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.CSS_SELECTOR,'#input_value')
x = x_element.text
y = calc(x)

button = browser.find_element(By.CSS_SELECTOR,"[type='submit']")
browser.execute_script('window.scrollBy(0, 100);')

element1 = browser.find_element(By.CSS_SELECTOR,'#answer')
element1.send_keys(y)

button1 = browser.find_element(By.CSS_SELECTOR,"[for='robotCheckbox']")
button1.click()
button2 = browser.find_element(By.CSS_SELECTOR,"#robotsRule")
button2.click()
button.click()

time.sleep(5)
browser.quit()
