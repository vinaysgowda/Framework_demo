import pytest
from selenium import webdriver


def Login():
    _username = 'username'
    _password = 'password'
    _login_button = '//*[contains(text(),"Log in")]'
    _submit_button = "//input[@type = 'submit']"
    _project_button = '//*[contains(text(),"Your projects (0)")]'

    def __init__(self):
        global driver
        driver = webdriver.Chrome()


    def login_to_account(self):
        driver.get('https://pypi.org/')
        driver.find_element_by_xpath(_login_button)
        driver.find_element_by_id('_username').send_keys('govind3011')
        driver.find_element_by_id('_password').send_keys('govind@3011')
        driver.find_element_by_xpath(_submit_button).click()
        print('login successful')

    def verify_login(self):

        driver.find_element_by_xpath(_project_button).is_displayed()
