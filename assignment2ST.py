#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20})
import seaborn as sns


# Abbreviations:
# AGR: Agricultural Lands
# RUR: Rural Population

# function for reading a dataset and returning two dataframes: one with
# years as column, and one with countries as column. First 4 rows are
# being skipped as they are not important
def read_datasets (x):
    y = pd.read_csv(x, skiprows=4)
    return y, y.T

# read both datasets
AGR_year, AGR_countries = read_datasets('AGR.csv')
RUR_year, RUR_countries = read_datasets('RUR.csv')

# initializing a list with the interval that both datasets provide
years_interval = [str(x) for x in range(1961, 2018)]

# setting country code as index for both dataframes.
AGR = AGR_year.set_index('Country Code')
RUR = RUR_year.set_index('Country Code')

# skipping countries which have blank cells
AGR = AGR[years_interval].dropna()
RUR = RUR[years_interval].dropna()

# this list will contain country codes for countries that
# provide data for both indicators
indices = list(set(RUR.index) & set(AGR.index))

# getting information from both dataframes using indices from the list above
AGR = AGR.loc[indices]
RUR = RUR.loc[indices]


# getting data ready for plotting (picking the countries which will be compared)
_AGR = AGR.loc[['JPN', 'ITA', 'CHN', 'GRC', 'WLD']].stack()
_AGR = _AGR.reset_index().rename(columns={"level_1":"year", 0: "Agricultural Lands %"})

# setting the size of the figure, and adding a title
fig, ax = plt.subplots(figsize=(15, 9))
ax.set_title('Change of Agricultural Land Percentage Over the Time From 1961-2018')

# plotting the data in a line plot using seaborn and matplotlib libraries
sns.lineplot(data = _AGR, x='year', y='Agricultural Lands %', hue='Country Code', palette="rocket")
plt.legend(loc='upper left')
plt.xticks(['1961', '1970', '1980', '1990', '2000', '2010', '2018'])
plt.show()
# saving the graph as an image to view with more resolution
fig.savefig('Change of Agricultural Land Percentage Over the Time From 1961-2018', dpi=600)



# getting data ready for plotting (picking the countries which will be compared)
_RUR = RUR.loc[['JPN', 'ITA', 'CHN', 'GRC', 'WLD']].stack()
_RUR = _RUR.reset_index().rename(columns={"level_1":"year", 0: "Rural Population %"})

# setting the size of the figure, and adding a title
fig2, ax2 = plt.subplots(figsize=(15, 9))
ax2.set_title('Change of Rural Population Percentage Over the Time From 1961-2018')

# plotting the data in a line plot using seaborn and matplotlib libraries
sns.lineplot(data = _RUR, x='year', y='Rural Population %', hue='Country Code', palette="rocket")
plt.legend(loc='upper left')
plt.xticks(['1961', '1970', '1980', '1990', '2000', '2010', '2018'])
plt.show()

# saving the graph as an image to view with more resolution
fig.savefig('Change of Rural Population Percentage Over the Time From 1961-2018', dpi=600)


# initializing a list of country codes in order to use it
# for exploring correlation between both indicators
countries_correlation_list = ['WLD', 'JPN', 'GRC', 'CHN', 'USA', 'ITA', 'NLD']
AGR_correlation = AGR.loc[countries_correlation_list]
RUR_correlation = RUR.loc[countries_correlation_list]


# setting size and style of the figure
fig, ax = plt.subplots(figsize=(15, 9))
sns.set_style("darkgrid")

# displaying scatterplots for the whole world, and for 6 countires
for country in countries_correlation_list:
    sns.regplot(x = AGR_correlation.loc[country], y = RUR_correlation.loc[country], label=country, ax=ax)

# setting labels and titles and showing the graph
ax.set(xlabel='Agricultural Lands %', ylabel='Rural Population %', )
ax.legend()
ax.set_title('AGL vs RUR')
sns.despine()

# saving the graph as an image to view with more resolution
fig.savefig('AGL vs RUR', dpi=600)
