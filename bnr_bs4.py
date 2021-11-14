import requests
from bs4 import BeautifulSoup
import pandas as pd #ii zice mentora cand il foloseste

r = requests.get("https://www.bnr.ro/Cursul-de-schimb--7372.aspx")
link = BeautifulSoup(r.text, "html.parser") #merge si xml.parser si altele de genul
#print(link)

title = link.find_all('div', attrs={'class': 'contentDiv'})[0]
#print(title)
header = []
dataset = []
for tr_index in title.find_all('table'):
    for td_index in tr_index.find_all('tr'):
        td_list = []
        if td_index.find_all('th'):
            header = [th_index.get_text() for th_index in td_index.find_all('th')] #mergea si cu .text in loc de .get_text
        for index, td_value in enumerate(td_index.find_all('td')):
            print(index, td_value)
            if index == 0:
                td_list.append(td_value.get_text())
            else:
                td_list.append(float(td_value.get_text().lstrip('   ').replace(',', '.'))) #rstrip pt dreapta
        dataset.append(td_list)
print(dataset)

df = pd.DataFrame(dataset, columns=header)
df.to_csv("CursBNR.xls", header=header)