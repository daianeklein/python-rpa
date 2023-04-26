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
driver.get("https://registro.br/")

time.sleep(2)

# Looking for the domain availability
pesquisa = driver.find_element(By.ID, "is-avail-field")
pesquisa.clear()
pesquisa.send_keys('roboscompython.com.br')
time.sleep(2)

# Save the current result element before submitting the form
old_result = driver.find_element(By.XPATH, "//p[contains(@class, 'font-3') and contains(@class, 'is-avail-response')]/span/strong")

# Submit the form
pesquisa.submit()

# Wait for the old result to become stale
wait = WebDriverWait(driver, 10)
wait.until(EC.staleness_of(old_result))

# Wait for the new result to become visible
results = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'font-3') and contains(@class, 'is-avail-response')]/span/strong")))

# Getting the results
text_result = results.text
print(text_result)

time.sleep(5)
driver.close()