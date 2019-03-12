from selenium import webdriver

driver = webdriver.Chrome()
# 访问百度首页
driver.get("http://www.baidu.com")

#查找输入框，输入内容
input_ele = driver.find_element_by_id("kw")
#在输入框中输入想要搜索的内容
input_ele.send_keys("chrome_driver")

#点击搜索
driver.find_element_by_id("su").click()


# hello test1

