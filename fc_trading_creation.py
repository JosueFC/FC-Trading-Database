import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
Faker.seed(42)
np.random.seed(42)

# Parameters for dataset size

# Customer Growth: 5% annual growth
start_customers = 5000
growth_rate = 0.05  # 5% annual growth for customers
num_customers = int(start_customers * (1 + growth_rate)**10)

# Employee Growth: 3% annual growth
start_employees = 200
employee_growth_rate = 0.03  # 3% annual growth for employees
num_employees = int(start_employees * (1 + employee_growth_rate)**10)

# Supplier Growth: 3% annual growth
start_suppliers = 250
supplier_growth_rate = 0.03  # 3% annual growth for suppliers
num_suppliers = int(start_suppliers * (1 + supplier_growth_rate)**10)

# Product Growth: 5% annual growth
start_products = 100
product_growth_rate = 0.05  # 5% annual growth for products
num_products = int(start_products * (1 + product_growth_rate)**10)

# Order Growth: 7% annual growth
start_orders = int(start_customers * 20)  # Assuming 20 orders per customer at the start
order_growth_rate = 0.07  # 7% annual growth for orders
num_orders = int(start_orders * (1 + order_growth_rate)**10)

# Shipper Growth: 4% annual growth
num_shippers = 20  # Slight increase over 10 years
shipper_growth_rate = 0.04  # 4% annual growth for shippers
num_shippers = int(num_shippers * (1 + shipper_growth_rate)**10)

# Restrict customers to America and Europe
allowed_countries = [
    'United States', 'Canada', 'Mexico', 'Panama', 'Brazil', 'Germany', 'France', 
    'United Kingdom', 'Spain', 'Italy', 'Netherlands', 'Austria', 'Sweden', 'Norway', 
    'Japan', 'South Korea', 'Australia'
]

# Assign higher probabilities to certain countries for variance
country_weights = np.array([
    0.30,  # United States (30% of customers)
    0.10,  # Canada
    0.05,  # Mexico
    0.02,  # Panama
    0.08,  # Brazil
    0.12,  # Germany
    0.08,  # France
    0.10,  # United Kingdom
    0.05,  # Spain
    0.03,  # Italy
    0.02,  # Netherlands
    0.01,  # Austria
    0.01,  # Sweden
    0.01,  # Norway
    0.01,  # Japan
    0.01,  # South Korea
    0.01   # Australia
])

# Ensure weights sum to 1
country_weights /= country_weights.sum()

# Product categories and sample product names (same as before)
category_products = {
    'Beverages': [
        'Cola', 'Diet Cola', 'Cherry Cola', 'Root Beer', 'Ginger Ale', 'Lemonade', 'Apple Juice', 'Cranberry Juice', 
        'Orange Juice', 'Pineapple Juice', 'Grape Juice', 'Tomato Juice', 'Fruit Punch', 'Iced Coffee', 'Cold Brew Coffee', 
        'Hot Coffee', 'Iced Tea', 'Black Tea', 'Green Tea', 'Herbal Tea', 'Chamomile Tea', 'Peppermint Tea', 'Energy Drink',
        'Sports Drink', 'Sparkling Water', 'Mineral Water', 'Coconut Water', 'Vitamin Water', 'Hot Chocolate', 
        'Almond Milk', 'Soy Milk', 'Oat Milk', 'Rice Milk', 'Matcha Latte', 'Iced Matcha', 'Lassi', 'Milkshake', 'Kombucha'
    ],
    'Condiments': [
        'Ketchup', 'Mustard', 'Soy Sauce', 'Hot Sauce', 'Barbecue Sauce', 'Mayonnaise', 'Relish', 'Ranch Dressing', 
        'Caesar Dressing', 'Vinegar', 'Apple Cider Vinegar', 'Balsamic Vinegar', 'Red Wine Vinegar', 'Olive Oil', 
        'Sunflower Oil', 'Canola Oil', 'Vegetable Oil', 'Truffle Oil', 'Peanut Butter', 'Almond Butter', 'Honey', 
        'Maple Syrup', 'Agave Syrup', 'Worcestershire Sauce', 'Teriyaki Sauce', 'Pesto', 'Chimichurri', 'Hummus', 
        'Tahini', 'Tabasco Sauce', 'Sriracha', 'Horseradish', 'Chili Oil', 'Mango Chutney', 'Tartar Sauce', 'Tzatziki'
    ],
    'Dairy': [
        'Cheddar Cheese', 'Mozzarella Cheese', 'Swiss Cheese', 'Gouda', 'Parmesan Cheese', 'Provolone', 'Brie', 
        'Camembert', 'Blue Cheese', 'Feta Cheese', 'Goat Cheese', 'Cream Cheese', 'Ricotta Cheese', 'Cottage Cheese', 
        'Greek Yogurt', 'Regular Yogurt', 'Almond Yogurt', 'Soy Yogurt', 'Sour Cream', 'Heavy Cream', 'Light Cream', 
        'Half and Half', 'Butter', 'Margarine', 'Clarified Butter (Ghee)', 'Buttermilk', 'Ice Cream', 'Gelato', 
        'Frozen Yogurt', 'Cottage Cheese', 'Skyr', 'Coconut Milk', 'Cashew Milk', 'Rice Pudding', 'Custard'
    ],
    'Meat/Poultry': [
        'Chicken Breast', 'Chicken Thighs', 'Chicken Wings', 'Chicken Drumsticks', 'Chicken Tenderloins', 'Whole Chicken', 
        'Ground Chicken', 'Turkey Breast', 'Turkey Sausage', 'Pork Ribs', 'Pork Tenderloin', 'Pork Chops', 'Pork Belly', 
        'Bacon', 'Pancetta', 'Sausages', 'Lamb Chops', 'Lamb Shank', 'Lamb Rack', 'Veal', 'Beef Ribeye', 'Beef Sirloin', 
        'Beef T-Bone', 'Ground Beef', 'Beef Brisket', 'Beef Tenderloin', 'Pastrami', 'Corned Beef', 'Duck Breast', 
        'Duck Legs', 'Goose', 'Rabbit', 'Venison', 'Bison', 'Mutton', 'Quail', 'Fois Gras', 'Smoked Ham', 'Prosciutto'
    ],
    'Produce': [
        'Apples', 'Bananas', 'Pineapple', 'Mango', 'Grapes', 'Blueberries', 'Strawberries', 'Raspberries', 'Blackberries', 
        'Oranges', 'Lemons', 'Limes', 'Kiwi', 'Plums', 'Pears', 'Cherries', 'Cantaloupe', 'Watermelon', 'Papaya', 
        'Tangerines', 'Avocados', 'Tomatoes', 'Cucumbers', 'Carrots', 'Beets', 'Radishes', 'Garlic', 'Onions', 'Shallots', 
        'Lettuce', 'Spinach', 'Kale', 'Arugula', 'Collard Greens', 'Mustard Greens', 'Cabbage', 'Brussels Sprouts', 
        'Broccoli', 'Cauliflower', 'Zucchini', 'Squash', 'Eggplant', 'Bell Peppers', 'Chili Peppers', 'Okra', 'Asparagus', 
        'Leeks', 'Fennel', 'Chard', 'Rhubarb', 'Green Beans', 'Peas', 'Edamame', 'Sweet Potatoes', 'Potatoes', 
        'Yams', 'Corn', 'Mushrooms', 'Seaweed', 'Algae', 'Cress', 'Bamboo Shoots'
    ],
    'Seafood': [
        'Salmon Fillet', 'Tuna Steak', 'Tuna in Water', 'Mahi Mahi', 'Swordfish', 'Halibut', 'Tilapia', 'Shrimp', 'Lobster', 
        'Crab Legs', 'Scallops', 'Oysters', 'Clams', 'Mussels', 'Anchovies', 'Sardines', 'Squid', 'Octopus', 'Caviar', 
        'Mussels', 'Crayfish', 'Sea Urchin', 'Abalone', 'Fish Roe', 'Tilapia Fillet', 'Cod Fish', 'Snapper', 'Flounder', 
        'Bass', 'Trout', 'Pollock', 'Yellowtail', 'Rainbow Trout', 'Chilean Sea Bass', 'Fish Fingers', 'Kippered Salmon'
    ]
}

# Generate Customers with skewed country distribution
customers = pd.DataFrame({
    'CustomerID': range(1, num_customers + 1),
    'CompanyName': [fake.company() for _ in range(num_customers)],
    'ContactName': [fake.name() for _ in range(num_customers)],
    'Email': [fake.email() for _ in range(num_customers)],
    'Phone': [fake.phone_number() for _ in range(num_customers)],
    'Country': np.random.choice(allowed_countries, size=num_customers, p=country_weights),
    'StreetAddress': [fake.street_address() for _ in range(num_customers)],
    'PostalCode': [fake.zipcode() for _ in range(num_customers)],
    'LastPurchaseDate': [fake.date_between(start_date='-3y', end_date='today') for _ in range(num_customers)],
    'CustomerSince': [fake.date_between(start_date='-10y', end_date='-1y') for _ in range(num_customers)],
    'ActiveStatus': np.random.choice(['Active', 'Inactive'], size=num_customers, p=[0.8, 0.2])
})

# Generate Employees (hire date adjusted for 15 years)
employees = pd.DataFrame({
    'EmployeeID': range(1, num_employees + 1),
    'FirstName': [fake.first_name() for _ in range(num_employees)],
    'LastName': [fake.last_name() for _ in range(num_employees)],
    'Title': np.random.choice(['Sales Manager', 'Sales Representative', 'Account Executive'], num_employees),
    'HireDate': [fake.date_between(start_date='-15y', end_date='today') for _ in range(num_employees)],
    'Department': np.random.choice(['Sales', 'HR', 'Finance', 'IT', 'Marketing'], size=num_employees),
    'Salary': np.random.randint(40000, 120000, size=num_employees)
})

# Generate Suppliers
suppliers = pd.DataFrame({
    'SupplierID': range(1, num_suppliers + 1),
    'CompanyName': [fake.company() for _ in range(num_suppliers)],
    'ContactName': [fake.name() for _ in range(num_suppliers)],
    'Phone': [fake.phone_number() for _ in range(num_suppliers)],
    'StreetAddress': [fake.street_address() for _ in range(num_suppliers)],
    'Country': [fake.country() for _ in range(num_suppliers)]
})

# Generate Products with additional attributes (no stock-related data)
products = []
for i in range(1, num_products + 1):
    category = np.random.choice(list(category_products.keys()))
    product_name = np.random.choice(category_products[category])
    supplier_id = np.random.choice(suppliers['SupplierID'])
    unit_price = np.round(np.random.uniform(5, 100), 2)
    
    # Quantity per unit (randomized formats)
    quantity_formats = ["24-count case", "12-pack", "1-liter bottle", "500ml bottle", "2kg bag", "6-pack", "50-count box"]
    quantity_per_unit = np.random.choice(quantity_formats)
    
    products.append([i, product_name, supplier_id, category, quantity_per_unit, unit_price])

# Convert products list to DataFrame
products = pd.DataFrame(products, columns=['ProductID', 'ProductName', 'SupplierID', 'Category', 
                                           'QuantityPerUnit', 'UnitPrice'])

# Generate Shippers
shippers = pd.DataFrame({
    'ShipperID': range(1, num_shippers + 1),
    'CompanyName': [fake.company() for _ in range(num_shippers)],
    'Phone': [fake.phone_number() for _ in range(num_shippers)]
})

# Generate Orders 
orders = pd.DataFrame({
    'OrderID': range(1, num_orders + 1),  # Primary Key
    'CustomerID': np.random.choice(customers['CustomerID'], num_orders),  # Foreign Key
    'EmployeeID': np.random.choice(employees['EmployeeID'], num_orders),  # Foreign Key
    'OrderDate': [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_orders)],  # Indexed
    'RequiredDate': [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_orders)],  # Nullable
    'ShippedDate': [fake.date_between(start_date='-10y', end_date='today') if np.random.rand() > 0.2 else None for _ in range(num_orders)],  # Nullable
    'ShipVia': np.random.choice(shippers['ShipperID'], num_orders),  # Foreign Key (ShipperID)
    'Freight': np.round(np.random.uniform(5, 500, num_orders), 2),  # Default = 0
    'ShipName': [fake.company() if np.random.rand() > 0.2 else fake.name() for _ in range(num_orders)],  # Nullable
    'ShipAddress': [fake.street_address() for _ in range(num_orders)],  # Nullable
    'ShipCity': [fake.city() for _ in range(num_orders)],  # Nullable
    'ShipRegion': [fake.state() if np.random.rand() > 0.5 else None for _ in range(num_orders)],  # Nullable
    'ShipPostalCode': [fake.zipcode() for _ in range(num_orders)],  # Indexed
    'ShipCountry': [fake.country() for _ in range(num_orders)]  # Nullable
})

# Generate Order Details (same as before)
num_order_details = int(num_orders * 1.5)
order_details = pd.DataFrame({
    'OrderDetailID': range(1, num_order_details + 1),
    'OrderID': np.random.choice(orders['OrderID'], num_order_details),
    'ProductID': np.random.choice(products['ProductID'], num_order_details),
    'Quantity': np.random.randint(1, 10, num_order_details),
    'Discount': np.round(np.random.uniform(0, 0.3), 2)
})

# Generate Payment Information
payment_information = pd.DataFrame({
    'PaymentID': range(1, num_orders + 1),
    'OrderID': np.random.choice(orders['OrderID'], num_orders),
    'PaymentMethod': np.random.choice(['Bank Transfer', 'Pay Pal', 'Credit Card', 'Other Electronic Payment'], num_orders),
    'PaymentAmount': np.round(np.random.uniform(10, 500), 2),
    'PaymentDate': [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_orders)],
    'PaymentStatus': np.random.choice(['Paid', 'Pending', 'Failed'], num_orders)
})

# Generate Inventory Information (consolidated from products)
inventory = pd.DataFrame({
    'ProductID': range(1, num_products + 1),
    'StockQuantity': np.random.randint(0, 500, num_products),  # Replacing 'UnitsInStock'
    'ReorderLevel': np.random.randint(50, 150, num_products),  # Replacing 'ReorderLevel'
    'ReorderQuantity': np.random.randint(50, 200, num_products),
    'LastRestockDate': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_products)],
    'SupplierID': np.random.choice(suppliers['SupplierID'], num_products)  # Linking to suppliers
})

# Generate Shipping Information
shipping_information = pd.DataFrame({
    'ShippingID': range(1, num_orders + 1),
    'OrderID': np.random.choice(orders['OrderID'], num_orders),
    'ShipperID': np.random.choice(shippers['ShipperID'], num_orders),
    'TrackingNumber': [fake.bothify(text='??#####') for _ in range(num_orders)],
    'ShippingStatus': np.random.choice(['In Transit', 'Delivered'], num_orders),
    'DeliveryDate': [fake.date_between(start_date='-1y', end_date='today') for _ in range(num_orders)]
})

# Generate Supplier Performance Data
supplier_performance = pd.DataFrame({
    'SupplierID': suppliers['SupplierID'],
    'OnTimeDeliveryRate': np.round(np.random.uniform(80, 100, len(suppliers)), 2),  # Percentage 80-100%
    'QualityScore': np.round(np.random.uniform(3, 5, len(suppliers)), 2),  # Score 3-5
    'AverageLeadTime': np.random.randint(5, 30, len(suppliers)),  # Days
    'LastEvaluatedDate': [fake.date_between(start_date='-1y', end_date='today') for _ in range(len(suppliers))]
})

# Generate Supplier Contracts Data
supplier_contracts = pd.DataFrame({
    'ContractID': range(1, len(suppliers) + 1),
    'SupplierID': suppliers['SupplierID'],
    'StartDate': [fake.date_between(start_date='-3y', end_date='-1y') for _ in range(len(suppliers))],
    'EndDate': [fake.date_between(start_date='-1y', end_date='+2y') for _ in range(len(suppliers))],
    'ContractTerms': np.random.choice(['Fixed Price', 'Variable Pricing', 'Volume Discount'], len(suppliers))
})

# Generate Shipping Delays Data
num_delays = int(len(shipping_information) * 0.2)  # Assuming 20% of shipments have delays
shipping_delays = pd.DataFrame({
    'DelayID': range(1, num_delays + 1),
    'ShippingID': np.random.choice(shipping_information['ShippingID'], num_delays),
    'Reason': np.random.choice(['Weather', 'Customs', 'Traffic', 'Logistics Issue'], num_delays),
    'DelayDuration': np.random.randint(1, 10, num_delays)  # Delay in days
})

# Generate Route Optimization Data
route_optimization = pd.DataFrame({
    'RouteID': range(1, len(shippers) + 1),
    'ShipperID': shippers['ShipperID'],
    'AvgDeliveryTime': np.round(np.random.uniform(2, 10), 2),  # Avg days to deliver
    'AvgCost': np.round(np.random.uniform(50, 500), 2)  # Cost in USD
})

# Save to CSV
customers.to_csv("customers.csv", index=False)
employees.to_csv("employees.csv", index=False)
suppliers.to_csv("suppliers.csv", index=False)
products.to_csv("products.csv", index=False)
shippers.to_csv("shippers.csv", index=False)
orders.to_csv("orders.csv", index=False)
order_details.to_csv("order_details.csv", index=False)
payment_information.to_csv("payment_information.csv", index=False)
inventory.to_csv("inventory.csv", index=False)
shipping_information.to_csv("shipping_information.csv", index=False)
supplier_performance.to_csv("supplier_performance.csv", index=False)
supplier_contracts.to_csv("supplier_contracts.csv", index=False)
shipping_delays.to_csv("shipping_delays.csv", index=False)
route_optimization.to_csv("route_optimization.csv", index=False)