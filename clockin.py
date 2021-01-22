# -*- coding: UTF-8 -*-
from selenium import webdriver
import time as tm
import random
import json

def readJson():

    username = []
    password = []

    with open('D:/python_practice/CoronaClockin/info.json', 'r') as myfile:
        data=myfile.read()

    obj = json.loads(data)
    member = obj['members']
    print(json.dumps(member, indent=4, ensure_ascii=False))

    for i in range(len(member)):
        # print(json.dumps(member[i], indent=4, ensure_ascii=False))
        un = member[i]['username']
        pwd = member[i]['password']
        username.append(un)
        password.append(pwd)
    print(username)
    print(password)

    return username,password

def clockin(myusername, mypassword):
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

    tm.sleep(3)
    check_url = 'https://jkxxcj.zjhu.edu.cn/historyList.html'
    driver.get(check_url)
    tm.sleep(3)

    obj = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/table/tbody/tr[1]/td[2]/span")
    state = obj.text
    # type(state) = 'str' 2state:已填写/未填写
    # print(state)
    if state == '已填写':
        print(f'The account of {myusername} signed succeed!')
    else:
        print(f'The account of {myusername} signed failed!')

    tm.sleep(3)
    driver.close()



if __name__ == '__main__':
    
    print("-----Auto Fill Form Starting-----")
    uname, pwd = readJson()
    for i in range(len(uname)):
        clockin(uname[i], pwd[i])

    print("-----Auto Fill Form Finished-----")