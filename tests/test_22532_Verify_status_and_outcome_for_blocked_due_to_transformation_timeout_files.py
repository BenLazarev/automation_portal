import pytest
from utilities import actions_os
from pageObjects.FilePortalMainPage import FilePortalMainPage
from tests.constants import Passwords, Outcomes, General


# This test should be performed with the following file
# 'VAX-HR-6522-170-9-HAG-02.zip'
# ("\\grey4\Share\Sasha\_SASHA\TESTS\Automation\Portal\Test_files\VAX-HR-6522-170-9-HAG-02.zip")

@pytest.mark.usefixtures("setup")
class TestOne:
    # Verifying initial status text
    def test_22532_verifying_initial_status_text(self):
        portal_link = actions_os.sanitize_file_via_dw(self, General.TESTFILE_CDR_TIMEOUT)
        self.driver.get(portal_link)
        file_portal_main_page = FilePortalMainPage(self.driver)
        status = file_portal_main_page.get_status_text()
        assert "Password required" in status.text, '"Password required" message is not displayed'

    # Verifying the status (top)
    def test_22532_verifying_status(self):
        # Entering a VALID password (for the parent)
        file_portal_main_page = FilePortalMainPage(self.driver)
        file_portal_main_page.password_input_parent().send_keys(Passwords.VALID_PASSWORD)
        file_portal_main_page.submit().click()

        # Verifying the status message text
        self.driver.implicitly_wait(360)
        status = file_portal_main_page.get_status_text()
        assert "Transformation timeout" in status.text, '"Transformation timeout" message is not displayed'

    # Verifying the outcome
    def test_22532_verifying_outcome(self):
        file_portal_main_page = FilePortalMainPage(self.driver)
        outcome = file_portal_main_page.get_outcome_text()
        assert Outcomes.OUTCOME_161 in outcome.text, Outcomes.OUTCOME_161 + ' message is not displayed'
