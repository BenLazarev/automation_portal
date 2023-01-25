import glob
import os
import shutil
import time
from utilities import actions_web, actions_os
from pathlib import Path
from tests.constants import General


def sanitize_file_via_dw(self, file_path):
    actions_os.start_service(General.SERVICE_NAME_CLIENT)
    time.sleep(General.TIMEOUT_SHORT)
    actions_os.copy_a_file(file_path, General.DW_INPUT)
    assert actions_os.file_exist(General.DW_OUT + Path(file_path).name + r'.fail.html',
                                 General.TIMEOUT_MEDIUM)
    portal_link = actions_web.get_portal_link(self, General.DW_OUT, Path(file_path).name
                                              + r'.fail.html', General.CORE_SERVER)
    return portal_link


def copy_all_files(source, destination):
    allfiles = os.listdir(source)
    for f in allfiles:
        shutil.copy2(source + f, destination + f)
        # using use shutil.copy2() to preserve timestamp


def copy_a_file(sourcefile, destination):
    shutil.copy2(sourcefile, destination + Path(sourcefile).name)
    time.sleep(2)
    # using use shutil.copy2() to preserve timestamp


def clean_folder(path):
    files = glob.glob(path +'*')
    for f in files:
        os.remove(f)


def start_service(svc):
    os.system(f'net start {svc}')


def stop_service(svc):
    os.system(f'net stop {svc}')


def file_exist(path, timeout):
    start = time.time()
    exists = os.path.exists(path)

    while not exists:
        time.sleep(1)
        exists = os.path.exists(path)
        elapsed = time.time() - start
        if elapsed >= timeout:
            return False
    return True

