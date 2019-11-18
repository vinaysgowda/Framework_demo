import pytest
from selenium import webdriver
from POM.login import Login


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.log_in = Login()
        print('class lable setup logging in ')
        yield

        print('logging out of PYPI')

    def test_tc124_verify_twitter(self):
        assert self.log_in.login_to_account()
        assert self.log_in.verify_twitter_link() == self.log_in._twitter_url,'ÚRL does not match'



