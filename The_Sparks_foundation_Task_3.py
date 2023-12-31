#!/usr/bin/env python
# coding: utf-8

# # Task 3: Exploratory Data Analysis - Retail
# ## Author: Mahmoud Ahmed Shimy
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis (EDA
#    )</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# > I have selected the **SampleSuperStore** dataset to investigate it and do some **E**xploratory **D**ata **A**nalysis by exploring the correlations between the varies things on it and find patterns to find out the weak areas where you can work to make more profit by answering some question that we will ask now
# 
# 
# #### Question(s) for Analysis
# <ol>
# <li>First question after importing and wrangling the data is What is the lowest Cities, States and Regions with total and average Profit? and starts <a href="#Q1">here</a></li>
# <li>Also it is important for me to find some correlations between the varies columns <a href="#Q2">here</a></li>
# <li>What is the biggest Cities, States and Regions offering Discounts? <a href="#Q4">here</a></li>
# <li>Finally we need to investigate more further in the areas that needs to work more to make more profits and starts <a href="#Q7">here</a></li>
# </ol>

# ### importing Liberaries and DataFrame
# >This section is to import the necessary liberaries and DataFrame

# In[2]:


# for data frames
import pandas as pd
# for numerical fn.
import numpy as np
# for data visualization
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling section
# > In this section we will do some gathering, assessing and cleaning to the data to be more suatable and easy to analyse

# In[4]:


df = pd.read_csv("SampleSuperstore.csv")
df.sample(2)


# In[5]:


df.shape


# Now we know that the data has nearly 10k observations and 13 column.
# 
# Lets look at the first 3 observations.

# In[6]:


df.head(3)


# lets take look at the columns names and data types and the number of the missing data on each one

# In[7]:


df.info()


# In[8]:


df.describe()


# 
# ### Data Cleaning
# > After gathering the data looks good so let's take a look on null values and duplicated.

# In[9]:


df.Country.value_counts()


# There's only one country so we can drop this column

# In[10]:


df.drop(columns='Country', inplace=True)


# Now we can drop all Null values from the dataframe

# In[11]:


df.dropna(inplace=True)


# Finally for cleaning the data let's take look at the number of duplicated values and drop them

# In[12]:


df.duplicated().sum()


# In[13]:


df.drop_duplicates(inplace=True)


# In[14]:


df.info()


# Now we have cleaned data without missing or duplicated values and ready to be explored

# <a id='eda'></a>
# ## Exploring Data Section (EDA)
# > After wrangling the data, In this section we will answer some questions by analysing the data to create some Conclusions about the dataframe.
# > All these questions is from my deep mind and of course you may have different questions so don't be restricted by this questions.

# In[13]:


# pip install ipywidgets
# pip install pandas-profiling


# In[14]:


from pandas_profiling import ProfileReport


# In[15]:


ProfileReport(df)


# In[16]:


df.sample(2)


# ## Uni-variate analysis

# In[17]:


# City
df["City"].value_counts()[:5]


# In[18]:


# State
df["State"].value_counts()[:5]


# In[19]:


# Region
df["Region"].value_counts()[:5]


# In[20]:


# Numerical Data
df.describe()


# ## Bi-Variate analysis
# <a id='Q1'></a>
# #### Q1: What is the lowest Cities with total and average Profit?

# In[21]:


def pltbar(datax, datay, namex, namey):
    plt.bar(
    x = datax,
    height = datay
    )
    plt.xlabel(namex, fontsize = 15)
    plt.ylabel(namey, fontsize = 15)


# In[22]:


df.sample(3)


# In[23]:


df.groupby(df["City"]).sum().sort_values(['Profit']).Profit[:5]


# In[24]:


pltbar(df.groupby(df["City"]).sum().sort_values(['Profit']).Profit[:5].index, df.groupby(df["City"]).sum().sort_values(['Profit']).Profit[:5].values*-1, "top 5 Cities", "Total loss")
plt.title("The lowest Cities with total Profit", fontsize = 15)


# In[25]:


df.groupby(df["City"]).mean().sort_values(['Profit']).Profit[:5]


# In[26]:


pltbar(df.groupby(df["City"]).mean().sort_values(['Profit']).Profit[:5].index, df.groupby(df["City"]).mean().sort_values(['Profit']).Profit[:5].values*-1, "top 5 Cities", "AVG loss")
plt.title("The lowest Cities with average Profit", fontsize = 15)


# #### Q2: What is the lowest States with total and average Profit?

# In[27]:


df.groupby(df["State"]).sum().sort_values(['Profit']).Profit[:5]


# In[28]:


pltbar(df.groupby(df["State"]).sum().sort_values(['Profit']).Profit[:5].index, df.groupby(df["State"]).sum().sort_values(['Profit']).Profit[:5].values*-1, "top 5 States", "Total loss")
plt.title("The lowest States with Total Profit", fontsize = 15)


# In[29]:


df.groupby(df["State"]).mean().sort_values(['Profit']).Profit[:5]


# In[30]:


pltbar(df.groupby(df["State"]).mean().sort_values(['Profit']).Profit[:5].index, df.groupby(df["State"]).mean().sort_values(['Profit']).Profit[:5].values*-1, "top 5 States", "AVG loss")
plt.xticks(rotation = 20)
plt.title("The lowest States with average Profit", fontsize = 15)


# #### Q3: What is the lowest Region with total and average Profit?

# In[31]:


df.groupby(df["Region"]).sum().sort_values(['Profit']).Profit[:5]


# In[32]:


pltbar(df.groupby(df["Region"]).sum().index, df.groupby(df["Region"]).sum().Profit.values, "Region", "Total Profit")
plt.title("Regions with total Profit", fontsize = 15)


# In[33]:


df.groupby(df["Region"]).mean().sort_values(['Profit']).Profit


# In[34]:


pltbar(df.groupby(df["Region"]).mean().index, df.groupby(df["Region"]).mean().Profit.values, "Region", "AVG Profit")
plt.title("Regions with average Profit", fontsize = 15)


# <a id='Q2'></a>
# ### Checking out some correlations

# In[35]:


plt.scatter(x = df.Discount, y = df.Profit)
plt.xlabel('Discount')
plt.ylabel('Profit')


# In[36]:


df.Profit.corr(df.Discount)


# After showing the plot and calculating correlation we see that there's a negative correlation between the profit and Discount = -2.19
# <a id='Q4'></a>
# #### Q4:What is the biggest Cities offering Discounts?

# In[37]:


df[df.Discount > 0].groupby(df["City"]).sum().sort_values(['Discount'], ascending=False)[:5] 


# In[38]:


pltbar(df.groupby(df["City"]).sum().sort_values(['Discount'], ascending=False)[:5].index, df.groupby(df["City"]).sum().sort_values(['Discount'], ascending=False)[:5] .Discount.values, 'City', 'Total discounts')
plt.title("The highest Cities with total discount", fontsize = 15)


# #### Q5:What is the biggest States offering Discounts?

# In[39]:


df.groupby(df["State"]).mean().sort_values(['Discount'], ascending=False)[:5]


# In[40]:


pltbar(df.groupby(df["State"]).mean().sort_values(['Discount'], ascending=False)[:5].index, df.groupby(df["State"]).mean().sort_values(['Discount'], ascending=False)[:5].Discount.values, 'State', 'AVG discounts')
plt.title("The highest states with AVG discount", fontsize = 15)


# #### Q6:What is the biggest Regions offering Discounts ?

# In[41]:


df.groupby(df["Region"]).mean().sort_values(['Discount'], ascending=False)


# In[42]:


pltbar(df.groupby(df["Region"]).mean().index, df.groupby(df["Region"]).mean().Discount.values, 'Region', 'AVG discounts')
plt.title("Regions with AVG discounts", fontsize = 15)


# <a id='Q7'></a>
# ## Multi-Variate analysis
# #### Q7: The  lowest Profit State in Centeral Region

# In[43]:


df[df['Region'] == "Central"].groupby(df.State).sum().sort_values(["Profit"])[:5]


# #### Q8: The  lowest Profit City in Texas State

# In[44]:


df[df.State == "Texas"].groupby(df.City).sum().sort_values(["Profit"])[:5]


# In[15]:


df.to_csv("Modified")


# <a id='conclusions'></a>
# ## Conclusions
# ### After investigating the data frame we knew the following:
# > - - The best selling Region is **West**
# >   - The best selling State is **California**
# >   - The best selling City is **New York City**
# > - The Average profit per unit is **7.56**
# > - The lowest Region with total profit is **Central** Region with $39655$ profit
# > - The lowest State with total profit is **Texas** with $25751$ Total loss
# > - The lowest City with total profit is **Philadelphia** with $13843$ Total loss
# > - The lowest City with total profit in Texas State in Central region is **Houston** with $10175$ Total loss and 27% discount per sell
# > - There's a **Negative** correlation between the Profit and Discount = -$0.219$
# > - The heighest Region offering discounts is the **Central** Region with an average 24% discount per sell
# > - The second heighest State offering discounts is **Texas** with 37%
# > - The heighest City offering discounts is **Philadelphia** with $1978$ discount offers.<br>
# > 
# >**Recommendation:**
# Finally we recommend to lower the discount in some areas like **Philadelphia** City in East Region and **Houston** City in Texas State and **Texas, Illinios** States in **Central** region on general to raise the profit.
# ## DataFrame limitations
# > Fortunately there's no big limitations on this data frame hence the biggest problem that limited our investigate is the lack of timeseries data or timestamp in the data and if there was, we would uses it to investigate more and more in the data frame but generally i think we did great job on this data frame under these limitations.
