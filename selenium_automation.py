from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\Dimuth De Zoysa\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('file:///C:/Users/Dimuth%20De%20Zoysa/Desktop/Python_projects/Details_Input&Display.html')

file = open('C://Users//Dimuth De Zoysa//Desktop//Python_projects//user_detail.txt', 'r')
lines = file.readlines()

time.sleep(5)

for line in lines :
    
    items = line.replace('\n','').split(' ')

    time.sleep(2)

    fname = driver.find_element_by_id("first_name")
    fname.clear()
    fname.send_keys(items[0])
    time.sleep(1)

    lname = driver.find_element_by_id("last_name")
    lname.clear()
    lname.send_keys(items[1])
    time.sleep(1)

    dropdown = Select(driver.find_element_by_id('dropdown_gender'))
    dropdown.select_by_visible_text(items[2])
    time.sleep(1)

    age = driver.find_element_by_id("num_age")
    age.clear()
    age.send_keys(items[3])
    time.sleep(1)

    bdate = driver.find_element_by_id("num_birthyear")
    bdate.clear()
    bdate.send_keys(items[4])
    time.sleep(1)

    driver.find_element_by_id("btn_submit").click()
