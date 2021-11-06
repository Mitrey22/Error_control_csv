import pandas as pd

df = pd.read_csv("finanzas2020.csv")


def df_creator(month):
    ctn = 0
    lista = []
    mes = month
    data = df[f'{mes}']
    while ctn < len(data):
        value = data.iloc[ctn]
        try:
            value = int(value)
        except ValueError:
            value = 0
        lista.insert(ctn, value)
        ctn += 1
        pass
    return lista


def gasto_mes(month):
    gasto = 0
    for i in month:
        if i < 0:
            gasto += i
        else:
            gasto += 0
    return gasto


def ingreso_mes(month):
    ingreso = 0
    for i in month:
        if i > 0:
            ingreso += i
        else:
            ingreso += 0
    return ingreso
