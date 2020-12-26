# -*-coding:UTF-8 -*-
from selenium import webdriver
from select import select
from selenium.webdriver.support.select import Select
from pymysql import connect
from time import sleep

conn=connect('192.168.1.4','root','root','ecshop',3306)
cursor=conn.cursor()
cursor.execute("delete from ecs_goods where goods_name='华为手机'")
conn.commit()


driver=webdriver.Chrome('..\drdriverhromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()

driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
driver.switch_to.default_content()

driver.switch_to.frame('main-frame')
# driver.find_element_by_name('keyword').send_keys('车')
# driver.find_element_by_class_name('button').click()
driver.find_element_by_xpath('/html/body/h1/span[1]/a').click()

driver.find_element_by_name('goods_name').send_keys('华为手机')
Select(driver.find_element_by_name('cat_id')).select_by_visible_text('    小型手机')
driver.find_element_by_xpath('//*[@id="tabbody-div"]/form/div/input[2]').click()
sleep(2)
cursor.execute("select * from ecs_goods where goods_name='华为手机'")
result=cursor.fetchone()
print(result)

if result[3]=='华为手机':
    print('测试通过')
    
else:
    print('测试不通过')
conn.close()
cursor.close()












