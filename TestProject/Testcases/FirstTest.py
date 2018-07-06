'''
Created on 02-Jul-2018

@author: adityaj
'''
from selenium import webdriver
import unittest
from PageObjects.PracticeForm import PracticeForm
from PageObjects.PracticeTable import PracticeTbl
from time import sleep

class PracticeFormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        '''chromedriver = "C:/Users/adityaj/Downloads/Driver/Chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver)'''
        
    def tearDown(self):
        self.driver.close()

    def testUserSubmit(self):
        driver = self.driver
        driver.get("http://toolsqa.com/automation-practice-form/")
        driver.maximize_window()
        practiceForm = PracticeForm(self.driver)
        practiceForm.set_firstname("Aditya")
        practiceForm.set_lastname("Jain")
        practiceForm.set_gender("male")
        practiceForm.set_exp(5)
        practiceForm.set_date("18 August,1991")
        practiceForm.set_profession("automation")
        practiceForm.download_framework()
        practiceForm.set_tool()
        practiceForm.set_continent("Asia")
        practiceForm.set_commands()
        sleep(10)

    def testReadTable(self):
        driver = self.driver
        driver.get("http://toolsqa.com/automation-practice-form/")
        driver.maximize_window()
        practiceForm = PracticeForm(self.driver)
        practiceForm.navigateToTestLink()
        practiceTable = PracticeTbl(self.driver)
        practiceTable.getValue("Rank", "Financial Center")                    

