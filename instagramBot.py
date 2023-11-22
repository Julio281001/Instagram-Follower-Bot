from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv

class InstagramBot:
  
  
  def __init__(self):
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    self.driver = webdriver.Chrome(options=options)
    
    
  def sign_in(self):
    
    load_dotenv()
    self.driver.get('https://www.instagram.com/')
    time.sleep(5)
    self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(os.getenv('EMAIL'))
    time.sleep(5)
    self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(os.getenv('PASSWORD'))
    time.sleep(5)
    self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()