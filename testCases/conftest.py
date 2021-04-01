from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path=r"D:\Drivers\chromedriver.exe")
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path=r"D:\Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
        print("Launching firefox browser.........")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser", action = 'store',default="chrome",
        help="my option: chrome or firefox")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")