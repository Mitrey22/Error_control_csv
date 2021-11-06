import pandas as pd
from funciones_actividad1 import *
import operator
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("finanzas2020.csv")

df_final = pd.DataFrame()

enero = df_creator('Enero')
febrero = df_creator('Febrero')
marzo = df_creator('Marzo')
abril = df_creator('Abril')
mayo = df_creator('Mayo')
junio = df_creator('Junio')
julio = df_creator('Julio')
agosto = df_creator('Agosto')
septiembre = df_creator('Septiembre')
octubre = df_creator('Octubre')
noviembre = df_creator('Noviembre')
diciembre = df_creator('Diciembre')

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
         'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

meses_var = [enero, febrero, marzo, abril, mayo, junio, julio,
             agosto, septiembre, octubre, noviembre, diciembre]

df_final['Enero'] = enero
df_final['Febrero'] = febrero
df_final['Marzo'] = marzo
df_final['Abril'] = abril
df_final['Mayo'] = mayo
df_final['Junio'] = junio
df_final['Julio'] = julio
df_final['Agosto'] = agosto
df_final['Septiembre'] = septiembre
df_final['Octubre'] = octubre
df_final['Noviembre'] = noviembre
df_final['Diciembre'] = diciembre

finanzas = {}

for i in meses:
    finanzas.update({i: df_final[i].sum()})

max_gasto = max(finanzas.items(), key=operator.itemgetter(1))[0]
min_gasto = min(finanzas.items(), key=operator.itemgetter(1))[0]


gasto_total = 0

for i in meses_var:
    gasto_mensual = gasto_mes(i)
    gasto_total += gasto_mensual

media_gastos = gasto_total/len(meses)

ingreso_total = 0
lista_ingresos = []

for i in meses_var:
    ingreso_mensual = ingreso_mes(i)
    ingreso_total += ingreso_mensual
    lista_ingresos.append(ingreso_mensual)


print(f"El ingreso total anual es de {ingreso_total}")
print(f"Los gastos totales ascienden a {gasto_total}")
print(f"Durante el año ha habido una media de gastos mensual de {media_gastos}")
print(f"{max_gasto} fue el mes en el que más se gastó y {min_gasto} el que menos")


plt.plot(lista_ingresos)
plt.title("Ingresos anuales")
plt.xlabel("Mes")
plt.ylabel("Ingresos")
indice = np.arange(12)
plt.xticks(indice, (meses))
plt.show()
