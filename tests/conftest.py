import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options 

@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome') #use headless if no ui needed
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=960,720')
    options.add_argument('--window-position=-1030,0')
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='..\chromedriver.exe', options=options)
    return driver

@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.macys.com/'
    if request.cls is not None:  #проверка на класс
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()

