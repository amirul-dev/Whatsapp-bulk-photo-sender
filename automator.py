from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoAlertPresentException
from time import sleep
from urllib.parse import quote
from sys import platform

driver = webdriver.Firefox()

print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
print("*****      This tool was built by Amirul Haqe       ******")
print("*****           www.github.com/amirul-dev           ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")

f = open("message.txt", "r")
message = f.read()
f.close()

print("##########################################################")
print('This is your message\n\n')
print(message)
print("##########################################################")
message = quote(message)

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line != "":
		numbers.append(line)
		
f.close()
total_number=len(numbers)
print("##########################################################")
print('\nWe found ' + str(total_number) + ' numbers in the file')
print("##########################################################")
print()


print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visiable	.")
for idx, number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue
	print('{}/{} => Sending message to {}.'.format((idx+1), total_number, number))
	try:
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		driver.get(url)
		driver.implicitly_wait(20)
		text_field = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
		text_field.send_keys(Keys.ENTER)
		driver.implicitly_wait(20)
		text_field.send_keys(Keys.CONTROL + 'V')
		driver.implicitly_wait(20)
		text_field = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]')
		text_field.send_keys(Keys.ENTER)
		sleep(5)

	except Exception as e:
		print('Failed to send message to ' + number + str(e))
