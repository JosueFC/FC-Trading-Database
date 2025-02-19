--SQL project using the FC-Trading Database v2

--What are the 10 best selling products and their categories
SELECT 
    p.ProductID, 
    p.ProductName, 
    p.Category, 
    SUM(od.Quantity * (p.UnitPrice - od.Discount)) AS TotalRevenue
FROM `fc-trading-v2.fc_trading_v2.order_details` od
JOIN `fc-trading-v2.fc_trading_v2.products` p 
    ON od.ProductID = p.ProductID
GROUP BY p.ProductID, p.ProductName, p.Category
ORDER BY TotalRevenue DESC
LIMIT 10;

--Order categories by revenue
SELECT  
    p.Category, 
    SUM(od.Quantity * (p.UnitPrice - od.Discount)) AS TotalRevenue
FROM `fc-trading-v2.fc_trading_v2.order_details` od
JOIN `fc-trading-v2.fc_trading_v2.products` p 
    ON od.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY TotalRevenue DESC
LIMIT 10;

--Customer Purchase Analysis
SELECT c.CustomerID, c.CompanyName, c.Country, SUM(od.Quantity * (p.UnitPrice - od.Discount)) AS TotalSpent
FROM `fc-trading-v2.fc_trading_v2.customers` c
JOIN `fc-trading-v2.fc_trading_v2.orders` o ON c.CustomerID = o.CustomerID
JOIN `fc-trading-v2.fc_trading_v2.order_details` od ON o.OrderID = od.OrderID
JOIN `fc-trading-v2.fc_trading_v2.products` p ON od.ProductID = p.ProductID
GROUP BY c.CustomerID, c.CompanyName,c.Country
ORDER BY TotalSpent DESC
LIMIT 10;

--Revenue By Country
SELECT c.Country, SUM(od.Quantity * (p.UnitPrice - od.Discount)) AS Revenue
FROM `fc-trading-v2.fc_trading_v2.customers` c
JOIN `fc-trading-v2.fc_trading_v2.orders` o ON c.CustomerID = o.CustomerID
JOIN `fc-trading-v2.fc_trading_v2.order_details` od ON o.OrderID = od.OrderID
JOIN `fc-trading-v2.fc_trading_v2.products` p ON od.ProductID = p.ProductID
GROUP BY c.Country
ORDER BY Revenue DESC
LIMIT 10;

--Employee Sales Performance
SELECT e.EmployeeID, e.FirstName, e.LastName, SUM(od.Quantity * (p.UnitPrice - od.Discount)) AS TotalRevenue
FROM `fc-trading-v2.fc_trading_v2.employees` e
JOIN `fc-trading-v2.fc_trading_v2.orders` o ON e.EmployeeID = o.EmployeeID
JOIN `fc-trading-v2.fc_trading_v2.order_details` od ON o.OrderID = od.OrderID
JOIN `fc-trading-v2.fc_trading_v2.products` p ON od.ProductID = p.ProductID
GROUP BY e.EmployeeID, e.FirstName, e.LastName
ORDER BY TotalRevenue DESC;

--Top 5 suppliers based on total product sales.
SELECT s.SupplierID, s.CompanyName, SUM(od.Quantity * (p.UnitPrice - od.Discount)) AS TotalSales
FROM `fc-trading-v2.fc_trading_v2.suppliers` s
JOIN `fc-trading-v2.fc_trading_v2.products` p ON s.SupplierID = p.SupplierID
JOIN `fc-trading-v2.fc_trading_v2.order_details` od ON p.ProductID = od.ProductID
GROUP BY s.SupplierID, s.CompanyName
ORDER BY TotalSales DESC
LIMIT 5;

--Identify products that are low in stock and need reordering.
SELECT p.ProductID, p.ProductName, i.StockQuantity, i.ReorderLevel,
       CASE 
           WHEN i.StockQuantity <= i.ReorderLevel THEN 'Restock Needed'
           ELSE 'Sufficient Stock'
       END AS StockStatus
FROM `fc-trading-v2.fc_trading_v2.products` p
JOIN `fc-trading-v2.fc_trading_v2.inventory` i ON p.ProductID = i.ProductID
ORDER BY i.StockQuantity ASC;



--Compute Yearly Revenue Growth by Country
WITH RevenueByYear AS (
    SELECT 
        c.Country,
        YEAR(o.OrderDate) AS Year,
        SUM(od.Quantity * (p.UnitPrice - od.Discount)) AS TotalRevenue
    FROM `fc-trading-v2.fc_trading_v2.orders` o
    JOIN `fc-trading-v2.fc_trading_v2.order_details` od ON o.OrderID = od.OrderID
    JOIN `fc-trading-v2.fc_trading_v2.products` p ON od.ProductID = p.ProductID
    JOIN `fc-trading-v2.fc_trading_v2.customers` c ON o.CustomerID = c.CustomerID
    GROUP BY c.Country, YEAR(o.OrderDate)
),
RevenueGrowth AS (
    SELECT 
        r1.Country,
        r1.Year,
        r1.TotalRevenue,
        (r1.TotalRevenue - r2.TotalRevenue) / NULLIF(r2.TotalRevenue, 0) * 100 AS RevenueGrowthPercent
    FROM RevenueByYear r1
    LEFT JOIN RevenueByYear r2 
        ON r1.Country = r2.Country 
        AND r1.Year = r2.Year + 1
)
SELECT * FROM RevenueGrowth
ORDER BY RevenueGrowthPercent DESC;

--Data to be analyzed with R

--Create Monthly Revenue Table
CREATE TABLE MonthlyRevenue AS
SELECT 
    DATE_FORMAT(o.OrderDate, '%Y-%m') AS Month, 
    SUM(od.Quantity * (p.UnitPrice - od.Discount)) AS TotalRevenue
FROM `fc-trading-v2.fc_trading_v2.orders` o
JOIN `fc-trading-v2.fc_trading_v2.order_details` od ON o.OrderID = od.OrderID
JOIN `fc-trading-v2.fc_trading_v2.products` p ON od.ProductID = p.ProductID
GROUP BY Month
ORDER BY Month;

--Monthly revenue by product
SELECT 
    p.Category,
    DATE_FORMAT(o.OrderDate, '%Y-%m') AS Month,
    SUM(od.Quantity * (p.UnitPrice - od.Discount)) AS TotalRevenue
FROM 
    `fc-trading-v2.fc_trading_v2.orders` o
JOIN 
    `fc-trading-v2.fc_trading_v2.order_details` od ON o.OrderID = od.OrderID
JOIN 
    `fc-trading-v2.fc_trading_v2.products` p ON od.ProductID = p.ProductID
GROUP BY 
    p.Category, 
    YEAR(o.OrderDate), 
    MONTH(o.OrderDate)
ORDER BY 
    OrderYear, OrderMonth, ProductName;