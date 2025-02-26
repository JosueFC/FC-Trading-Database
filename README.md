# FC-Trading-Database
Creation of a Synthetic Database for Querying and Data Science Applications.

The goal of this project is to design and develop a comprehensive synthetic database for FC Trading, a fictional international foods company involved in the import and export of a diverse range of food products. This database will serve as a robust and versatile tool for data science applications, offering a variety of use cases for querying and data analysis.

FC Trading operates across multiple countries, dealing with various product categories such as produce, condiments, dairy, meat and seafood.  It has a global supply chain network, including suppliers, shippers, and clients. The synthetic database will model this complexity, incorporating key aspects of international trade, inventory management, customer behavior, and financial transactions.

# Database Schema Overview

## 1. Suppliers
Stores information about product suppliers.

| Column Name    | Data Type | Description                                      |
|----------------|-----------|--------------------------------------------------|
| SupplierID     | INT       | Primary Key, Unique identifier for supplier      |
| CompanyName    | VARCHAR   | Name of the supplier company                     |
| ContactName    | VARCHAR   | Contact person at the supplier                   |
| Phone          | VARCHAR   | Contact phone number                             |
| StreetAddress  | VARCHAR   | Street address of the supplier                   |
| Country        | VARCHAR   | Country of the supplier                          |

## 2. Products
Stores information about products, excluding stock-related details.

| Column Name      | Data Type | Description                                            |
|------------------|-----------|--------------------------------------------------------|
| ProductID        | INT       | Primary Key, Unique identifier for product             |
| ProductName      | VARCHAR   | Name of the product                                    |
| SupplierID       | INT       | Foreign Key, references Suppliers(SupplierID)          |
| Category         | VARCHAR   | Product category (e.g., Beverages, Snacks)             |
| QuantityPerUnit  | VARCHAR   | Description of the product packaging (e.g., 12-pack)   |
| UnitPrice        | DECIMAL   | Price per unit of the product                          |

## 3. Shippers
Stores information about shippers that handle product deliveries.

| Column Name  | Data Type | Description                              |
|--------------|-----------|------------------------------------------|
| ShipperID    | INT       | Primary Key, Unique identifier for shipper |
| CompanyName  | VARCHAR   | Name of the shipper company             |
| Phone        | VARCHAR   | Phone number for the shipper company    |

## 4. Orders
Stores information about customer orders.

| Column Name   | Data Type | Description                                             |
|---------------|-----------|---------------------------------------------------------|
| OrderID       | INT       | Primary Key, Unique identifier for the order           |
| CustomerID    | INT       | Foreign Key, references Customers(CustomerID)          |
| EmployeeID    | INT       | Foreign Key, references Employees(EmployeeID)          |
| OrderDate     | DATE      | Date when the order was placed                          |
| RequiredDate  | DATE      | The date when the order should be delivered             |
| ShippedDate   | DATE      | The date when the order was shipped (nullable)          |
| ShipVia       | INT       | Foreign Key, references Shippers(ShipperID)             |
| Freight       | DECIMAL   | Shipping cost                                           |
| ShipName      | VARCHAR   | Name of the person or company shipping the order (nullable) |
| ShipAddress   | VARCHAR   | Shipping address                                        |
| ShipCity      | VARCHAR   | Shipping city                                           |
| ShipRegion    | VARCHAR   | Shipping region (nullable)                              |
| ShipPostalCode| VARCHAR   | Shipping postal code                                    |
| ShipCountry   | VARCHAR   | Shipping country                                        |

## 5. OrderDetails
Stores the details of each product within an order.

| Column Name    | Data Type | Description                               |
|----------------|-----------|-------------------------------------------|
| OrderDetailID  | INT       | Primary Key, Unique identifier for the order detail |
| OrderID        | INT       | Foreign Key, references Orders(OrderID)   |
| ProductID      | INT       | Foreign Key, references Products(ProductID) |
| Quantity       | INT       | Quantity of the product in the order      |
| Discount       | DECIMAL   | Discount applied on the product (if any)  |

## 6. PaymentInformation
Stores payment details for orders.

| Column Name    | Data Type | Description                               |
|----------------|-----------|-------------------------------------------|
| PaymentID      | INT       | Primary Key, Unique identifier for the payment |
| OrderID        | INT       | Foreign Key, references Orders(OrderID)   |
| PaymentMethod  | VARCHAR   | Method of payment (e.g., Cash, Credit Card) |
| PaymentAmount  | DECIMAL   | Total payment amount                      |
| PaymentDate    | DATE      | Date when payment was made                |
| PaymentStatus  | VARCHAR   | Status of payment (e.g., Paid, Pending)   |

## 7. Inventory
Stores inventory details for products (stock levels, reorder points, etc.).

| Column Name      | Data Type | Description                                          |
|------------------|-----------|------------------------------------------------------|
| ProductID        | INT       | Foreign Key, references Products(ProductID)          |
| StockQuantity    | INT       | Quantity of the product in stock                     |
| ReorderLevel     | INT       | The stock level at which a reorder is triggered      |
| ReorderQuantity  | INT       | The quantity to reorder when stock hits the reorder level |
| LastRestockDate  | DATE      | Date the product was last restocked                  |
| SupplierID       | INT       | Foreign Key, references Suppliers(SupplierID)        |

## 8. ShippingInformation
Stores information about the shipping status and tracking details for orders.

| Column Name    | Data Type | Description                                      |
|----------------|-----------|--------------------------------------------------|
| ShippingID     | INT       | Primary Key, Unique identifier for the shipping  |
| OrderID        | INT       | Foreign Key, references Orders(OrderID)          |
| ShipperID      | INT       | Foreign Key, references Shippers(ShipperID)      |
| TrackingNumber | VARCHAR   | Tracking number for the shipment                 |
| ShippingStatus | VARCHAR   | Current shipping status (e.g., In Transit, Delivered) |
| DeliveryDate   | DATE      | Date the shipment was delivered                  |

## 9. SupplierPerformance
Stores performance metrics for suppliers.

| Column Name         | Data Type | Description                                        |
|---------------------|-----------|----------------------------------------------------|
| SupplierID          | INT       | Foreign Key, references Suppliers(SupplierID)      |
| OnTimeDeliveryRate  | DECIMAL   | Percentage of orders delivered on time            |
| QualityScore        | DECIMAL   | Quality score assigned to the supplier (out of 5)  |
| AverageLeadTime     | INT       | Average number of days taken for delivery         |
| LastEvaluatedDate   | DATE      | Date when the supplier was last evaluated          |

## 10. SupplierContracts
Stores details about supplier contracts.

| Column Name   | Data Type | Description                                      |
|---------------|-----------|--------------------------------------------------|
| ContractID    | INT       | Primary Key, Unique identifier for the contract  |
| SupplierID    | INT       | Foreign Key, references Suppliers(SupplierID)    |
| StartDate     | DATE      | Date when the contract started                   |
| EndDate       | DATE      | Date when the contract ends                      |
| ContractTerms | VARCHAR   | Terms of the contract (e.g., Fixed Price, Volume Discount) |

## 11. ShippingDelays
Stores information about any shipping delays.

| Column Name   | Data Type | Description                                      |
|---------------|-----------|--------------------------------------------------|
| DelayID       | INT       | Primary Key, Unique identifier for the delay     |
| ShippingID    | INT       | Foreign Key, references ShippingInformation(ShippingID) |
| Reason        | VARCHAR   | Reason for the delay (e.g., Weather, Traffic)    |
| DelayDuration | INT       | Duration of the delay in days                    |

## 12. RouteOptimization
Stores information on shipping route optimization.

| Column Name   | Data Type | Description                                      |
|---------------|-----------|--------------------------------------------------|
| RouteID       | INT       | Primary Key, Unique identifier for the route     |
| ShipperID     | INT       | Foreign Key, references Shippers(ShipperID)      |
| AvgDeliveryTime | DECIMAL | Average delivery time in days                    |
| AvgCost        | DECIMAL  | Average cost for shipping via this route         |


# Business questions

# Question 1
Which 10 products generated the highest revenue in Q4 2024?
<details>
  <summary>Results</summary>
  
  | Row | ProductID | Product Name   | Total Revenue  |
  |-----|-----------|----------------|----------------|
  | 1   | 10        | Chamomile Tea  | 30,252.60      |
  | 2   | 44        | Corn           | 27,793.60      |
  | 3   | 151       | Orange Juice   | 25,899.50      |
  | 4   | 8         | Bacon          | 25,666.20      |
  | 5   | 41        | Mustard Greens | 25,311.00      |
  | 6   | 98        | Truffle Oil    | 25,158.70      |
  | 7   | 18        | Scallops       | 24,399.23      |
  | 8   | 73        | Tuna Steak     | 24,030.00      |
  | 9   | 138       | Coconut Milk   | 23,217.48      |
  | 10  | 89        | Horseradish    | 23,137.08      |

</details>


# Question 2
Which 10 countries generated the highest revenue?
<details>
  <summary>Results</summary>

|     Country        |   Total Revenue   |
|--------------------|-------------------|
| United States      | 1,902,444.05      |
| Germany            | 720,279.60        |
| Canada             | 610,176.40        |
| United Kingdom     | 583,873.48        |
| Brazil             | 502,694.95        |
| France             | 458,021.27        |
| Mexico             | 337,724.13        |
| Spain              | 288,245.14        |
| Italy              | 166,735.65        |
| Panama             | 124,097.56        |


</details>

# Question 3
What was the revenue distribution per product category in 2024?
<details>
  <summary>Results</summary>

  | Row | Category     | Total Revenue         |
  |-----|--------------|-----------------------|
  | 1   | Condiments   | 1,135,774.12          |
  | 2   | Beverages    | 1,124,646.53          |
  | 3   | Seafood      | 1,092,799.42          |
  | 4   | Dairy        | 973,502.71            |
  | 5   | Produce      | 939,477.87            |
  | 6   | Meat/Poultry | 899,082.94            |

</details>

# Question 4
Which countries had the highest revenue growth in 2024?
<details>
  <summary>Results</summary>

  | Row | Country        | Revenue 2024     | Revenue 2023     | Revenue Growth     |
  |-----|----------------|------------------|------------------|--------------------|
  | 1   | Brazil         | 502,694.95       | 454,799.79       | 0.1053             |
  | 2   | Australia      | 59,166.35        | 54,744.84        | 0.0808             |
  | 3   | United States  | 1,902,444.05     | 1,786,455.54     | 0.0649             |
  | 4   | United Kingdom | 583,873.48       | 549,560.78       | 0.0624             |
  | 5   | Sweden         | 55,214.69        | 52,407.13        | 0.0536             |
  | 6   | Mexico         | 337,724.13       | 321,947.36       | 0.0490             |
  | 7   | South Korea    | 65,664.81        | 62,966.72        | 0.0428             |
  | 8   | Italy          | 166,735.65       | 166,258.39       | 0.0029             |
  | 9   | Germany        | 720,279.60       | 719,308.82       | 0.0013             |
  | 10  | France         | 458,021.27       | 458,473.26       | -0.0010            |

</details>

# Question 5
What was the average yearly revenue growth from 2015 to 2024?
<details>
  <summary>Response</summary>

  | Row | Country         | AvgRevenueGrowth |
  |-----|-----------------|------------------|
  | 1   | South Korea     | 4.5220           |
  | 2   | Australia       | 3.4014           |
  | 3   | Mexico          | 3.0057           |
  | 4   | Panama          | 2.7007           |
  | 5   | Sweden          | 2.6784           |
  | 6   | Norway          | 2.6068           |
  | 7   | Japan           | 2.4399           |
  | 8   | United States   | 2.3088           |
  | 9   | Germany         | 2.1172           |
  | 10  | United Kingdom  | 2.0027           |
  | 11  | Canada          | 1.9586           |
  | 12  | Brazil          | 1.9216           |
  | 13  | France          | 1.8808           |
  | 14  | Austria         | 1.2341           |
  | 15  | Spain           | 1.1753           |
  | 16  | Netherlands     | 0.4581           |
  | 17  | Italy           | 0.3422           |

</details>

# Question 6
What were the top 10 customers in 2024
<details>
  <summary>Results</summary>

  | Row | CustomerID | CompanyName               | Total Revenue  |
  |-----|------------|---------------------------|----------------|
  | 1   | 2895       | Stewart Group             | 6380.22        |
  | 2   | 6029       | Hendricks-Elliott         | 6307.63        |
  | 3   | 6077       | Stone, Riggs and Johnson  | 6032.47        |
  | 4   | 5281       | Waters PLC                | 6010.75        |
  | 5   | 2056       | Davis-Ortiz               | 5579.28        |
  | 6   | 2436       | Torres-Brooks             | 5341.84        |
  | 7   | 4765       | Watson, West and Cook     | 5263.56        |
  | 8   | 2552       | Anderson PLC              | 5197.69        |
  | 9   | 1974       | Baird-Williams            | 5176.38        |
  | 10  | 4378       | Anderson PLC              | 5092.48        |

</details>

# Question 7
Which customers had the most frequent orders in the last 3 years?
<details>
  <summary>Results</summary>

| CustomerID | Company Name                      | Total Orders |
|------------|-----------------------------------|--------------|
| 7761       | Watson and Sons                   | 17           |
| 6459       | Webb-Ortega                       | 17           |
| 6007       | Bennett, Chavez and Anderson      | 17           |
| 2992       | Maxwell, Rice and Watson          | 17           |
| 2763       | Booth, Rodriguez and Armstrong    | 17           |
| 156        | Hill Inc                          | 17           |
| 3239       | White Inc                         | 17           |
| 4938       | Rojas Ltd                         | 17           |
| 3668       | Davis and Sons                    | 16           |
| 637        | Wilcox-Robertson                  | 16           |
| 2346       | Park, Maynard and Ruiz            | 16           |
| 6352       | Hampton-Wilson                    | 16           |
| 102        | Patterson, Smith and Jones        | 16           |

</details>

# Question 7
Which suppliers had the best on-time delivery rate and highest quality score?
<details>
  <summary>Results</summary>
  ## Supplier Performance Data

| SupplierID | Company Name                      | OnTimeDeliveryRate | QualityScore | AverageLeadTime | LastEvaluatedDate |
|------------|-----------------------------------|--------------------|--------------|-----------------|-------------------|
| 290        | Sanchez Ltd                       | 99.55              | 4.19         | 24              | 2024-03-28        |
| 250        | Ford LLC                          | 99.53              | 4.8          | 14              | 2024-03-05        |
| 13         | Norman, Cordova and Fry           | 99.45              | 3.12         | 14              | 2024-12-28        |
| 35         | Bell-Nichols                      | 99.43              | 4.91         | 5               | 2024-11-29        |
| 63         | Olsen, Jackson and White          | 99.27              | 3.7          | 10              | 2024-11-30        |
| 316        | Fernandez, Garcia and Gomez       | 99.25              | 3.15         | 18              | 2024-04-15        |
| 308        | Taylor-Pearson                    | 99.07              | 4.09         | 22              | 2024-07-05        |
| 208        | Gibson-Armstrong                  | 98.89              | 4.23         | 5               | 2025-01-16        |
| 5          | Pierce-Jackson                    | 98.82              | 3.03         | 14              | 2024-06-13        |
| 216        | Hall Ltd                          | 98.79              | 4.24         | 14              | 2024-05-12        |
| 107        | Hodge-Fuller                      | 98.69              | 3.37         | 28              | 2024-05-11        |
| 191        | Hansen-Sims                       | 98.62              | 3.37         | 12              | 2024-05-10        |
| 196        | Fletcher-Kane                     | 98.6               | 3.84         | 28              | 2024-09-15        |

</details>
