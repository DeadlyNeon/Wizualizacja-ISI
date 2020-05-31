import pandas as pd
import matplotlib.pyplot as plt

data = pd.ExcelFile('imiona.xlsx')
frame = pd.read_excel(data)

rok = frame['Rok'].max()
group = frame[frame['Rok'] > rok-5].groupby(['Plec']).agg({'Liczba':['sum']})
group.plot.pie(subplots= True, autopct='%.2f %%')
plt.show()
