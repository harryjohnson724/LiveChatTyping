from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep


driver = webdriver.Firefox()
driver.get("https://www.livechat.com/typing-speed-test/#/")


typing_space = driver.find_element_by_id("test-input")

t_end = time.time() + 60
while time.time() < t_end:
    for i in range(15):
        sleep(0.1)
        typing_space.send_keys(driver.find_element_by_xpath("//span[contains(@data-reactid,'.0.1.1.0.0.$=11.0.$=10.1.1.$0')]").text)
        typing_space.send_keys(" ")


