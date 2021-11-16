import pandas as pd
import numpy as np

Suicide_data= pd.read_csv(r'C:\Users\Brian Creed\Downloads\master.csv.zip')

Ireland_suicide_data = Suicide_data[Suicide_data['country'] == 'Ireland']

Ireland_suicide_data.isnull().sum()
full_Ireland_suicide_data = Ireland_suicide_data.fillna(method = 'ffill')

full_Ireland_suicide_data.set_index('year')

full_Ireland_suicide_data.sort_values(by = 'year')

From_1985_to_1989 = full_Ireland_suicide_data[0:60]
From_1990_to_1994 = full_Ireland_suicide_data[60:120]
From_1995_to_1999 = full_Ireland_suicide_data[120:180]
From_2000_to_2004 = full_Ireland_suicide_data[180:240]
From_2005_to_2009 = full_Ireland_suicide_data[240:300]
From_2010_to_2014 = full_Ireland_suicide_data[300:360]


def total_suicides(n):
    total = np.sum(n['suicides_no'])
    return total

plot_point1 = total_suicides(From_1985_to_1989)
plot_point2 = total_suicides(From_1990_to_1994)
plot_point3 = total_suicides(From_1995_to_1999)
plot_point4 = total_suicides(From_2000_to_2004)
plot_point5 = total_suicides(From_2005_to_2009)
plot_point6 = total_suicides(From_2010_to_2014)

gender = From_1985_to_1989.groupby('sex').sum()







