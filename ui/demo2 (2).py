# -*-coding:UTF-8 -*-

from time import sleep

from pymysql import connect
from selenium import webdriver

from myexcel.du_student import cursor


driver=webdriver.Chrome('..\driver\chromedriver.exe')
driver.get('http://192.168.1.4/ecshop/admin/privilege.php?act=login')
driver.maximize_window()
 
driver.find_element_by_name('username').send_keys('caichang')
driver.find_element_by_name('password').send_keys('caichang1')
driver.find_element_by_class_name('btn-a').click()

sleep(2)
driver.switch_to.frame('menu-frame')
driver.find_element_by_link_text('商品列表').click()
driver.switch_to.default_content()
driver.switch_to.frame('main-frame')
sleep(2)
driver.find_element_by_name('keyword').send_keys('车')
driver.find_element_by_xpath("//input[@value=' 搜索 ']").click()

sleep(1)
search_text=driver.find_element_by_xpath('//*[@id="listDiv"]/table[1]/tbody/tr[3]/td[2]/span').text
search_total=driver.find_element_by_id('totalRecords').text

conn=connect('192.168.1.4','root','root','ecshop',3306)
coursor=conn.cursor()
coursor.execute("select goods_name from ecs_goods where goods_name like '%车%'")

rs=cursor.fetchall()


coursor.execute("select count(*) from ecs_goods where goods_name like '%车%'")
total = cursor.fetchone()

if search_text==rs[0][0] and int(search_total)==total[0]:
    print('测试通过')
    
else:
    print('测试不通过')
cursor.close()
conn.close()
    


















