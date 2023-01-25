from selenium.webdriver.common.by import By


class FilePortalMainPage:

    def __init__(self, driver):
        self.driver = driver

    # Password input field for the parent
    def password_input_parent(self):
        return self.driver.find_element(By.ID, "Password")

    # Password input field for the first child
    def password_input_first_child(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[5]/div/form/ul/li/ul/li[1]/input")

    # Password input field for the second child
    def password_input_second_child(self):
        return self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[5]/div/form/ul/li/ul/li[2]/input")

    # Submit button
    def submit(self):
        return self.driver.find_element(By.ID, "Submit")

    # Status (top outcome) message text
    def get_status_text(self):
        status = self.driver.find_element(By.ID, "pageTitle")
        return status

    # Outcome message text
    def get_outcome_text(self):
        outcome = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[5]/div/form/ul/li/ul/*")
        return outcome

    # Error title text
    def get_error_title_text(self):
        error_title = self.driver.find_element(By.ID, "errorTitle")
        return error_title

    # Error reason text
    def get_error_reason_text(self):
        error_reason = self.driver.find_element(By.ID, "errorReason")
        return error_reason
