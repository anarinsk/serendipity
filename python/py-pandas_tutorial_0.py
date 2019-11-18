#%%
import pandas as pd 
#%% 
test_list = [100,200,300]
pd.Series(data=test_list)

# %%
dictionary = {'a':100, 'b':200, 'c':300}
pd.Series(data=dictionary)

#%%
data = [['thomas', 100], ['nicholas', 200], ['danson', 300]] 
df = pd.DataFrame(data, columns = ['name', 'Age'])
df
# %%
url = 'https://gist.githubusercontent.com/michhar/2dfd2de0d4f8727f873422c5d959fff5/raw/ff414a1bcfcba32481e4d4e8db578e55872a2ca1/titanic.csv'
df = pd.read_csv(url, sep='\t')

# %%
df

# %%
