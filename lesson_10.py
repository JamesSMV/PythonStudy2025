from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# def test_local():
#     pass



driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(5)  # Ждём 10 секунд
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Return to") # поиск по части "Return to index" текста
link.click()
time.sleep(20)  # Ждём 10 секунд перед закрытием
# print(driver.title)
# driver.quit()

