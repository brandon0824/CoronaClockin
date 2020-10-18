from selenium import webdriver
import time as tm
import random
import json

print("-----Auto Fill Form Starting-----")
with open('info.json', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)
# print("username: " + str(obj['username']))
# print("password:" + str(obj['password']))
myusername = str(obj['username'])
mypassword = str(obj['password'])

print("Your username is : " + myusername)
print("Your password is : " + mypassword)

login_url = 'https://jkxxcj.zjhu.edu.cn/login.html'

driver = webdriver.Chrome()
driver.get(login_url)
driver.maximize_window()
tm.sleep(3)

username = driver.find_element_by_id('zgh')
username.send_keys(myusername)

password = driver.find_element_by_id('mm')
password.send_keys(mypassword)

button = driver.find_element_by_id('loginBtn')
button.click()

tm.sleep(3)
healthReport = driver.find_element_by_link_text('健康报告')
healthReport.click()

a = random.uniform(36.6, 37.4)
b = random.uniform(36.6, 37.4)
a1 = round(a, 1)
b1 = round(b, 1)
# print(a1, b1)
mornTemp = str(a1)
nightTemp = str(b1)
print("Random morning Temperature : " + mornTemp)
print("Random night Temperature : " + nightTemp)

tm.sleep(3)
inputMorn = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/form/div[19]/div/textarea")
inputMorn.clear()
inputMorn.send_keys(mornTemp)

tm.sleep(3)
inputNight = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/form/div[20]/div/textarea")
inputNight.clear()
inputNight.send_keys(nightTemp)

tm.sleep(3)
confirm = driver.find_element_by_id('saveBtn')
confirm.click()

driver.close()
print("-----Auto Fill Form Finished-----")