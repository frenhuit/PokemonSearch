import time

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

browser = None


def test_suggestion():
    print('Starts testing suggestions...')
    browser.get('http://127.0.0.1:8000/')
    time.sleep(5)
    browser.find_element(By.XPATH, '//input[@class="searchInput"]').send_keys('Squirtle')
    time.sleep(3)
    suggestion_list = browser.find_elements(By.XPATH, '//ul[@class="dataList"]/li')
    first_suggestion_text = suggestion_list[0].find_element(By.XPATH, '//a').text
    assert first_suggestion_text == 'Squirtle (Pokémon)'
    print('Passed.')


def test_search_result():
    print('Starts testing search results...')
    browser.get('http://127.0.0.1:8000/')
    time.sleep(5)
    browser.find_element(By.XPATH, '//input[@class="searchInput"]').send_keys('Squirtle (Pokémon)')
    time.sleep(3)
    browser.find_element(By.XPATH, '//input[@type="button" and @class="searchButton"]').click()
    time.sleep(5)
    results = browser.find_elements(By.XPATH, '//div[@class="resultItem"]')
    first_title = results[0].find_element(By.XPATH, '//div[@class="itemHead"]//span[@class="keyWord"]').text
    assert first_title == 'Squirtle (Pokémon)'
    print('Passed.')


if __name__ == '__main__':
    option = uc.ChromeOptions()
    prefs = {'intl.accept_languages': 'en, en_US'}
    option.add_experimental_option('prefs', prefs)
    option.add_argument('--ignore-ssl-errors=yes')
    option.add_argument('--ignore-certificate-errors')
    browser = uc.Chrome(options=option)

    test_suggestion()
    test_search_result()

    print('All passed.')
    browser.quit()
