import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Suicide_data= pd.read_csv(r'C:\Users\Brian Creed\Downloads\master.csv.zip')

Ireland_suicide_data = Suicide_data[Suicide_data['country'] == 'Ireland']

Ireland_suicide_data.isnull().sum()
full_Ireland_suicide_data = Ireland_suicide_data.fillna(method = 'ffill')
index_full_Ireland_suicide_data=full_Ireland_suicide_data.set_index('year')
sort_full_Ireland_suicide_data=index_full_Ireland_suicide_data.sort_values(by = 'year')

From_1985_to_1989 = sort_full_Ireland_suicide_data[:60]
From_1990_to_1994 = sort_full_Ireland_suicide_data[60:120]
From_1995_to_1999 = sort_full_Ireland_suicide_data[120:180]
From_2000_to_2004 = sort_full_Ireland_suicide_data[180:240]
From_2005_to_2009 = sort_full_Ireland_suicide_data[240:300]
From_2010_to_2014 = sort_full_Ireland_suicide_data[300:]


def total_suicides(n):
    total = np.sum(n['suicides_no'])
    return total

plot_point1 = total_suicides(From_1985_to_1989)
plot_point2 = total_suicides(From_1990_to_1994)
plot_point3 = total_suicides(From_1995_to_1999)
plot_point4 = total_suicides(From_2000_to_2004)
plot_point5 = total_suicides(From_2005_to_2009)
plot_point6 = total_suicides(From_2010_to_2014)

new_data = {'Year':['1985_to_1989','1990_to_1994', '1995_to_1999', '2000_to_2004', '2005_to_2009','2010_to_2014'],'suicides_no':[plot_point1,plot_point2,plot_point3,plot_point4,plot_point5,plot_point6]}
df_new_data = pd.DataFrame(new_data)
sex = ['total','total','total','total','total','total']
df_new_data['sex'] = sex

years = ['1985_to_1989','1985_to_1989','1990_to_1994','1990_to_1994','1995_to_1999','1995_to_1999', '2000_to_2004','2000_to_2004', '2005_to_2009','2005_to_2009','2010_to_2014','2010_to_2014']

gender1 = From_1985_to_1989.groupby('sex')['suicides_no'].sum()
gender11 = gender1.to_frame()
gender11['Year'] = years[:2]
final_gender1 = gender11.reset_index()

gender2 = From_1990_to_1994.groupby('sex')['suicides_no'].sum()
gender12 = gender2.to_frame()
gender12['Year'] = years[2:4]
final_gender2 = gender12.reset_index()

gender3 = From_1995_to_1999.groupby('sex')['suicides_no'].sum()
gender13 = gender3.to_frame()
gender13['Year'] = years[4:6]
final_gender3 = gender13.reset_index()

gender4 = From_2000_to_2004.groupby('sex')['suicides_no'].sum()
gender14 = gender4.to_frame()
gender14['Year'] = years[6:8]
final_gender4 = gender14.reset_index()

gender5 = From_2005_to_2009.groupby('sex')['suicides_no'].sum()
gender15 = gender5.to_frame()
gender15['Year'] = years[8:10]
final_gender5 = gender15.reset_index()

gender6 = From_2010_to_2014.groupby('sex')['suicides_no'].sum()
gender16 = gender6.to_frame()
gender16['Year'] = years[10:]
final_gender6 = gender16.reset_index()

gender_table = pd.concat([final_gender1,final_gender2,final_gender3,final_gender4,final_gender5,final_gender6])

merged_tables = df_new_data.merge(gender_table, on= ['suicides_no','sex','Year'], how ='outer')
merged_table_sort = merged_tables.sort_values(by= 'Year')
print(merged_table_sort)

sns.set_theme(style = 'darkgrid')
hue_colours = {'total': 'green', 'male':'blue', 'female':'red'}
g = sns.lineplot(x='Year', y='suicides_no', data = merged_table_sort, hue= 'sex', hue_order = ['total','male', 'female'], palette = hue_colours, marker= 'o', markersize= 10)
g.set_title('Irish suicide statistics')
g.set(xlabel='Years', ylabel= 'Number of Suicides')
plt.xticks(rotation = 90)
plt.show()

number_gender = np.array([gender1, gender2, gender3, gender4, gender5, gender6])

female_increase = np.array([])
for i in range(6):
    female_increase = np.append(female_increase,number_gender[i][0])

male_increase = np.array([])
for i in range(6):
    male_increase = np.append(male_increase,number_gender[i][1])

a = 0
b = 1
f_diff = np.array([])

while a < 5:
    f_diff = np.append(f_diff, (female_increase[b] - female_increase[a]))
    a += 1
    b += 1
f_mean = np.mean(f_diff)
f_std = np.std(f_diff)
print(f_mean, f_std)

m_diff = np.array([])
a = 0
b = 1

while a < 5:
    m_diff = np.append(m_diff, (male_increase[b] - male_increase[a]))
    a += 1
    b += 1
m_mean = np.mean(m_diff)
m_std = np.std(m_diff)
print(m_mean, m_std)







