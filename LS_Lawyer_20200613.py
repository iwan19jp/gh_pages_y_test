#import time
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
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 Mobile/14C92 Safari/602.1')
#options.add_argument('--disable-gpu')
#browser = webdriver.Chrome(chrome_options=options)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
#browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
browser = webdriver.Chrome('./chromedriver',chrome_options=options)
#browser = webdriver.Chrome()

# URLにアクセス
# 検索対象URL
url ="https://www.bengo4.com/tokyo/f_12/"
browser.get(url)

#抽出できているかテスト
sleep(2)
w = browser.execute_script('return document.body.scrollWidth')
h = browser.execute_script('return document.body.scrollHeight')
browser.set_window_size(w, h)
browser.save_screenshot('screenshot.png')
browser.save_screenshot('tw_screenshot.png')

print('---- screenshot OK --------')

#スクレイピング対象ペイン
#main_element = browser.find_element_by_class_name("pressrelease")

elm_list = []

#登録されているの弁護士事務所
#for idx in range(1):
sleep(3)
#lawyer_element = browser.find_element_by_class_name("route-citizen-searchResultV2")
lawyer_element = browser.find_element_by_xpath('//div')
element_html = lawyer_element.get_attribute("innerHTML")
print(element_html)
    #prsrls_element_edt = prsrls_element.text.replace("のプレスリリース","")
    #company_list.append(prsrls_element_edt)

#next_btn_element = browser.find_elements_by_xpath('//a[@id="addPr"]')

#next_btn_element[0].click()
#sleep(3)

#もっと見るボタン　クリック後の範囲
#for boxno in range(1000):
#    print(boxno)
#    tag = f'//div[@class="list box_no{boxno+1}"]/div[2]/p[2]/a[1]'
#    for idx2 in range(10):
#        prsrls_element_next = browser.find_elements_by_xpath(tag)[idx2]
#        company_list.append(prsrls_element_next.text)
#        #print(prsrls_element_next.text)
#    next_btn_element[0].click()
#    sleep(3)

#with open('pressRelease_List.txt','wt') as f:
#    #writer = csv.writer(f)
#    for comp in company_list:
#        #print(comp)
#        f.write(comp + '\n')
#


# ブラウザーを終了
browser.quit()

#print(company_list)

print('completed!!')
