import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import os
from dotenv import load_dotenv
load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1500, driver.get_window_size()['height'])
driver.get("https://tinder.com")

time.sleep(2)
login = driver.find_element(By.XPATH,'//*[@id="s1592971809"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
login.click()

time.sleep(4)
fblogin = driver.find_element(By.XPATH,'//*[@id="s-135409267"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
fblogin.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
time.sleep(2)

email = driver.find_element(By.XPATH,'//*[@id="email"]')
password = driver.find_element(By.XPATH,'//*[@id="pass"]')
email.send_keys(os.environ["my_email"])
time.sleep(3)

password.send_keys(os.environ["my_pass"],Keys.ENTER)
time.sleep(5)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)

allow_location_button = driver.find_element(By.XPATH, value='//*[@id="s-135409267"]/div/div[1]/div/div/div[3]/button[1]')
allow_location_button.click()

time.sleep(10)
like = driver.find_element(By.XPATH,
                                   '//*[@id="s1592971809"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
for n in range(100):
    try:
        time.sleep(2)
        like.click()
    except ElementClickInterceptedException:
        time.sleep(3)
        continue

