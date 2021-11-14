from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-14-noiembrie-ora-13-00-2/")
table = browser.find_element_by_xpath('//table[@width="0"]')
table_text = table.text
lista = table_text.split('\n')
print(lista)
header = browser.find_element(By.XPATH, '//table[@width="0"]/tbody/tr').text.split('\n')
dictionar = {i: [] for i in header}
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionar[header[int(j)]].append(lista[i])
print(dictionar)

df = pd.DataFrame(dictionar)
df.to_csv("covid.csv")
time.sleep(2)
browser.close()