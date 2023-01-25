import pytest
from utilities import actions_os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from tests.constants import General

from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument("ignore-certificate-errors")
    options.add_argument("start-maximized")

    # next line added to avoid
    #   "USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection:
    #    A device attached to the system is not functioning. (0x1F)"
    # error
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    #service_obj = Service("C:\\_SASHA\\Automation\\webdrivers\\chromedriver.exe")
    #driver = webdriver.Chrome(service=service_obj, options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # driver.get(
    # "https://server33:4507/portal/file/8534/EC03913D2D8A4871D59BB5B7B8073EA520A457666FDE610D6C62BA8641B9DDF8")

    request.cls.driver = driver

    #clean DW out folder
    actions_os.clean_folder(General.DW_OUT)

    yield
    actions_os.stop_service(General.SERVICE_NAME_CLIENT)
    driver.quit()
