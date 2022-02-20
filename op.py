from datetime import date
custoop1 = [("Janeiro",0.45),("Fevereiro",0.43),("Março",0.43),("Abril",0.43),("Maio",0.413)]

meses = [(1,31,1,0.45),(1,28,2,0.43),(1,31,3,0.43),(1,30,4,0.43),(1,31,5,0.413)]

j = 0

op = 0
opplus = 0
custoop = 0
dias = 0

diaini = int(input("Digite o dia de entrada"))
mesini = int(input("Digite o mes de entrada"))
anoini = int(input("Digite o ano de entrada"))

diafim = int(input("Digite o dia de saída"))
mesfim = int(input("Digite o mes de saída"))
anofim = int(input("Digite o ano de saída"))

dataini = date(year=anoini, month=mesini, day=diaini)

for i in meses:

    if mesini > meses[j][2] or mesfim < meses[j][2]:
        op = 0
        print('\n',op)
    elif mesini == meses[j][2]:
        op = meses[j][1] - diaini + 1
        print('\n',op)
        dias = dias + op
        custoop = op * meses[j][3]
        opplus = opplus + custoop
    elif mesini < meses[j][2] and mesfim > meses[j][2]:
        op = meses[j][1] - meses[j][0] + 1 
        print('\n',op)
        dias = dias + op
        custoop = op * meses[j][3]
        opplus = opplus + custoop
    else:
        op = diafim - meses[j][0] + 1
        print('\n',op)
        dias = dias + op
        custoop = op * meses[j][3]
        opplus = opplus + custoop
    
    j = j + 1

print("Dias: ", dias, "\n", "Custo op total:", opplus, "Custo op médio:", f'{(opplus/dias):.3f}')

'''
if mesini > mesfim:
    mesfim = mesfim - 12
'''
