import pytest
from utilities import actions_os
from pageObjects.FilePortalMainPage import FilePortalMainPage
from tests.constants import Passwords, General


# This test should be performed with the following file 'Enc_with_2_enc.zip'
# ("\\grey4\Share\Sasha\_SASHA\TESTS\Automation\Portal\Test_files\Enc_with_2_enc.zip")

@pytest.mark.usefixtures("setup")
class TestOne:
    # Verifying initial status text
    def test_16763_verifying_initial_status_text(self):
        portal_link = actions_os.sanitize_file_via_dw(self, General.TESTFILE_INVALID_PASSWORD)
        self.driver.get(portal_link)
        file_portal_main_page = FilePortalMainPage(self.driver)
        status = file_portal_main_page.get_status_text()
        assert "Password required" in status.text, '"Password required" message is not displayed'

    # Entering a VALID password for the parent
    def test_16763_entering_valid_password(self):
        file_portal_main_page = FilePortalMainPage(self.driver)
        file_portal_main_page.password_input_parent().send_keys(Passwords.VALID_PASSWORD)
        file_portal_main_page.submit().click()

        # Verifying the status message text
        self.driver.implicitly_wait(120)
        status = file_portal_main_page.get_status_text()
        assert "Password required" in status.text, '"Password required" message is not displayed'

    # Entering an INVALID and VALID password for the children
    def test_16763_entering_invalid_password_to_children(self):
        file_portal_main_page = FilePortalMainPage(self.driver)
        file_portal_main_page.password_input_first_child().send_keys(Passwords.INVALID_PASSWORD)
        file_portal_main_page.password_input_second_child().send_keys(Passwords.VALID_PASSWORD)
        file_portal_main_page.submit().click()

        # Verifying the status message text
        self.driver.implicitly_wait(120)
        status = file_portal_main_page.get_status_text()
        assert "Invalid Password" in status.text, '"Invalid password" message is not displayed'

    # Entering a VALID password for the first child
    def test_16763_entering_valid_password_to_children(self):
        file_portal_main_page = FilePortalMainPage(self.driver)
        file_portal_main_page.password_input_first_child().send_keys(Passwords.VALID_PASSWORD)
        file_portal_main_page.submit().click()

        # Verifying the status message text
        self.driver.implicitly_wait(120)
        status = file_portal_main_page.get_status_text()
        assert "Processed successfully, safe to use" in status.text, '"Processed successfully, safe to use" message ' \
                                                                     'is not displayed '
