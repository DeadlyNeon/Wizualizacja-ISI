import pandas as pd
import matplotlib.pyplot as plt

data = pd.ExcelFile('imiona.xlsx')
frame = pd.read_excel(data)

list=[]
for a in frame['Imie']:
    if a[-1] == 'A':
        list.append('K')
    else:
        list.append('M')
frame['Plec'] = list

gr = frame.groupby(['Plec']).agg({'Liczba':['sum']})
gr.plot.bar()
plt.xlabel('Plec')
plt.ylabel('Ilosc')
plt.show()