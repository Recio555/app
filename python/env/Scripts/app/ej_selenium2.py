from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

import time
import pandas as pd


options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\Users\\hnore\\Downloads\\chromedriver-win64\\cromedriver.exe'

driver = webdriver.Chrome(driver_path, options=options)


driver.set_window_position(200, 0)
driver.maximize_window()
time.sleep(1)

drivet.get('https://eltiempo.es')





































































