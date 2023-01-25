import pytest

from selenium.webdriver.common.by import By

from pageObjects.FilePortalMainPage import FilePortalMainPage
from utilities.BaseClass import BaseClass
import time


@pytest.mark.usefixtures("setup")
class TestOne:
    def test_(self):
        self.driver.get(
        "https://server33:4507/portal/file/11761/2EEC1B13E211397740D87854BF5C2DF7E396B9F99045BA1B003EB2B7E9EBFD3A")
        file_portal_main_page = FilePortalMainPage(self.driver)

        # self.driver.find_element(By.XPATH, '//*[@id="list"]/li/ul/li[1]/input').send_keys("2222")
        # self.driver.find_element(By.XPATH, '//*[@id="list"]/li/ul/li[2]/input').send_keys("2222")
        # file_portal_main_page.password_input().send_keys("2222")
        # self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[5]/div/form/ul/li/ul/li[2]/input")

        # self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[5]/div/form/ul/li/ul/li/span")
        # self.driver.find_element(By.ID, "Submit").click()
        # file_portal_password_page.password_input().send_keys("2222")
        # file_portal_main_page.submit().click()
        #
        # self.driver.implicitly_wait(120)
        # outcome1 = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[5]/div/form/ul/li/ul/li/span")
        outcome = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[5]/div/form/ul/li/ul/*")
        # status = file_portal_password_page.get_status_text()
        # assert "File is Infected" in outcome1.text, '"File is Infected" message in outcome1 is not displayed'
        # assert "Invalid password" in outcome.text, '"Invalid password" message is not displayed'
        assert "Modified" in outcome.text, '"Modified" message is not displayed'
