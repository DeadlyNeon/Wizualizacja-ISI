import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd

df = pd.read_excel(pd.ExcelFile("imiona.xlsx"), "Arkusz1")
pl = df.groupby(['Plec']).agg({"Liczba": ["sum"]})
rk = df.groupby(['Rok']).agg({"Liczba": ["sum"]})
M = df[df["Plec"] == 'M'].groupby(['Rok']).sum()
K = df[df["Plec"] == 'K'].groupby(['Rok']).sum()

plt.subplot(1, 3, 1)
plt.bar(['K', 'M'], [pl.values[0][0], pl.values[1][0]], color=['blue', 'red'])
plt.ylabel('Ilosc urodzen (w mln)')
plt.xlabel('Plec')
plt.subplot(1, 3, 2)

plt.plot(df.Rok.unique(), [K.values[y][-1] for y in range(len(K.values))], "b", label="K")
plt.plot(df.Rok.unique(), [M.values[y][0] for y in range(len(M.values))], "r", label="M")

plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilosc urodzen')
plt.xlabel('Rok')
plt.legend()
plt.subplot(1, 3, 3)
plt.bar(df.Rok.unique(), [rk.values[y][0] for y in range(len(rk.values))], color="black")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilosc urodzen')
plt.xlabel('Rok')
plt.show()