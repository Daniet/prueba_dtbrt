import os

import pandas as pd

file = f'{os.sep}'.join(['resources', 'PSO20220223.xls'])
df = pd.read_excel(file, parse_dates=True, sheet_name='Arcos Comerciales y T.Recorrido')

tr_min = df.sort_values(by=['tr_minimo'], ascending=False).groupby(['linea']).head()
tr_max = df.sort_values(by=['tr_maximo'], ascending=True).groupby(['linea']).head()
tr_optimo = df.sort_values(by=['tr_optimo'], ascending=False).groupby(['linea']).head()

pd.concat([tr_min, tr_max, tr_optimo]).head().to_csv(f'{os.sep}'.join(['resources', 'PSO20220223.csv']))
