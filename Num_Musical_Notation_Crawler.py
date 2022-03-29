import time
import requests
import re
import sys
import bs4
import os
import stat
import urllib
from bs4 import BeautifulSoup
from selenium import webdriver



root_url = 'http://www.jianpuw.com/search.aspx?q='
key_word = sys.argv[1]
url = root_url + key_word
url2 = 'http://www.jianpuw.com/'
file_path = '/Users/zwsuo/Music/Num_Musical_Notation_Images'

headers = {
        'User-Agent': 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0',
        'Cookie': 'UM_distinctid=17d85032f6961a-006efee2d213f1-45596a-1aeaa0-17d85032f6a5f6; CNZZDATA1000092060=1382527029-1638607060-null%7C1638674862'
    }
    
root_response = requests.get(url,headers=headers)
root_response.encoding = 'utf-8'
root_source = root_response.text
root_element = BeautifulSoup(root_source,'lxml')

root_ul = root_element.find('ul')
print('='*50,' Start ','='*50)
for li in root_ul.find_all("li"):
    root_music_name = li.a.get_text()
    root_music_link = url2+li.a['href'].lstrip('../')
    print(root_music_name,root_music_link)
    browser=webdriver.Chrome()
    browser.get(root_music_link)
    cu_response = browser.page_source
    cu_element = BeautifulSoup(cu_response,'lxml')
    img_info = cu_element.find_all('img')
    # print (img_info)
    time.sleep(1)
    for img in img_info:
        print('='*25,' Start to parse image page.','='*25)
        cu_music_name = img.get('title')
        cu_music_jianpuimg_link = url2+'/'+(img.get('src').lstrip('../..'))
        print (cu_music_name,'==',cu_music_jianpuimg_link)
        print('='*25,' End of parse image page.','='*25)

        try:
            file_name = cu_music_jianpuimg_link.split('/')[-1]
            file_path2 = file_path+os.sep+key_word
            filename = '{}{}{}'.format(file_path2,os.sep,file_name)
            print('IMG: ',filename)
            if not os.path.exists(file_path2):
                os.makedirs(file_path2)
            urllib.request.urlretrieve(cu_music_jianpuimg_link,filename=filename)
        except Exception as error_info:
            print (error_info)
        time.sleep(1)
    browser.close()
print('='*50,' End.','='*50)