from selenium import webdriver
import LoginInfo
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time

tStart = time.time()

#'C:\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome('/Volumes/Transcend/GitProject/PTTParser/chromedriver')

#login
# browser.get('https://secure.rakuten.com.tw/member/signin?return_url=?service_id=Top&return_url=https:%2F%2Fwww.rakuten.com.tw%2F')

#登入頁面
loginInfo = LoginInfo.LoginInfo()#

#購物頁面
browser.get('https://www.rakuten.com.tw/shop/2097game/product/100000008863393/?l-id=tw_search_grid_product_1')
# browser.get('https://www.rakuten.com.tw/shop/conishop/product/9jz726jrb/?s-id=Event-supersale-180409-index-041012-001')

# sleep(10) # 延遲10秒

buyButton = browser.find_elements_by_xpath("//*[contains(text(), '立即購買')]")

print(buyButton)

buyButton[1].click()
browser.find_elements_by_xpath("//*[contains(text(), '繼續結帳')]")[0].click()

#登入頁面
userName = browser.find_element_by_id('username')
userName.send_keys(loginInfo['account'])
password = browser.find_element_by_id('password')
password.send_keys(loginInfo['password'])
browser.find_elements_by_xpath("//*[contains(text(), '以會員身份登入')]")[1].click()

#配送方式頁面
if browser.find_elements_by_xpath("//*[contains(text(), '其他物流')]"):
    browser.find_elements_by_xpath("//*[contains(text(), '其他物流')]")[0].click()

browser.find_elements_by_xpath("//*[contains(text(), '繼續付款')]")[0].click()

#結帳頁面
# payment = browser.find_elements_by_xpath("//*[contains(text(), '常用信用卡 (1)')]")[0].click()
# sleep(1) #popput delay
# # WebDriverWait(browser, 10).until(browser.find_element_by_id('CVV'))
#
# cvv = browser.find_element_by_id('CVV')
# cvv.send_keys(loginInfo['cvv'])
#
#
#
# idCard = browser.find_element_by_id('id-card-number')
# idCard.send_keys(loginInfo['idCard'])

finish = browser.find_elements_by_xpath("//*[contains(text(), 'ATM轉帳')]")[0].click()

tEnd = time.time()#計時結束

print("It cost %f sec" % (tEnd - tStart))#會自動做近位

###### finish.click()  #真的會結帳語法



