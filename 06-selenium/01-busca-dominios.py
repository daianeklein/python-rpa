from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

print('Iniciando...')

#config
path = '/Users/daianeklein/Documents/DS/python-rpa/python-rpa/06-selenium/chrome-web-driver/'
service = Service(executable_path=path + "chromedriver")
driver = webdriver.Chrome(service=service)

# Looking for the domain availability
dominios = ['roboscompython.com.br', 'www.uol.com.br', 'www.pythonabc123.com.br', 'www.udemy.com']

for dominio in dominios:
    driver.get("https://registro.br/")
    time.sleep(2)

    pesquisa = driver.find_element(By.ID, "is-avail-field")
    pesquisa.clear()
    pesquisa.send_keys(dominio)
    time.sleep(2)

    # Save the current result element before submitting the form
    result_locator = (By.XPATH, "//p[contains(@class, 'font-3') and contains(@class, 'is-avail-response')]/span/strong")
    old_result = driver.find_element(*result_locator)
    old_text = old_result.text

    # Submit the form
    pesquisa.submit()
    time.sleep(3)

    try:
        # Wait for the result to change
        wait = WebDriverWait(driver, 20) # Increase timeout to 20 seconds
        wait.until(EC.text_to_be_present_in_element(result_locator, old_text), message=f"Result didn't change for domain {dominio}")

        # Wait for the new result to become visible
        results = driver.find_element(*result_locator)
        time.sleep(3)

        # Getting the results
        text_result = results.text
        print(dominio, text_result)
        time.sleep(3)

    except TimeoutException as e:
        print(f"Timeout while processing domain: {dominio}")
        print(str(e))
        continue

time.sleep(5)
driver.close()
