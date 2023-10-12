#cQuant importing data
#DataPrice_A
import pandas as pd
print(pd.__version__)
df=pd.read_csv('PriceData_A.csv')
df_meltA=df.melt(id_vars=['Name', 'Date', ], value_vars=['Run_1', 'Run_2', 'Run_3', 'Run_4','Run_5'], var_name='Run')
print(df_meltA)
