import pytest

from pageObjects.FilePortalMainPage import FilePortalMainPage


# This test should be performed for the sanitization with removed stored files

@pytest.mark.usefixtures("setup")
class TestOne:
    # Verifying the error status text
    def test_16758_verifying_error_status_text(self):
        self.driver.get(
            "https://server33:4507/portal/file/11760/6F4156C5F9C023FDE8D579ABEA4553D2FC20CE345ABE310D33D64AE50822A810")
        file_portal_main_page = FilePortalMainPage(self.driver)
        error_title = file_portal_main_page.get_error_title_text()
        assert "An error has occured" in error_title.text, '"An error has occured" message is not displayed'

    # Verifying the error reason text
    def test_16758_verifying_error_reason(self):
        file_portal_main_page = FilePortalMainPage(self.driver)
        error_reason = file_portal_main_page.get_error_reason_text()
        assert "Missing or invalid sanitization" in error_reason.text, '"Missing or invalid sanitization" message is ' \
                                                                       'not displayed '
