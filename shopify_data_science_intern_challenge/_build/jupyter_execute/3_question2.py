#!/usr/bin/env python
# coding: utf-8

# # Question 2

# ## How many orders were shipped by Speedy Express in total?  

# Answer in single query is:
SELECT count(o.ShipperID) FROM Shippers s
JOIN Orders o on s.ShipperID = o.ShipperID
WHERE ShipperName = 'Speedy Express'
# The answer is : **54**

# However, in reality, depends on the application, we don't need to join the table.  
# We can find the shipperID of `Speedy Express`, then count the Shipper table to enhance performance, if shipperID is not indexed.
SELECT * FROM Shippers WHERE ShipperName = 'Speedy Express' # ShipperID = 1SELECT count(ShipperID) FROM Orders WHERE ShipperID = 1
# ## What is the last name of the employee with the most orders? 

# Answer in single query is:
SELECT e.LastName, MAX(Count) 
FROM (
	SELECT EmployeeID, COUNT(EmployeeID) "Count" 
    FROM [Orders] 
    GROUP BY EmployeeID) o
JOIN Employees e ON o.EmployeeID = e.EmployeeID
# The answer is : **Peacock**  
# ** The reason of NOT using LIMIT 1 is because there maybe more that one employee has the small amount of maximum orders.

# Similar to part(a), if single query is not necessary, I will query the top five to make sure the employee of maximum order is unique, then query the employee name.
SELECT EmployeeID, COUNT(EmployeeID) "Count" 
FROM [Orders] 
GROUP BY EmployeeID
ORDER BY Count DESC
LIMIT 5SELECT LastName FROM Employees WHERE EmployeeID = 4
# ## What product was ordered the most by customers in Germany? 

# Answer in single query is:
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
