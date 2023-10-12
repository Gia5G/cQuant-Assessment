import pandas as pd
import numpy as np
df=pd.read_csv('PriceData_A.csv')
A=df.melt(id_vars=['Name', 'Date'], value_vars=['Run_1', 'Run_2', 'Run_3', 'Run_4','Run_5'], var_name='Run')

df=pd.read_csv('PriceData_B.csv')
B=df.melt(id_vars=['Name', 'Date'], value_vars=['Run_1', 'Run_2', 'Run_3', 'Run_4','Run_5'], var_name='Run')

JoinedData=pd.merge(A,B, on=['Name','Date','Run'] ,how='inner')
#print(JoinedData.head())

#Calculating the differences using the merged data
JoinedData['A-B'] = JoinedData['value_x'] - JoinedData['value_y']
JoinedData['(A-B)/A'] = (JoinedData['value_x'] - JoinedData['value_y'])/JoinedData['value_x']
JoinedData['abs(A-B)'] = abs(JoinedData['value_x'] - JoinedData['value_y'])
JoinedData['abs((A-B)/A)'] = abs((JoinedData['value_x'] - JoinedData['value_y'])/JoinedData['value_x'])
print(JoinedData)


#Future Direction:
# 
# For task 6, I would save each of the 4 summary tables generated in task5 under different variables (ex: JoinedDatax) and generate csv's
# using the to_csv function
# "JoinedDatax.to_csv('Summary Statistics by [dimension]')" 
#
# For task 7, I would create a big picture chart of difference between A and B using a line graph. The x axis would have the range of the dates given while the y axis
# would show the difference in values and the lines for data A and B would be colored in blue and orange or two other contrasting colors.
# I would also include similar figures that look at the mean difference by month, day, and hour to show possible correlations between those factors and the difference between A and B
#