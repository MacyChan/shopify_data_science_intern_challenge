#!/usr/bin/env python
# coding: utf-8

# # Summary

# In[1]:


import pandas as pd
orders = pd.read_csv('data/orders.csv')


# ## Question 1: 
# *a. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.*  
# 
# **Assume the data is in USD, the amount of AOV does not make sense, given**  
# 1. **The sold sneakers are affordable items (i.e. says USD100).**
# 2. **Each shops sells one model**
# **This indicated customers are making bulk purchases of 30 pairs of identical shoes per order in average.**  
# **Shopify is well known among B2C eCommerce. Therefore this result is unlikely to happen.**

# *b. What metric would you report for this dataset?*
# 
# **Because of the outliners, we can use `median`, which is less sensitive to outliers.**

# *c. What is its value?*

# In[2]:


print(f'The median of order value is USD{ orders["order_amount"].median()}')


# ## Question 2:
# a. How many orders were shipped by Speedy Express in total?  
SELECT count(o.ShipperID) FROM Shippers s
JOIN Orders o on s.ShipperID = o.ShipperID
WHERE ShipperName = 'Speedy Express'
# The answer is : **54**

# b. What is the last name of the employee with the most orders? 
SELECT e.LastName, MAX(Count) 
FROM (
	SELECT EmployeeID, COUNT(EmployeeID) "Count" 
    FROM [Orders] 
    GROUP BY EmployeeID) o
JOIN Employees e ON o.EmployeeID = e.EmployeeID
# The answer is : **Peacock**  
# ** The reason of NOT using LIMIT 1 is because there maybe more that one employee has the small amount of maximum orders.

# c. What product was ordered the most by customers in Germany? 
SELECT p.ProductID, p.ProductName, SUM(Quantity) "Total_Qty" FROM [Customers] c
JOIN Orders o ON c.CustomerID = o.CustomerID
JOIN OrderDetails od ON o.OrderID = od.OrderID
JOIN Products p on od.ProductID = p.ProductID
WHERE c.Country = 'Germany'
GROUP BY p.ProductID
ORDER BY Total_Qty DESC
LIMIT 5
# The answer is : **Boston Crab Meat**  
# ** This is another approach for Top 1 category, simply draw out more than one values to make sure there is no duplicated top values.
