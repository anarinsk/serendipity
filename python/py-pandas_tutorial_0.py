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
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url, sep=',')
# %%
df.info()

# %%
df.nunique()

# %%
df[['Pclass', 'Sex']]

# %%
df.drop(['PassengerId', 'Name', 'Ticket'], axis = 1, inplace=True)
df.iloc[500:511]
# %%
df[df['Sex'] == 'male']
# %%
df[['Pclass', 'Sex']][df['Sex'] == 'male'].iloc[500:511]

# %%
df.describe()

# %%
df.corr()

# %%
df['Sex'].value_counts()

# %%
df.isnull().sum()

# %%
df[df['Age'].isnull()]

# %%
#df['Age'].fillna(df['Age'].mean())
df.dropna(inplace=True)
# %%
df.isnull().sum()

# %%
df.groupby('Pclass').mean()
df.groupby('Pclass')['Age'].mean()
# %%
