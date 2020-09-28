# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
# 启动chrome游览器
driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# 启动edge游览器
# driver = webdriver.Firefox()
driver.get("http://www.5itest.cn/register")
# 延迟五秒等这个页面加载完
time.sleep(5)
# 页面加载完后检测页面有没有“包含注册字样”，来判断界面是否加载成功
print(EC.title_contains("注册"))
# 通过class_name找出元素
element = driver.find_element_by_class_name("controls")
locator = (By.CLASS_NAME, "controls")
# EC.visibility_of_element_located(element)在页面显示的元素
# webDriverwait(driver,10)表示在页面中找元素，找10秒钟，找不到就报错提示
# 如果找到元素则往下运行，没有则返回false
WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator))
email_element = driver.find_element_by_id("register_email")
# 获取元素的值
print(email_element.get_attribute("placeholder"))
email_element.send_keys("test@163.com")
# 获取用户填入的值
print(email_element.get_attribute("value"))


# 每次实例化一个driver但没有关闭的话会导致电脑越来越卡顿，所以应该关闭掉driver
driver.close()

# driver.find_element_by_id("register_email").send_keys("mushishi1_01@163.com")
# 一定要是driver.find_elements_by_class_name,不可以写成element，因为class_name为controls的元素有很多个
#user_name_element_node = driver.find_elements_by_class_name("controls")[1]
# 获取class_name 为 controls的元素下的class_name为“form_control”的元素
#user_element = user_name_element_node.find_element_by_class_name("form-control")
# user_element.send_keys("qerqewre")
# driver.find_element_by_name("password").send_keys("11111")
# 使用xpath还获取元素时，双引号里面双引号要改成单引号
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("11111")
