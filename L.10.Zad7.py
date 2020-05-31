import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd

df= pd.read_excel(pd.ExcelFile("imiona.xlsx"),"Arkusz1")
M=df[df["Plec"]=='M'].groupby(['Rok']).sum()
K=df[df["Plec"]=='K'].groupby(['Rok']).sum()

plt.bar(df.Rok.unique(),[M.values[y][0] for y in range(len(M.values))],color="blue", label="M")
plt.bar(df.Rok.unique(),[K.values[y][0] for y in range(len(K.values))],color="red", label="K",  bottom=[M.values[y][0] for y in range(len(M.values))])
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilosc urodzen')
plt.xlabel('Rok')
plt.legend()
plt.show()