import win32com.client as win32

vendedores2 = [("Gustavo Perez", "gustavo.perez@msfoods.agr.br")]

outlook = win32.Dispatch('outlook.application')
email = outlook.CreateItem(0)

email.To = f""
email.Subject = "PEDIDO TECNO FOODS 22/11 - 21"  # assunto
email.HTMLBody = f"""
<p>Bom dia Rebeca,</p>

<p>Segue novo pedido TECNO FOODS-FOB.</p>

<p>Fico no aguardo da confirmação de recebimento e favor programar retirada para o dia 17/12(sexta-feira), conforme está no pedido.</p>

<p>Sem observação.</p>

<p>Atenciosamente Gustavo Perez!</p>
"""
anexo = f"C:/Users/TEMP/Desktop/MONITORES/Nova pasta/2021 11 22 Formulário de Pedidos - TECNO FOODS - FOB - 21.xlsx"
email.Attachments.Add(anexo)

email.Send()

print("E-mail enviado!")