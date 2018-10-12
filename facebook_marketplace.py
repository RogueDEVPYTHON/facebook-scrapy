#coding: utf-8
from bs4 import BeautifulSoup
import requests
import lxml
import codecs
all_html = ""
try:
    URL = "https://www.facebook.com/marketplace/"
    response = requests.get(URL)
    all_html =  all_html + response.text
except:
    print(index)
soup =  BeautifulSoup(all_html, "html.parser")
all_title = soup.select('#u_0_c > div > div > div > div > div > div > div > a > div > div > div > div > p')
#js_8 > div._3-98 > div > div > div._65db > a:nth-child(1) > div > div._2ph_._2ms_._4-u3 > div._50f4 > div > p
print(all_title);
#f = codecs.open('a.txt', 'w', encoding='utf-8')
#for title in all_title:
#    f.write(title.text)
#    f.write("\r\n")
