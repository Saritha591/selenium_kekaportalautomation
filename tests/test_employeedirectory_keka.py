from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from data import config
print("test case started")

user = config.user
password = config.password


def test_employee_Kekaportal():
    driver = webdriver.Chrome(
        executable_path="D:\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://msys.keka.com/")
    time.sleep(5)
    driver.find_element(
        By.XPATH, "//body//div[@class='d-flex vh-100']//div[@class='login-content d-flex flex-column justify-content-between overflow-auto']//div//div//div[2]//button[1]//div[1]//img[1]").click()
    time.sleep(5)
    driver.find_element(By.NAME, "Email").send_keys(user)
    time.sleep(5)
    driver.find_element(By.ID, "password").send_keys(password)
    time.sleep(3)
    driver.find_element(
        By.CSS_SELECTOR, ".btn.btn-primary.mt-10.border-0").click()
    time.sleep(2)
    driver.find_element(
        By.XPATH, "//span[@class='ic-org sidebar-list-icon']").click()
    time.sleep(2)
    driver.find_element(
        By.XPATH, "//body[1]/xhr-app-root[1]/div[1]/xhr-left-nav[1]/nav[1]/div[1]/ul[1]/li[6]/div[1]/ul[1]/li[1]/a[1]").click()
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Employee Directory").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//body/xhr-app-root/div/xhr-org/div/employee-directory/div/employee-org-directory/div/div/div/div[2]").click()
    time.sleep(2)