#%% imports module pandas with nickname 'pd'
import pandas as pd


#%% from the matplotlib package import pyplot module with nickname plt
from matplotlib import pyplot as plt

#%%
x = [1, 2 ,3] 
y = [1, 4, 9]
z = [10, 5, 0]
plt.plot(x, y)
plt.plot(x, z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y", "this is z"])
plt.show()

#%%
sample_data = pd.read_csv('/home/wenzel/Jupyter/Tutorial/sample_data.csv')

#%%
sample_data 

#%%
type(sample_data)

#%%
sample_data.column_c

#%%
type(sample_data.column_c)

#%%
sample_data.column_c.iloc[0]


#%% Longer method
x = [sample_data.column_a]
y = [sample_data.column_b]
plt.plot(x, y)
plt.title("Sample Data AB")
plt.xlabel("A")
plt.ylabel("B")
plt.show()

#%%
plt.plot(sample_data.column_a, sample_data.column_b, 'o')
plt.plot(sample_data.column_a, sample_data.column_c)
plt.show()

#%%
countries = pd.read_csv("/home/wenzel/Jupyter/Tutorial/countries.csv")

#%%
countries

#%% Compare population growth in certain countries (US and China)
us = countries[countries.country == 'United States']

#%%
us

#%%
china = countries[countries.country == 'China']

#%%
china

#%%
plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.xlabel("year")
plt.ylabel("Population in Millions")
plt.title("China and US Population Growth")
plt.legend(['United States', 'China'])
plt.show()

#%%
us.population

#%%
us.population.iloc[0]

#%%
us.population / us.population.iloc[0]

#%%
us.population / us.population.iloc[0] * 100

#%%
plt.plot(us.year, us.population / us.population.iloc[0] * 100)
plt.plot(china.year, china.population / china.population.iloc[0] * 100)
plt.show()

#%%
