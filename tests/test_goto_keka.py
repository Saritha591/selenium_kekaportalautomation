from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from data import config
print("test case started")


def test_goto_Kekaportal():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://msys.keka.com/")
    time.sleep(5)
    driver.find_element(By.XPATH, "//body//div[@class='d-flex vh-100']//div[@class='login-content d-flex flex-column justify-content-between overflow-auto']//div//div//div[2]//button[1]//div[1]//img[1]").click()
    time.sleep(5)
    