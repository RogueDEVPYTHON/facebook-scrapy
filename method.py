from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import json
import sys

driver =webdriver.PhantomJS( service_log_path='phantomjs/ghostdriver.log', executable_path='phantomjs/bin/phantomjs')
driver.set_window_size(1024, 768)
try:
	sys.argv[1]
	try:
		sys.argv[2]
		print("https://www.facebook.com/marketplace/"+sys.argv[1]+"/"+sys.argv[2])
		driver.get("https://www.facebook.com/marketplace/"+sys.argv[1]+"/"+sys.argv[2])
	except Exception as e:
		print("Second arguments not")
	finally:
		print("https://www.facebook.com/marketplace/"+sys.argv[1])
		driver.get("https://www.facebook.com/marketplace/"+sys.argv[1])
except Exception as e:
	print("No arguments")
	driver.get("https://www.facebook.com/marketplace/")

page = driver.page_source

soup = BeautifulSoup(page, "html.parser")
source = soup.select('#js_2 > div._3-98 > div > div > div._65db > a > div > div._2ph_._2ms_._4-u3 > div._50f4 > div > p')#js_3 > div._3-98 > div > div > div._65db > a:nth-child(1) > div > div._2ph_._2ms_._4-u3 > div._50f4 > div > p#js_6 > div._3-98 > div > div > div._65db > a:nth-child(1) > div > div._2ph_._2ms_._4-u3 > div._50f4 > div > p#js_6 > div._3-98 > div > div > div._65db > a:nth-child(1) > div > div._2ph_._2ms_._4-u3 > div._50f4 > div > p#js_5 > div._3-98 > div > div > div._65db > a:nth-child(1) > div > div._2ph_._2ms_._4-u3 > div._50f4 > div > p#js_5 > div._3-98 > div > div > div._65db > a:nth-child(1) > div > div._2ph_._2ms_._4-u3 > div._50f4 > div > p#js_2 > div._3-98 > div > div > div._65db > a:nth-child(1) > div > div._2ph_._2ms_._4-u3 > div._50f4 > div > p
text = [];
for element in source:
	text.append(element.text)
print(json.dumps(text))

#chrome_driver_path = r"chromedriver.exe"

#driver = webdriver.Chrome()
#driver.get("https://www.facebook.com/marketplace/103729219665367")