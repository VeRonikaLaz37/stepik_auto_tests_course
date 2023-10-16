from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    def calc(x):
       return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)
    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
