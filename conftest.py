import pytest
from selenium import webdriver
from selenium.webdriver import Chrome, Firefox


@pytest.fixture
def browser(config):
  if config['browser'] == 'chrome':
    driver = Chrome()
  elif config['browser'] == 'firefox':
    driver = Firefox()
  else:
    raise Exception(f'"{config["browser"]}" is not a supported browser')
  driver.implicitly_wait(config['wait_time'])
  yield driver
  driver.quit()









# @pytest.fixture
# def browser():
#   driver = webdriver.Chrome()
#   driver.implicitly_wait(5)
#   yield driver
#   driver.quit()    