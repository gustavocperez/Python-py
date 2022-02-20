import quandl
import pandas as pd
import numpy as np
import tabula
from openpyxl import load_workbook

df = pd.DataFrame()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

quandl.ApiConfig.api_key = '2Ai364RsjrHwe-CbVKdx'

SELIC = quandl.get('BCB/4189', start_date='2000-01-01')
IPCA = quandl.get('BCB/13522', start_date='2000-01-01')
DOLAR = quandl.get('BCB/3697', start_date='2000-01-01')
PIB = quandl.get('BCB/24364', start_date='2000-01-01')

df_final = pd.concat([IPCA, SELIC, PIB, DOLAR], axis=1)

df_final = df_final.set_axis(['IPCA', 'SELIC', 'PIB', 'DOLAR'], axis=1, inplace=False)

print(df_final)

nome_arquivo = "arquivo_rafael.xlsx"

df_final.to_excel(nome_arquivo)

workbook = load_workbook(filename=nome_arquivo)
ws = workbook.active

workbook.save(filename=nome_arquivo)

