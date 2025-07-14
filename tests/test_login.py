import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pages.login_page import LoginPage
from utils.webdriver_setup import setup  # 👈 ADD THIS LINE


from utils.logger import get_logger
logger = get_logger()

def test_valid_login(setup):
    logger.info("Launching browser and opening login page")
    driver = setup
    login = LoginPage(driver)
    login.do_login("student", "Password123")
    logger.info("Submitted login credentials")
    assert "Logged In Successfully" in driver.page_source
    logger.info("Login validated successfully")
def test_invalid_login(setup):
    driver = setup
    login = LoginPage(driver)
    login.do_login("wronguser", "wrongpass")
    assert "Your username is invalid!" in driver.page_source or "Invalid" in driver.page_source
