from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

url = ''
req = requests.get(url)
print(req)

soup = BeautifulSoup(req.text,"html.parser")

ul = soup.find("ul", {"class": "provincias"})

enlace = []
local = []
numero = []

for li in ul.find_all("li"):
    a = li.find("a")

    enlace.append(a.get("href"))
    local.append(a.text)

    print(li.text)
    match = re.match(r".+\(([0-9.]+) Empresas\)", li.text, re.I)
    item = ""
    if match:
        item = match.groups()[0]
    print(item)

    numero.append(item.replace(".", ""))
    print(numero)

listado_empresas = pd.DataFrame({

    "Localidad" : local,

    "Numero de Empresas" : numero,

    "Enlace": enlace

})
listado_empresas.set_index('Localidad',inplace=True)

listado_empresas[0 :10]

listado_empresas.to_csv()

print (listado_empresas)