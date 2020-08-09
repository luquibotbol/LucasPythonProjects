from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.aliexpress.com/")
print(driver.title)
search = driver.find_element_by_name("SearchText")
ask = input('What do you wanna search on AliExpress \n')
search.send_keys(ask)
search.send_keys(Keys.RETURN)
timeout = 10
num = 0
try:
    main = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'list-items'))
    )
    items = main.find_elements_by_tag_name("a")
    for item in items:
        link = item.find_elements_by_class_name("find_elements_by_tag_name")
        num = num+1



except TimeoutException:
    print("passed 3 seconds didn't load")

finally:
    print(num)
    driver.quit()