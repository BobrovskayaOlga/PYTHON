from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

brauser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
brauser.get("https://ya.ru")

#(1)
#element = brauser.find_element(By.CSS_SELECTOR,"#text")
#element.clear()
#lement.send_keys("test skypro")

#brauser.find_element(By.CSS_SELECTOR, "button[type=submit]").click
#sleep(10)

#print(element)

#brauser.find_elements()

#(2)
usd = brauser.find_element(By.CSS_SELECTOR, "&nbsp;&nbsp;").text

sleep(10)
txt = usd.text

print(txt)

#(3)


#sleep(10)
#brauser.quit()

#sleep(10)
#txt = usd.text

#print(txt)

#(3)


sleep(10)
brauser.quit()