import pandas as pd
data = pd.read_csv('athlete_events.csv')

# # question 1
# columns_to_show = ['Sex', 'Age', 'Year']
# a = (data[data['Year'] == 1996])
# print(a.groupby(['Sex']).describe())
# print(data[data['Year'] == 1996].groupby(['Sex']).describe())

# # question 2
# a = (data[(data['Year'] == 2000) & (data['Sex'] == 'M')])
# count_for_all_sports = len(a.Name.unique())
# z = a[a['Sport'] == 'Gymnastics']
# count = len(z.Name.unique())
# print(count/count_for_all_sports)

# # question 3
# columns_to_show = ['Name', 'Height']
# a = (data[(data['Year'] == 2000) & (data['Sex'] == 'F') & (data['Sport'] == 'Basketball')])[columns_to_show]
# z = a.drop_duplicates(subset=None, keep='first', inplace=False)
# print(z.describe())

# # question 4
# columns_to_show = ['Name', 'Weight', 'Sport']
# a = data[data['Year'] == 2002][columns_to_show]
# z = a.sort_values(by='Weight', ascending=False)
# print(z.head(1))

# # question 5
# columns_to_show = ['Name', 'Year']
# a = data[data['Name'] == 'Pawe Abratkiewicz'][columns_to_show]
# print(len(a.index))
# z = a.drop_duplicates(subset=None, keep='first', inplace=False)
# print(len(z.index))

# # question 6
# columns_to_show = ['Name', 'Medal']
# a = data[(data['Medal'] == 'Silver') & (data['Year'] == 2000) & (data['Team'] == 'Australia') & (data['Sport'] == 'Tennis')][columns_to_show]
# print(len(a.index))

# question 7
# columns_to_show = ['Name', 'Medal']
# a = data[(data['Medal'].notnull()) & (data['Team'] == 'Switzerland') & (data['Year'] == 2016)][columns_to_show]
# b = data[(data['Medal'].notnull()) & (data['Team'] == 'Serbia') & (data['Year'] == 2016)][columns_to_show]
# print((len(a.index)) > (len(b.index)))

# # question 8
# columns_to_show = ['Age']
# a = data[(data['Year'] == 2014)]
# print(a.groupby(['Age']).describe())

# # question 9
# columns_to_show = ['Sport']
# a = data[(data['City'] == 'Lake Placid') & (data['Season'] == 'Summer')]
# print(len(a.index) > 0)
# a = data[(data['City'] == 'Sankt Moritz') & (data['Season'] == 'Winter')]
# print(len(a.index) > 0)

# # question 10
# columns_to_show = ['Sport']
# a = data[data['Year'] == 1996][columns_to_show]
# z = a.drop_duplicates(subset=None, keep='first', inplace=False)
# count_1996 = len(z.index)
# a = data[data['Year'] == 2016][columns_to_show]
# z = a.drop_duplicates(subset=None, keep='first', inplace=False)
# count_2016 = len(z.index)
# print(abs(count_1996-count_2016))
