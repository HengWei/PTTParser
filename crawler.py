#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import xlwt
import os
import urllib


def output(filename, sheet, list1):
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet)


    sh.write(0, 0, '標題')
    i = 0
    for item in list1:
        i=i+1
        sh.write(i, 0, item)
    book.save(filename)


def save_img(img_url,file_name,file_path='\img'):
    #保存图片到磁盘文件夹 file_path中，默认为当前脚本运行目录下的 book\img文件夹
    try:
        if not os.path.exists(file_path):
            print('文件夹',file_path,'不存在，重新建立')
            #os.mkdir(file_path)
            os.makedirs(file_path)
        #获得图片后缀
        file_suffix = os.path.splitext(img_url)[1]
        #拼接图片名（包含路径）
        filename = '{}{}{}{}'.format(file_path,os.sep,file_name,file_suffix)
       #下载图片，并保存到文件夹中
        urllib.urlretrieve(img_url,filename=filename)
    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)


#目標網址
targetURL = 'https://www.ptt.cc/bbs/Beauty/index2429.html'

r = requests.get(targetURL)

if r.status_code == 200: #200為成功的狀態碼
    # 解析html標籤
    data = BeautifulSoup(r.text, 'html.parser')

    # 找出目標
    a_tag = data.find_all('div', class_='r-ent')

    # 個別顯示
    TitleList = []
    pushBum = []
    url = []
    for item in a_tag:
        if (item.find('a') is not None) and (item.find('span', class_='hl') is not None):
            # 只顯示30推以上
            if (item.find('span', class_='hl').string == '爆') or (int(item.find('span', class_='hl').string) > 30):
                print(item.find('a').string)
                print(item.find('span', class_='hl').string)
        # if item.find('a') != None:
        #     print(item.find('span', class_='hl f3').string)
        #     TitleList.append(item.find('a').string)
        #     print(item.find('a').string)
        # BeautifulSoup(item, 'html.parser').find('a')
    # output('beati.xls', 'Test1', TitleList)
else:
    #顯示錯誤訊息
    print('讀取網頁失敗，請確認網址: ' + targetURL)




