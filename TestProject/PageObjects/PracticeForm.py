'''
Created on 02-Jul-2018

@author: adityaj
'''

from selenium.webdriver.common.by import By
from PageObjects.InitDriver import InitDriver
from selenium.webdriver.support.select import Select

class PracticeForm(InitDriver):
    
    firstName = (By.XPATH, "//input[@name='firstname']")
    lastName = (By.XPATH, "//input[@name='lastname']")
    maleSex = (By.ID, 'sex-0')
    femaleSex = (By.ID, 'sex-1')
    date = (By.XPATH, "//input[@id='datepicker']")
    professionManual = (By.XPATH, "//input[@id='profession-0']")
    professionAutomation = (By.XPATH, "//input[@id='profession-1']")
    toolQTP = (By.XPATH, "//input[@value='QTP']")
    toolSelIDE = (By.XPATH, "//input[@value='Selenium IDE']")
    toolWebDriver = (By.XPATH, "//input[@value='Selenium Webdriver']")
    continentsDrop = (By.XPATH, "//select[@id='continents']")
    SelCommandsCombo = (By.XPATH, "//select[@id='selenium_commands']")
    submitButton = (By.XPATH, "//button[@id='submit']")
    testLink = (By.XPATH, "//a//strong[text()='Link Test']")
    downloadFramework = (By.XPATH, "//a[text()='Test File to Download']")

    def set_firstname(self, firstname):
        self.webdriver.find_element(*self.firstName).send_keys(firstname)

    def set_lastname(self, lastname):
        self.webdriver.find_element(*self.lastName).send_keys(lastname)
    
    def set_gender(self, gender):
        if(gender == "male"):
            self.webdriver.find_element(*self.maleSex).click()
        elif(gender == "female"):
            self.webdriver.find_element(*self.femaleSex).click()
        else:
            print("Invalid gender type")
    
    def set_exp(self, exp):
        self.webdriver.find_element(*(By.ID, "exp-"+ str(exp-1))).click()
    
    def set_date(self, dob):
        self.webdriver.find_element(*self.date).send_keys(dob)

    def set_profession(self, prof):
        if(prof == "manual"):
            self.webdriver.find_element(*self.professionManual).click()
        elif(prof == "automation"):
            self.webdriver.find_element(*self.professionAutomation).click()
        else:
            print("Invalid choice")
            
    def download_framework(self):
        self.webdriver.find_element(*self.downloadFramework).click()

    def set_tool(self):
        self.webdriver.find_element(*self.toolWebDriver).click()

    def set_continent(self, continent="Asia"):
        select = Select(self.webdriver.find_element(*self.continentsDrop))
        select.select_by_visible_text(continent)

    def set_commands(self):
        selCombo = Select(self.webdriver.find_element(*self.SelCommandsCombo))
        if (selCombo.is_multiple):
            selCombo.select_by_visible_text("Navigation Commands")
            selCombo.select_by_visible_text("Browser Commands")
            
    def navigateToTestLink(self):
        self.webdriver.find_element(*self.testLink).click()

    def submit(self):
        self.webdriver.find_element(*self.submitButton).click()
