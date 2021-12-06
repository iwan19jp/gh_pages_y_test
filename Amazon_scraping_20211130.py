#webスクレイピング

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#import chromedriver_binary
from selenium.webdriver.support.ui import Select
from time import sleep
#from webdriver_manager.chrome import ChromeDriverManager
import csv

options = Options()
#options.binary_location = 'C:\\Users\\Yasushi19\\Anaconda3\\Lib\\site-packages\\chromedriver_binary'
options.add_argument('--headless')
#options.add_argument('--disable-gpu')
#browser = webdriver.Chrome(chrome_options=options)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
#browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
browser = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=options)

# 検索対象URL
url ="https://www.amazon.co.jp/"

browser.get(url)

word='手帳'

#キーワード入力
#next_button_element = browser.find_element_by_xpath("//a[@class='btn_next pagerNext nextprev next']").click
keyword_element = browser.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
keyword_element.send_keys(word)
browser.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()

sleep(3)

page_height = browser.execute_script("return document.body.scrollHeight;")
browser.set_window_size(1300,  page_height)

#browser.set_window_size(1280, 720)
browser.save_screenshot('screenshot1201_01.png')

main_element = browser.find_elements_by_xpath("//div[@data-asin]")
print(len(main_element))

#for itm in range(len(main_element)):
for itm in range(5):
    sleep(2)
    item_element= main_element[itm].get_attribute("data-asin")
    print(item_element)

next_page = browser.find_element_by_xpath("//li[@class='a-last']/a")
next_url = next_page.get_attribute("href") 

print(next_url)

browser.get(next_url)

sleep(3)

page_height = browser.execute_script("return document.body.scrollHeight;")
browser.set_window_size(1300,  page_height)
browser.save_screenshot('screenshot1201_02.png')

#src=item_element.get_attribute("innerHTML")

#f = open('Source01.txt', 'w')
#f.write(src)

#item_element = main_element.find_elements_by_xpath("//div[0]")
#print(item_element.get_attribute("innerHTML"))
