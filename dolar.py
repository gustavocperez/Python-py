from selenium import webdriver
from datetime import date
from openpyxl import load_workbook

data_atual1 = date.today()

# definir navegador e abrir o chrome
navegador = webdriver.Chrome("C:/Users/TEMP/Desktop/DolarPTAX/chromedriver.exe")

# entrar no site do banco central
navegador.get("https://www.bcb.gov.br/")

# acha o valor do Dolar PTAX de compra pelo xpath
navegador.find_element_by_xpath('/html/body/app-root/app-root/main/dynamic-comp/div/div/div/div[1]/div[1]/div/cotacao/table[1]/tbody/tr[1]/td[2]/span')

element = navegador.find_element_by_xpath(
    '/html/body/app-root/app-root/main/dynamic-comp/div/div/div/div[1]/div[1]/div/cotacao/table[1]/tbody/tr[1]/td[2]/span')

# salva o valor do Dolar PTAX
html_content = element.get_attribute('outerHTML')

# acha o valor do Dolar PTAX de venda pelo xpath
navegador.find_element_by_xpath('/html/body/app-root/app-root/main/dynamic-comp/div/div/div/div[1]/div[1]/div/cotacao/table[1]/tbody/tr[1]/td[3]/span')

element2 = navegador.find_element_by_xpath(
    '/html/body/app-root/app-root/main/dynamic-comp/div/div/div/div[1]/div[1]/div/cotacao/table[1]/tbody/tr[1]/td[3]/span')

html_content2 = element2.get_attribute('outerHTML')

dolarp = str("Dolar PTAX COMPRA: ")

linha = ("\n")

# "abre" a planilha do excel
workbook = load_workbook(filename="G:/Outros computadores/Meu modelo Laptop (1)/DolarPTAX/DOLARPTAX.xlsx")
sheet = workbook.active

preco = 0
precof = 0
precoff = 0
preco2 = 0
precof2 = 0
precoff2 = 0

# separa o lixo que vem junto com o valor do XPATH
linguagens = html_content.split('>')
linguagens2 = html_content2.split('>')
for i in linguagens:
    preco = linguagens

ling = preco[1].split('<')
for i in ling:
    precof = ling

precoff = precof[0]

linguagens = html_content2.split('>')
for i in linguagens2:
    preco2 = linguagens2

ling2 = preco2[1].split('<')
for i in ling2:
    precof2 = ling2

precoff2 = precof2[0]

row = 1
col = "A"

cel = ("%s%d" % (col, row))

# acha a última célula vazia no excel
while sheet[cel].value is not None:
    row = row + 1
    cel = ("%s%d" % (col, row))

sheet[cel].value = data_atual1
col = "B"
cel = ("%s%d" % (col, row))
sheet[cel].value = precoff

col = "C"
cel = ("%s%d" % (col, row))
sheet[cel].value = precoff2

workbook.save(filename="G:/Outros computadores/Meu modelo Laptop (1)/DolarPTAX/DOLARPTAX.xlsx")

navegador.quit()
