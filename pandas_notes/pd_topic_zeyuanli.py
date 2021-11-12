# # Pivot tables
# 
# Stats 507, Fall 2021
# 
# Zeyuan Li
# zeyuanli@umich.edu
# 10/19/2021
# 
# 

# ## Pivot tables in pandas
# 
# The pivot tables in Excel is very powerful and convienent in handling with numeric data. Pandas also provides ```pivot_table()``` for pivoting with aggregation of numeric data. There are 5 main arguments of ```pivot_table()```:
# * ***data***: a DataFrame object
# * ***values***: a column or a list of columns to aggregate.
# * ***index***: Keys to group by on the pivot table index. 
# * ***columns***:  Keys to group by on the pivot table column. 
# * ***aggfunc***: function to use for aggregation, defaulting to ```numpy.mean```.

# ### Example

# In[3]:


df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 6,
        "B": ["A", "B", "C"] * 8,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 4,
        "D": np.random.randn(24),
        "E": np.random.randn(24),
        "F": [datetime.datetime(2013, i, 1) for i in range(1, 13)]
        + [datetime.datetime(2013, i, 15) for i in range(1, 13)],
    }
)
df


# ### Do aggregation
# 
# * Get the pivot table easily. 
# * Produce the table as the same result of doing ```groupby(['A','B','C'])``` and compute the ```mean``` of D, with different values of D shown in seperate columns.
# * Change to another ***aggfunc*** to finish the aggregation as you want.

# In[4]:


pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])


# In[9]:


pd.pivot_table(df, values="D", index=["B"], columns=["A", "C"], aggfunc=np.sum)


# ### Display all aggregation values
# 
# * If the ***values*** column name is not given, the pivot table will include all of the data that can be aggregated in an additional level of hierarchy in the columns:

# In[6]:


pd.pivot_table(df, index=["A", "B"], columns=["C"])


# ### Output
# 
# * You can render a nice output of the table omitting the missing values by calling ```to_string```

# In[10]:


table = pd.pivot_table(df, index=["A", "B"], columns=["C"])
print(table.to_string(na_rep=""))
