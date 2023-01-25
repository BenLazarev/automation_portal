import pytest
from utilities import actions_os
from pageObjects.FilePortalMainPage import FilePortalMainPage
from tests.constants import Passwords, General
from utilities.BaseClass import BaseClass


# This test should be performed with the following file 'xsl_enc.zip'
# ("\\grey4\Share\Sasha\_SASHA\TESTS\Automation\Portal\Test_files\xsl_enc.zip")

@pytest.mark.usefixtures("setup")
# class TestOne(BaseClass):
class TestOne:
    # Verifying initial status text
    def test_17607_verifying_initial_status_text(self):
        portal_link = actions_os.sanitize_file_via_dw(self, General.TESTFILE_ENC_ARCHIVE_XLS)
        self.driver.get(portal_link)
        file_portal_main_page = FilePortalMainPage(self.driver)
        status = file_portal_main_page.get_status_text()
        assert "Password required" in status.text, '"Password required" message is not displayed'

    # Entering an INVALID password for the parent
    def test_17607_entering_invalid_password(self):
        file_portal_main_page = FilePortalMainPage(self.driver)
        file_portal_main_page.password_input_parent().send_keys(Passwords.INVALID_PASSWORD)
        file_portal_main_page.submit().click()

        # Verifying the status message text
        self.driver.implicitly_wait(120)
        status = file_portal_main_page.get_status_text()
        assert "Invalid Password" in status.text, '"Invalid password" message is not displayed'

    # Entering a VALID password for the parent
    def test_17607_entering_valid_password(self):
        file_portal_main_page = FilePortalMainPage(self.driver)
        file_portal_main_page.password_input_parent().send_keys(Passwords.VALID_PASSWORD)
        file_portal_main_page.submit().click()

        # Verifying the status message text
        self.driver.implicitly_wait(120)
        status = file_portal_main_page.get_status_text()
        assert "Password required" in status.text, '"Password required" message is not displayed'

    # Entering an INVALID password for the child
    def test_17607_entering_invalid_password_to_children(self):
        file_portal_main_page = FilePortalMainPage(self.driver)
        file_portal_main_page.password_input_first_child().send_keys(Passwords.INVALID_PASSWORD)
        file_portal_main_page.submit().click()

        # Verifying the status message text
        self.driver.implicitly_wait(120)
        status = file_portal_main_page.get_status_text()
        assert "Invalid Password" in status.text, '"Invalid password" message is not displayed'

    # Entering a VALID password for the child
    def test_17607_entering_valid_password_to_children(self):
        file_portal_main_page = FilePortalMainPage(self.driver)
        file_portal_main_page.password_input_first_child().send_keys(Passwords.VALID_PASSWORD)
        file_portal_main_page.submit().click()

        # Verifying the status message text
        self.driver.implicitly_wait(120)
        status = file_portal_main_page.get_status_text()
        assert "Processed successfully, safe to use" in status.text, '"Processed successfully, safe to use" message ' \
                                                                     'is not displayed '
