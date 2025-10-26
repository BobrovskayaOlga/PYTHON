from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#(1)
#brauser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#current_title = brauser.title

#print(current_title)

#brauser.quit()


#(2)
#brauser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#brauser.get("http://ya.ru")

#url = brauser.current_url

#print(url)

#brauser.quit()

#(3)
#brauser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#brauser.get("http://ya.ru")

#brauser.maximize_window()
#brauser.minimize_window()
#brauser.fullscreen_window()
#brauser.set_window_size(1000, 600)

#sleep(10)

#(4)
brauser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}


brauser.get("https://labirint.ru")
brauser.add_cookie(my_cookie)

cookies = brauser.get_cookies()
print(cookies)

brauser.refresh()

brauser.delete_all_cookies()
brauser.refresh()

sleep(20)
brauser.quit()
