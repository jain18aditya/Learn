'''
Created on 04-Jul-2018

@author: adityaj
'''
from selenium.webdriver.common.by import By
from PageObjects.InitDriver import InitDriver

class PracticeTbl(InitDriver):
    
    columnHeader = (By.XPATH, "//th[@scope='col']")
    data = (By.XPATH, "//tbody/tr/td")
    structure = (By.XPATH, "//tbody/tr/th")
#    //th[@scope='row'][contains(text(),'Burj Khalifa')]/parent::tr/td
    
    def getValue(self, height, structure):
        col = self.webdriver.find_elements(*self.columnHeader)
        colSize = col.__len__()
        print(colSize)
        structureName = self.webdriver.find_elements(*self.structure)
        rowSize = structureName.__len__()
        print(rowSize)
        dataText = self.webdriver.find_elements(*self.data)
        for i in range(colSize):
            print(col[i].text)
            if (col[i].text == height):
                expectedColumn = i
        for i in range(rowSize):
            expectedRow = i
            if(structureName[i].text == structure):
                break
        print("colSize:",colSize,"-expectedRow:",expectedRow,"-expectedColumn:",expectedColumn)
        print(dataText[((colSize-1)*expectedRow)+expectedColumn-1].text)
