import pytest
from utilities import actions_os
from pageObjects.FilePortalMainPage import FilePortalMainPage
from tests.constants import Passwords, Outcomes, General


# This test should be performed with the following file
# 'Encrypted_net.maxicom.android.snake_7937c1ab615de0e71632fe9d59a259cf.zip'
# ("\\grey4\Share\Sasha\_SASHA\TESTS\Automation\Portal\Test_files\Encrypted_net.maxicom.android.snake_7937c1ab615de0e71632fe9d59a259cf.zip")

@pytest.mark.usefixtures("setup")
class TestOne:
    # Verifying initial status text
    def test_22529_verifying_initial_status_text(self):
        portal_link = actions_os.sanitize_file_via_dw(self, General.TESTFILE_INFECTED)
        self.driver.get(portal_link)
        file_portal_main_page = FilePortalMainPage(self.driver)
        status = file_portal_main_page.get_status_text()
        assert "Password required" in status.text, '"Password required" message is not displayed'

    # Verifying the status (top)
    def test_22529_verifying_status(self):
        # Entering a VALID password (for the parent)
        file_portal_main_page = FilePortalMainPage(self.driver)
        file_portal_main_page.password_input_parent().send_keys(Passwords.VALID_PASSWORD)
        file_portal_main_page.submit().click()

        # Verifying the status message text
        self.driver.implicitly_wait(120)
        status = file_portal_main_page.get_status_text()
        assert "Infected" in status.text, '"Infected" message is not displayed'

    # Verifying the outcome
    def test_22529_verifying_outcome(self):
        file_portal_main_page = FilePortalMainPage(self.driver)
        outcome = file_portal_main_page.get_outcome_text()
        assert Outcomes.OUTCOME_200 in outcome.text, Outcomes.OUTCOME_200 + ' message is not displayed'
