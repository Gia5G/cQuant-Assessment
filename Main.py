import pandas as pd
import numpy as np

# Importing data set A
df=pd.read_csv('PriceData_A.csv')
A=df.melt(id_vars=['Name', 'Date'], value_vars=['Run_1', 'Run_2', 'Run_3', 'Run_4','Run_5'], var_name='Run')

# Importing data set B
df=pd.read_csv('PriceData_B.csv')
B=df.melt(id_vars=['Name', 'Date'], value_vars=['Run_1', 'Run_2', 'Run_3', 'Run_4','Run_5'], var_name='Run')

#Merging data set A and data set B
JoinedData=pd.merge(A,B, on=['Name','Date','Run'] ,how='inner')
print('Joined data table:','\n',JoinedData.head())

#Calculating the differences using the merged data
JoinedData['A-B'] = JoinedData['value_x'] - JoinedData['value_y']
JoinedData['(A-B)/A'] = (JoinedData['value_x'] - JoinedData['value_y'])/JoinedData['value_x']
JoinedData['abs(A-B)'] = abs(JoinedData['value_x'] - JoinedData['value_y'])
JoinedData['abs((A-B)/A)'] = abs((JoinedData['value_x'] - JoinedData['value_y'])/JoinedData['value_x'])
print('Joined data table summary statistics:','\n',JoinedData)

# Calculating the overall summary statistics for all of the date
YearMin=JoinedData['abs(A-B)'].min()
YearMax=JoinedData['abs(A-B)'].max()
YearMean=JoinedData['abs(A-B)'].mean()

print('Overall min:', YearMin)
print('Overall max:', YearMax)
print('Overall mean:', YearMean)

#Future Directions:
# For task 5, I have included the overall min, max, and mean of the absolute difference of data sets A and B. With more time, I would group this data
# by year, month, day of week, and hour of day according to the instructions. I was not sure if the summary statistics should have been added onto the merged table
# or presented as a separate table. As a separate table, I would include the min, max, and mean as separate columns for each date and time dimension with an additional column for the specific
# time/date dimension that is being represented. Each table would be named differently to save them as csv files
#
# For task 6, I would save each of the 4 summary tables generated in task5 under different variables (ex: JoinedDatax) and generate csv's
# using the to_csv function
# "JoinedDatax.to_csv('Summary Statistics by [dimension]')" 
#
# For task 7, I would create a big picture chart of difference between A and B using a line graph. The x axis would have the range of the dates given while the y axis
# would show the difference in values and the lines for data A and B would be colored in blue and orange or two other contrasting colors.
# I would also include similar figures that look at the mean difference by month, day, and hour to show possible correlations between those factors and the difference between A and B
#