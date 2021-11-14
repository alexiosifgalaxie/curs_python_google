from selenium import webdriver
# from selenium.webdriver.common.by import By    ce mai e comentat imd mai jos se leaga de asta
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
table = browser.find_element_by_xpath('//*[@id="Data_table"]')
# table = browser.find_element(By.XPATH,'//*[@id="Data_table"]')
table_text = table.text
lista = table_text.split('\n')
print(lista)
header = browser.find_element_by_xpath('//*[@id="Data_table"]/table/thead/tr').text.split('\n')
dictionar = {i: [] for i in header}  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(header.text.split('\n')) #split returneaza lista
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        dictionar[header[int(j)]].append(lista[i])
print(dictionar)

df = pd.DataFrame(dictionar)
df.to_csv("BNR-ALL-DATA.csv")
time.sleep(2)
browser.close()
