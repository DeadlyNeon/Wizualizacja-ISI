import pandas as pd
import matplotlib.pyplot as plt

data = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(data)
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
grupa.plot()
plt.show()
