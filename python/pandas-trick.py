#%%  assign - explode 
import pandas as pd

# %%
df = pd.DataFrame({
    'sandwich': ['PB&J', 'BLT', 'cheese'], 
    'ingredients': ['peanut butter, jelly', 
                    'Bacon, lettuce, tomato', 
                    'swiss cheese']}, 
    index = ['a', 'b', 'c']
)
# %%
df.ingredients

# %%
df.assign(
  ingredients =  df.ingredients.str.split(',')
).explode('ingredients')
# %% assign 
df = pd.DataFrame({'temp_c': [17.0, 25.0]},
...                   index=['Portland', 'Berkeley'])

# %%
df

# %%
df.assign(
   temp_f = lambda x: x.temp_c  * 9 / 5 + 32, 
   temp_r = [x if x > 17 else x * 100 for x in df['temp_c']]
)
# %%
