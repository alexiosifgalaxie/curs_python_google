from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-14-noiembrie-ora-13-00-2/")
judete = browser.find_elements(By.XPATH, '//table[@width="0"]/tbody/tr/td[@width="151"]')
lista_judete= [i.text for i in judete]
lista_judete.append("TOTAL")

dictionar = {lista_judete[0]: lista_judete[slice(1, len(lista_judete))]}
for i in range(14,7,-1):
    browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-"+str(i)+"-noiembrie-ora-13-00-2/")
    if not browser.find_elements(By.XPATH, '//table[@width="0"]/tbody/tr/td[@width="189"]'):
        continue
    column1 = browser.find_elements(By.XPATH, '//table[@width="0"]/tbody/tr/td[@width="189"]')
    column2 = browser.find_elements(By.XPATH, '//table[@width="0"]/tbody/tr/td[@width="161"]')
    column3 = browser.find_elements(By.XPATH, '//table[@width="0"]/tbody/tr/td[@width="162"]')
    lista1 = [i.text for i in column1]
    lista1[0] = lista1[0] + f"({i}.noiembrie)"
    lista2 = [i.text for i in column2]
    lista2[0] = lista2[0] + f"({i}.noiembrie)"
    lista3 = [i.text.replace(',', '.') for i in column3]
    lista3[0] = lista3[0] + f"({i}.noiembrie)"
    dictionar[lista1[0]] = lista1[slice(1, len(lista1))]
    dictionar[lista2[0]] = lista2[slice(1, len(lista2))]
    dictionar[lista3[0]] = lista3[slice(1, len(lista3))]
df = pd.DataFrame(dictionar)
df.to_csv("covid.csv")
time.sleep(2)
browser.close()