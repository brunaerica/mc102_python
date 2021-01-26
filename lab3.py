#LAB CORRETO

salario = float(input())
ir = float(0.00)
inss = float(0.00)


if salario<= 1045.00:
    inss = salario*0.075
elif salario>=1045.01 and salario<=2089.60:
    inss = salario*0.09
elif salario>=2089.61 and salario<=3134.40:
    inss = salario*0.12
elif salario>=3134.41 and salario<=6101.06:
    inss = salario*0.14
else:
    inss = 6101.06*0.14


#calculo do desconto de IR

dif = salario-inss;


if dif<= 1903.98:
    ir = 0.00
elif dif>=1903.99 and dif<=2826.65:
    ir = dif*0.075 - 142.80
elif dif>=2826.66 and dif<=3751.05:
    ir = dif*0.15 - 354.80
elif dif>=3751.06 and dif<=4664.68:
    ir = dif*0.225 - 636.13
else:
    ir =dif*0.275 -869.36


liquido = salario - (inss+ir)
#Resultados

print("Bruto: R$", "{:.2f}".format(round(salario, 2)).replace('.',','))
print("Bruto: R$", "{:.2f}".format(round(salario, 2)).replace('.',','))
print("Desconto INSS: R$", "{:.2f}".format(round(inss, 2)).replace('.',','))
print("Desconto IR: R$" , "{:.2f}".format(round(ir, 2)).replace('.',','))
print("Líquido: R$" , "{:.2f}".format(round(liquido, 2)).replace('.',','))
