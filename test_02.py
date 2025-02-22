import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tc1(self):
    self.driver.get("https://www...com/")
    self.driver.set_window_size(1245, 863)
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").send_keys("devops")
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    self.driver.find_element(By.LINK_TEXT, "Devops").click()
    self.driver.save_screenshot("test01.jpg")
    self.driver.find_element(By.CSS_SELECTOR, ".lp-zapisz-btn > a").click()
    #self.driver.find_element(By.XPATH("/html/body/div[3]/div[1]/div/div[2]/div[2]")).click()
