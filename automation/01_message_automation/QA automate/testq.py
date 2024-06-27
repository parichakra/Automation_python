import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions, Options
import time
import pytest

# Set up Chrome options for headless mode

# options = ChromeOptions()
# options.add_argument("--headless") # Enable headless mode

driver = webdriver.Chrome()

# Check if the current version of chromedriver exists# and if it doesn't exist, download it automatically,# then add chromedriver to path

test_url = "https://en.wikipedia.org/w/index.php?search"

def test_get_wiki_page():
    driver.get(test_url)
    driver.maximize_window()
    assert driver.title == "Search - Wikipedia"
def test_shah_rukh_khan():
    driver.get(test_url)
    test_id = '//*[@id="ooui-php-1"]'
    click_search = '//*[@id="mw-search-top-table"]/div/div/div/span/span/button'
    time.sleep(7)
    driver.find_element(By.XPATH, test_id).send_keys("Shah Rukh Khan")
    driver.find_element(By.XPATH, click_search).click()
    time.sleep(7)


def test_title_assert():
    driver.get(test_url)
    test_id = '//*[@id="ooui-php-1"]'
    click_search = '//*[@id="mw-search-top-table"]/div/div/div/span/span/button'
    time.sleep(7)
    driver.find_element(By.XPATH, test_id).send_keys("Shah Rukh Khan")
    driver.find_element(By.XPATH, click_search).click()
    assert driver.title == "shah rukh khan - Search results - Wikipedia"
    time.sleep(7)


def test_click_on_main_page():
    xpath_main_page = "/html/body/div[1]/header/div[1]/a"
    main_page_title = "Wikipedia, the free encyclopedia"
    driver.get(test_url)
    driver.maximize_window()
    main_page = driver.find_element(By.XPATH, xpath_main_page)
    main_page.click()
    assert driver.title == main_page_title

test_get_wiki_page()
test_shah_rukh_khan()    
test_title_assert()
test_title_assert()