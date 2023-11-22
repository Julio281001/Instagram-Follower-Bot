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
    
  
  def find_account(self, account):
    
    time.sleep(5)
    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div').click()
    time.sleep(5)
    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input').send_keys(account)
    time.sleep(5)
    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]/div/div/div[2]/div/div').click()
    time.sleep(10)
    self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a').click()
  

  def follow(self):
    counter = 1
    while True:
      time.sleep(10)
      try:
        self.driver.find_element(By.XPATH, f'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div/div/div[{counter}]/div/div/div/div[3]/div/button').click()
        try:
          self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]').click()
        except:
          pass
      except :
        break
      counter += 1