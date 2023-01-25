import pytest
from utilities import actions_os
from tests.constants import  General

from pageObjects.FilePortalMainPage import FilePortalMainPage


# This test should be performed with a link without the signature

@pytest.mark.usefixtures("setup")
class TestOne:
    # Verifying the error status text
    def test_16759_verifying_error_status_text(self):
        portal_link = actions_os.sanitize_file_via_dw(self, General.TESTFILE_ENCRYPTED)
        self.driver.get(portal_link[:-5])

        file_portal_main_page = FilePortalMainPage(self.driver)
        error_title = file_portal_main_page.get_error_title_text()
        assert "An error has occured" in error_title.text, '"An error has occured" message is not displayed'

    # Verifying the error reason text
    def test_16759_verifying_error_reason(self):
        file_portal_main_page = FilePortalMainPage(self.driver)
        error_reason = file_portal_main_page.get_error_reason_text()
        assert "Invalid URL" in error_reason.text, '"Invalid URL" message is not displayed '
