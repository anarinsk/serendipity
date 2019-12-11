## https://towardsdatascience.com/5-advanced-features-of-pandas-and-how-to-use-them-1f2e2585d83e

#%% how to set pandas env

import pandas as pd

display_settings = {
    'max_columns': 10,
    'expand_frame_repr': True,  # Wrap to multiple pages
    'max_rows': 10,
    'precision': 2,
    'show_dimensions': True
}

for op, value in display_settings.items():
    pd.set_option("display.{}".format(op), value)

# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html

# %%
import seaborn as sns

iris = sns.load_dataset('iris')
# %%
iris1 = iris[0:100]
iris2 = iris[100:]
iris3 = iris.iloc[:, 0:2]
iris4 = iris.iloc[:, 2:]
# %%
pd.concat([iris1, iris2], axis=0)
# %%
pd.concat([iris3, iris4], axis=1) 

# %%
import pandas as pd

players_data = {'Player': ['Superman', 'Batman', 'Thanos', 'Batman', 'Thanos',
   'Superman', 'Batman', 'Thanos', 'Black Widow', 'Batman', 'Thanos', 'Superman'],
   'Year': [2000,2000,2000,2001,2001,2002,2002,2002,2003,2004,2004,2005],
   'Points':[23,43,45,65,76,34,23,78,89,76,92,87]}
   
df = pd.DataFrame(players_data)

print(df)


# %%
