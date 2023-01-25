import pytest
from utilities import actions_os
from pageObjects.FilePortalMainPage import FilePortalMainPage
from tests.constants import Passwords, General


# This test should be performed with the following file
# 'Encrypted_Damaged_and_txt.zip'
# ("\\grey4\Share\Sasha\_SASHA\TESTS\Automation\Portal\Test_files\Encrypted_Damaged_and_txt.zip")

@pytest.mark.usefixtures("setup")
class TestOne:
    # Verifying initial status text
    def test_22534_verifying_initial_status_text(self):
        portal_link = actions_os.sanitize_file_via_dw(self, General.TESTFILE_CONTENT_REMOVED)
        self.driver.get(portal_link)
        file_portal_main_page = FilePortalMainPage(self.driver)
        status = file_portal_main_page.get_status_text()
        assert "Password required" in status.text, '"Password required" message is not displayed'

    # Verifying the status (top)
    def test_22534_verifying_status(self):
        # Entering a VALID password (for the parent)
        file_portal_main_page = FilePortalMainPage(self.driver)
        file_portal_main_page.password_input_parent().send_keys(Passwords.VALID_PASSWORD)
        file_portal_main_page.submit().click()

        # Verifying the status message text
        self.driver.implicitly_wait(120)
        status = file_portal_main_page.get_status_text()
        assert "Content removed" in status.text, '"Content removed" message is not displayed'
