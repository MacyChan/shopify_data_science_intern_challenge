#!/usr/bin/env python
# coding: utf-8

# # Question 1

# Given some sample data, write a program to answer the following: 
# 
# ```On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. ```

# In[1]:


import altair as alt
import pandas as pd


# *a. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.*  
# 
# Assume the data is in USD, the amount of AOV does not make sense, given  
# 1. The sold sneakers are affordable items (i.e. says USD100).
# 2. Each shops sells one model  
# 
# This indicated customers are making bulk purchases of 30 pairs of identical shoes per order in average.  
# 
# Shopify is well known among B2C eCommerce. Therefore this result is unlikely to happen.

# In[2]:


orders = pd.read_csv('data/orders.csv')
orders.head()


# Looking at the data, the `total_items` is much less than 30 in first few lines.  
# As mean is estimator that very sensitive to outliers, my first suspicion is there are outliners in the dataset.

# In[3]:


alt.Chart(orders).mark_bar().encode(
    alt.X("total_items", bin=alt.Bin(maxbins=30),title="Average number of sneakers per order (pair)"),
    y='count()',
    tooltip=['total_items','count()', 'order_amount']
).properties(height=200, width=800, title="Distribution of average number of sneakers per order")


# Form the graph above, most of the orders are between 1-3 items. However, there are 17 records with bulk purchase of 2000 pairs of shoes (USD704,000), it leads to the high shift of AOV. 

# *b. What metric would you report for this dataset?*
# 
# Because of the outliners, we can use `median`, which is less sensitive to outliers.

# *c. What is its value?*

# In[4]:


print(f'The median of order value is USD{ orders["order_amount"].median()}')


# It is a fairly reasonable amount, compare to USD$3145.13.  
# 
# 
# To further investigate, we can also look at the distribution of average price per pair of shoes.

# In[5]:


orders["avg_per_pair"] = orders["order_amount"] / orders["total_items"]
base = (
    alt.Chart(orders)
    .mark_bar()
    .encode(
        x=alt.X(
            "avg_per_pair:Q",
        ),
        y="count()",
    )
    .properties(height=200, width=800, title="Distribution of average sneakers price")
)

brush = alt.selection_interval(encodings=["x"])
lower = (
    base.encode(
        x=alt.X(
            "avg_per_pair:Q",
            axis=alt.Axis(
                labels=False, title="Average price per pair of sneakers (USD)"
            ),
        )
    )
    .properties(height=60, width=800, title="Drag the plot in below to zoom")
    .add_selection(brush)
)

upper = base.encode(
    alt.X(
        "avg_per_pair:Q",
        scale=alt.Scale(domain=brush),
        axis=alt.Axis(title=""),
    )
)


upper & lower


# As we can see, there are outliners - very expensive shoes as well.  
# Therefore, we can compare the median of pair of shoes per order, and the median price per pair of sneakers.

# In[6]:


print(f'The median of pair of shoes per order is { orders["total_items"].median()}')
print(f'The median price per pair of sneakers is USD{ round(orders["avg_per_pair"].median(), 2) }')


# It matched our result in part c.
