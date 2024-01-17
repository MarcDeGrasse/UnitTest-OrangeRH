# -*- coding: utf-8 -*-
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test1Inscription(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
          # Maximisez la fenêtre du navigateur
        self.driver.maximize_window()
    # et pour les screenshots:
        time.sleep(5)
        driver.save_screenshot("screenshot-avant.png")
        time.sleep(5)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1_inscription(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/header/div/div[2]/ul/li/span/p").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.LINK_TEXT, "Recruitment").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate")
        driver.find_element(By.NAME, "firstName").click()
        driver.find_element(By.NAME, "firstName").clear()
        driver.find_element(By.NAME, "firstName").send_keys("Marco")
        driver.find_element(By.NAME, "middleName").click()
        driver.find_element(By.NAME, "middleName").clear()
        driver.find_element(By.NAME, "middleName").send_keys("DelDago")
        driver.find_element(By.NAME, "firstName").click()
        driver.find_element(By.NAME, "firstName").clear()
        driver.find_element(By.NAME, "firstName").send_keys("Marco 1")
        driver.find_element(By.NAME, "middleName").click()
        driver.find_element(By.NAME, "middleName").clear()
        driver.find_element(By.NAME, "middleName").send_keys("DelDago1")
        driver.find_element(By.NAME, "lastName").click()
        driver.find_element(By.NAME, "lastName").clear()
        driver.find_element(By.NAME, "lastName").send_keys("Alfonso")
        driver.find_element(By.NAME, "lastName").clear()
        driver.find_element(By.NAME, "lastName").send_keys("Alfonso1")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").send_keys("DelDago@gmail.com")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input").send_keys("0123456789")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[6]/div/div/div/div[2]/textarea").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[6]/div/div/div/div[2]/textarea").clear()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[6]/div/div/div/div[2]/textarea").send_keys("Be here")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[7]/div/div/div/div[2]/div/label/span/i").click()
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/changeCandidateVacancyStatus?candidateId=46&selectedAction=2")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li[5]/a/span").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div/div/div/label/span/i").click()
        driver.find_element(By.XPATH, "//div[@id='app']/div/div/header/div/div[2]/ul/li/span/i").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").clear()
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys("admin123")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
