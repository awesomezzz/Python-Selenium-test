import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
from BeautifulReport import BeautifulReport


options = webdriver.ChromeOptions()

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self): 
        self.driver = webdriver.Chrome(chrome_options=options)
        self.action = ActionChains(self.driver)
        self.URL = "https://mis.twse.com.tw/stock/index.jsp"
        self.driver.get(self.URL)
        self.driver.maximize_window()
    
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        
    def test_0050(self):
      """
        前往基本市況報導網站後，搜尋"0050"成交價量及最佳五檔價量資訊
        """
      self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/form/input[1]").send_keys("0050")
      time.sleep(2)
      self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]/form/input[2]").click()
      time.sleep(5)

basedir = "D:/000_Python_Selenium/TC2_Stock/"
if __name__ == '__main__':
    test = unittest.defaultTestLoader.discover(basedir, pattern='*.py')
    result = BeautifulReport(test)
    result.report(filename='Report_TC2',description='Stock Exchange about search 0050', log_path='D:/000_Python_Selenium/TC2_Stock/')
                 