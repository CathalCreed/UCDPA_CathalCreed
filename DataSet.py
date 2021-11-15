import pandas as pd

Suicide_data= pd.read_csv(r'C:\Users\Brian Creed\Downloads\master.csv.zip')

Ireland_suicide_data = Suicide_data[Suicide_data['country'] == 'Ireland']

Ireland_suicide_data.set_index('year')

Ireland_suicide_data.sort_values(by = 'year')

From_1985_to_1989 = Ireland_suicide_data[0:60]
From_1990_to_1994 = Ireland_suicide_data[60:120]
From_1995_to_1999 = Ireland_suicide_data[120:180]
From_2000_to_2004 = Ireland_suicide_data[180:240]
From_2005_to_2009 = Ireland_suicide_data[240:300]
From_2010_to_2014 = Ireland_suicide_data[300:360]





