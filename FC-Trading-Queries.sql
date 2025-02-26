-- SQL project using the FC-Trading Database v2

-- Question 1: Which 10 products generated the highest revenue in Q4 2024?
WITH Last_Quarter AS (
    SELECT 
        DATE '2024-10-01' AS last_quarter_start,
        DATE '2024-12-31' AS last_quarter_end
)
SELECT 
    p.ProductID, 
    p.ProductName, 
    SUM(od.Quantity * p.UnitPrice) AS total_revenue
FROM `fc-trading-v2.FC_Trading_V2.order_details` od
JOIN `fc-trading-v2.FC_Trading_V2.orders` o ON od.OrderID = o.OrderID
JOIN `fc-trading-v2.FC_Trading_V2.products` p ON od.ProductID = p.ProductID
WHERE 
    o.OrderDate BETWEEN (SELECT last_quarter_start FROM Last_Quarter) 
                     AND (SELECT last_quarter_end FROM Last_Quarter)
GROUP BY 
    p.ProductID, p.ProductName
ORDER BY 
    total_revenue DESC
LIMIT 10;

-- Question 2: Which 10 countries generated the highest revenue?
SELECT 
    c.Country, 
    ROUND(SUM(od.Quantity * p.UnitPrice * (1 - od.Discount)),2) AS Total_Revenue
FROM `fc-trading-v2.FC_Trading_V2.order_details` od
JOIN `fc-trading-v2.FC_Trading_V2.orders` o ON od.OrderID = o.OrderID
JOIN `fc-trading-v2.FC_Trading_V2.products` p ON od.ProductID = p.ProductID
JOIN `fc-trading-v2.FC_Trading_V2.customers` c ON o.CustomerID = c.CustomerID
WHERE EXTRACT(YEAR FROM o.OrderDate) = 2024
GROUP BY c.Country
ORDER BY total_revenue DESC;

-- Question 3: What was the revenue distribution per product category in 2024?
SELECT 
    p.Category, 
    SUM(od.Quantity * p.UnitPrice * (1 - od.Discount)) AS total_revenue
FROM `fc-trading-v2.FC_Trading_V2.order_details` od
JOIN `fc-trading-v2.FC_Trading_V2.orders` o ON od.OrderID = o.OrderID
JOIN `fc-trading-v2.FC_Trading_V2.products` p ON od.ProductID = p.ProductID
WHERE EXTRACT(YEAR FROM o.OrderDate) = 2024
GROUP BY p.Category
ORDER BY total_revenue DESC;

-- Question 4: Which countries had the highest revenue growth in 2024?
WITH RevenueByCountry AS (
    SELECT 
        c.Country,
        EXTRACT(YEAR FROM o.OrderDate) AS order_year,
        SUM(od.Quantity * p.UnitPrice * (1 - od.Discount)) AS total_revenue
    FROM `fc-trading-v2.FC_Trading_V2.order_details` od
    JOIN `fc-trading-v2.FC_Trading_V2.orders` o ON od.OrderID = o.OrderID
    JOIN `fc-trading-v2.FC_Trading_V2.products` p ON od.ProductID = p.ProductID
    JOIN `fc-trading-v2.FC_Trading_V2.customers` c ON o.CustomerID = c.CustomerID
    WHERE EXTRACT(YEAR FROM o.OrderDate) IN (2023, 2024)
    GROUP BY c.Country, order_year
),
RevenueGrowth AS (
    SELECT 
        r2024.Country,
        r2024.total_revenue AS revenue_2024,
        COALESCE(r2023.total_revenue, 0) AS revenue_2023,
        (r2024.total_revenue - COALESCE(r2023.total_revenue, 0)) / NULLIF(r2023.total_revenue, 0) AS revenue_growth
    FROM RevenueByCountry r2024
    LEFT JOIN RevenueByCountry r2023 
        ON r2024.Country = r2023.Country AND r2023.order_year = 2023
    WHERE r2024.order_year = 2024
)
SELECT Country, revenue_2024, revenue_2023, revenue_growth
FROM RevenueGrowth
ORDER BY revenue_growth DESC
LIMIT 10;

-- Question 5: What was the average yearly revenue growth from 2015 to 2024?
WITH RevenueByYear AS (
    SELECT 
        c.Country,
        EXTRACT(YEAR FROM o.OrderDate) AS Year,
        SUM(od.Quantity * (p.UnitPrice - od.Discount)) AS TotalRevenue
    FROM `fc-trading-v2.FC_Trading_V2.orders` o
    JOIN `fc-trading-v2.FC_Trading_V2.order_details` od ON o.OrderID = od.OrderID
    JOIN `fc-trading-v2.FC_Trading_V2.products` p ON od.ProductID = p.ProductID
    JOIN `fc-trading-v2.FC_Trading_V2.customers` c ON o.CustomerID = c.CustomerID
    WHERE EXTRACT(YEAR FROM o.OrderDate) BETWEEN 2015 AND 2024
    GROUP BY c.Country, EXTRACT(YEAR FROM o.OrderDate)
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
),
AverageGrowth AS (
    SELECT 
        Country,
        AVG(RevenueGrowthPercent) AS AvgRevenueGrowth
    FROM RevenueGrowth
    WHERE Year BETWEEN 2015 AND 2024
    GROUP BY Country
)
SELECT * FROM AverageGrowth
ORDER BY AvgRevenueGrowth DESC;


-- Question 6: Who were the top 10 customers in 2024
SELECT 
    c.CustomerID, 
    c.CompanyName,
    c.Country, 
    SUM(od.Quantity * p.UnitPrice) AS total_revenue
FROM `fc-trading-v2.FC_Trading_V2.order_details` od
JOIN `fc-trading-v2.FC_Trading_V2.orders` o ON od.OrderID = o.OrderID
JOIN `fc-trading-v2.FC_Trading_V2.customers` c ON o.CustomerID = c.CustomerID
JOIN `fc-trading-v2.FC_Trading_V2.products` p ON od.ProductID = p.ProductID
WHERE 
    EXTRACT(YEAR FROM o.OrderDate) = 2024
GROUP BY 
    c.CustomerID, c.CompanyName, c.Country
ORDER BY 
    total_revenue DESC
LIMIT 10;

-- Question 7: Which customers had the most frequent orders in the last 3 years?
SELECT 
    c.CustomerID, 
    c.CompanyName, 
    COUNT(o.OrderID) AS TotalOrders
FROM `fc-trading-v2.FC_Trading_V2.customers` c
JOIN `fc-trading-v2.FC_Trading_V2.orders` o 
    ON c.CustomerID = o.CustomerID
WHERE o.OrderDate BETWEEN '2022-01-01' AND '2024-12-31'
GROUP BY c.CustomerID, c.CompanyName
HAVING COUNT(o.OrderID) > 1
ORDER BY TotalOrders DESC;

-- Question 8: Which suppliers had the best on-time delivery rate and highest quality score?
SELECT 
    s.SupplierID,
    s.CompanyName,
    sp.OnTimeDeliveryRate,
    sp.QualityScore,
    sp.AverageLeadTime,
    sp.LastEvaluatedDate
FROM `fc-trading-v2.FC_Trading_V2.supplier_performance` sp
JOIN `fc-trading-v2.FC_Trading_V2.suppliers` s ON sp.SupplierID = s.SupplierID
ORDER BY sp.OnTimeDeliveryRate DESC, sp.QualityScore DESC;
