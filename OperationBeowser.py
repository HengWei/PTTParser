from selenium import webdriver

browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')


browser.get('https://google.com.tw')

serachBar = browser.find_element_by_id('lst-ib')
serachBar.send_keys('Find Test')