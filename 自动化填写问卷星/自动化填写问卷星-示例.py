#导入相关库
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from random import choice
#问卷网址
url='https://www.wjx.cn/vm/hKvbqcL.aspx'
#绕过问卷星的智能检测，将webdriver属性设置为undefined，不设置也不会错
option=Options()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_experimental_option('useAutomationExtension',False)
web=Chrome(options=option)
web.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{'source':'Object.defineProperty(navigator,"webdriver",{get:()=>undefined})'})
#对页面进行请求
web.get(url)
#设置每个题目的选项列表
#分别对每个题进行随机的，或者有倾向填充
for i in range(1,4):
	qa_tmp=web.find_element(By.XPATH,f"//*[@id='div{i}']")
	answers=qa_tmp.find_elements(By.XPATH,f".//div[@class='ui-radio']")
	# 生成随机选项
	# [1,2,3,3,3,33,3,33,3,33,]
	answer=choice(answers)
	answer.click()
qa_tmp=web.find_element(By.XPATH,"//*[@id='div4']")
input_=qa_tmp.find_element(By.XPATH,".//input")
input_.send_keys('Python 好啊！')
sleep(0.1)
#点击提交按钮
web.find_element(By.XPATH,'//*[@id="ctlNext"]').click()
sleep(0.1)
web.quit()