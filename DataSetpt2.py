import pandas as pd
import matplotlib.pyplot as plt


Suicide_data = pd.read_csv(r'C:\Users\Brian Creed\Downloads\master.csv.zip')

Ireland_suicide_data = Suicide_data[Suicide_data['country'] == 'Ireland']

Ireland_suicide_data.isnull().sum()
full_Ireland_suicide_data = Ireland_suicide_data.fillna(method='ffill')

index_full_Ireland_suicide_data = full_Ireland_suicide_data.set_index('year')
sort_full_Ireland_suicide_data = index_full_Ireland_suicide_data.sort_values(by='year')
grouped_full_Ireland_suicide_data = sort_full_Ireland_suicide_data.groupby(['sex', 'age'])['suicides_no'].sum()
final_df = grouped_full_Ireland_suicide_data.reset_index()

male = final_df[final_df['sex'] == 'male']
female = final_df[final_df['sex'] == 'female']
print(male, female)

def plot_table(axes, x, y, colour, rot, title, xlabel, ylabel):
    axes.bar(x, y, color=colour)
    axes.set_xlabel(xlabel, fontsize =16)
    axes.set_ylabel(ylabel, fontsize = 16)
    axes.set_title(title, fontsize = 16)
    axes.set_xticklabels(x, rotation=rot, fontsize= 16)


fig, ax = plt.subplots(1, 2, sharey=True)
plot_table(ax[0], male['age'], male['suicides_no'], 'blue', 90, 'Male', 'age category', 'Number of suicides')
plot_table(ax[1], female['age'], female['suicides_no'], 'red', 90, 'Female', 'age category', '')
fig.suptitle('Irish suicide statistics 1985 to 2014', fontsize = 20)

plt.show()








