import pandas as pd
import matplotlib.pyplot as plt



csv = pd.read_csv('zamowienia.csv', delimiter=';')
group = csv.groupby(['Sprzedawca']).agg({'idZamowienia':['sum']})
group.plot.bar()
plt.show()