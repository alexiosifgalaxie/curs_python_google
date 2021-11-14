from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(By.ID, 'searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()
# product = browser.find_element((By.ID, 'card_grid')
product = browser.find_element(By.CLASS_NAME, 'card-item')
print(product.text)
