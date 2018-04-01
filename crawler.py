#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import xlwt
import os
import urllib
import ssl



#================Setting===========================

minPushNumber = 30  #最小推文數
exclude = ['帥哥']  #排除清單
targetURL = 'https://www.ptt.cc/bbs/Beauty/index2429.html'
hostURL = 'https://www.ptt.cc'

#================Setting===========================

def output(filename, sheet, list1):
    book = xlwt.Workbook()
    sh = book.add_sheet(sheet)
    sh.write(0, 0, '標題')
    sh.write(0, 1, '推文數')
    sh.write(0, 2, '連結')
    i = 0
    for item in list1:
        i=i+1
        sh.write(i, 0, item['title'])
        sh.write(i, 1, item['pushNumber'])
        sh.write(i, 2, item['url'])

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
        urllib.request.urlretrieve(img_url,filename=filename)
    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)


#目標網址
#取消SSL驗證
ssl._create_default_https_context = ssl._create_unverified_context
r = requests.get(targetURL)

if r.status_code == 200: #200為成功的狀態碼
    # 解析html標籤
    data = BeautifulSoup(r.text, 'html.parser')

    # 找出目標
    a_tag = data.find_all('div', class_='r-ent')

    # 個別顯示
    data=[]
    for item in a_tag:
        if (item.find('a') is not None) and (item.find('span', class_='hl') is not None):
            #計算推文數, 爆=100
            pusnNum = 0
            if item.find('span', class_='hl').string == '爆':
                pusnNum = 100
            else:
                pusnNum = int(item.find('span', class_='hl').string)

            if pusnNum > minPushNumber:
                data.append({'title': item.find('a').string, 'pushNumber': pusnNum,
                             'url': hostURL + item.find('a')['href']})
                print('標題: '+item.find('a').string)
                print('推文數: '+ str(pusnNum))
                print('文章連結: ' + hostURL + item.find('a')['href'])
                content = requests.get(hostURL + item.find('a')['href'])

                hyperLink = BeautifulSoup(content.text, 'html.parser')
                if hyperLink is not None:
                    hyperLink = hyperLink.find_all('a')
                    no = 1
                    for pic in hyperLink:
                        if 'jpg' in pic['href']:
                            print('圖片下載中...')
                            save_img(pic['href'], str(no), '\img\\'+item.find('a').string)
                            no = no+1
    print(data)
    output('beati.xls', 'Test1', data)
else:
    #顯示錯誤訊息
    print('讀取網頁失敗，請確認網址: ' + targetURL)




