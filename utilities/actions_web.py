import time
from selenium.webdriver.common.by import By
from os import listdir
from pathlib import Path


def get_portal_link(self, destination, reportfile, portalServer):
    _report_driver = self.driver
    _report_driver.maximize_window()
    time.sleep(2)
    try:
        for file in listdir(destination):
            if Path(file).name == reportfile:
                file_name = 'file://' + destination + file
                _report_driver.get(file_name)
                portal_link = _report_driver.find_element(By.XPATH, f"//a[contains(@href,{portalServer})]").get_attribute('href')
                return portal_link
    except AssertionError as error:
        print(error)
        _report_driver.quit()
