import pytest


@pytest.yield_fixture()

def setUp():
    print('running method level')
    yield
    print('teardown method level')

@pytest.yield_fixture(scope='class')
def oneTimeSetUp(browser):
    print('running onetime')
    if browser == 'firefox':
        print('running in firefox')
    else:
        print('running in chrome')
    yield
    print('running one time teardown')

def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--osType', help='Type of os')

@pytest.yield_fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')
@pytest.yield_fixture(scope='session')
def osType(request):
    return request.config.getoption('--osType')

