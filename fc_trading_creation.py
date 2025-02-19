import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()
Faker.seed(42)
np.random.seed(42)

# Parameters for dataset size
start_customers = 5000
growth_rate = 0.07  # 7% annual growth for customers
num_customers = int(start_customers * (1 + growth_rate)**10)

start_employees = 100
employee_growth_rate = 0.05  # 5% annual growth for employees
num_employees = int(start_employees * (1 + employee_growth_rate)**10)

start_suppliers = 200
supplier_growth_rate = 0.05  # 5% annual growth for suppliers
num_suppliers = int(start_suppliers * (1 + supplier_growth_rate)**10)

start_products = 800
product_growth_rate = 0.10  # 10% annual growth for products
num_products = int(start_products * (1 + product_growth_rate)**10)

start_orders = int(start_customers * 3)  # Assuming 3 orders per customer at the start
order_growth_rate = 0.10  # 10% annual growth for orders
num_orders = int(start_orders * (1 + order_growth_rate)**10)

num_shippers = 15  # Slight increase over 10 years

start_marketing = 3000
marketing_growth_rate = 0.10  # 10% growth per year for marketing entries
num_marketing_entries = int(start_marketing * (1 + marketing_growth_rate)**10)

# Restrict customers to America and Europe
allowed_countries = ['United States', 'Canada', 'Mexico', 'Panama', 'Brazil', 'Germany', 'France', 'United Kingdom', 'Spain', 'Italy', 'Netherlands', 'Austria', 'Sweden', 'Norway', 'Japan', 'South Korea', 'Australia']

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

# Generate Customers
customers = pd.DataFrame({
    'CustomerID': range(1, num_customers + 1),
    'CompanyName': [fake.company() for _ in range(num_customers)],
    'ContactName': [fake.name() for _ in range(num_customers)],
    'Email': [fake.email() for _ in range(num_customers)],
    'Phone': [fake.phone_number() for _ in range(num_customers)],
    'Country': [np.random.choice(allowed_countries) for _ in range(num_customers)]
})

# Generate Employees (hire date adjusted for 10 years)
employees = pd.DataFrame({
    'EmployeeID': range(1, num_employees + 1),
    'FirstName': [fake.first_name() for _ in range(num_employees)],
    'LastName': [fake.last_name() for _ in range(num_employees)],
    'Title': np.random.choice(['Sales Manager', 'Sales Representative', 'Account Executive'], num_employees),
    'HireDate': [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_employees)]
})

# Generate Suppliers
suppliers = pd.DataFrame({
    'SupplierID': range(1, num_suppliers + 1),
    'CompanyName': [fake.company() for _ in range(num_suppliers)],
    'ContactName': [fake.name() for _ in range(num_suppliers)],
    'Phone': [fake.phone_number() for _ in range(num_suppliers)]
})

# Generate Products (same as before)
products = []
for i in range(1, num_products + 1):
    category = np.random.choice(list(category_products.keys()))
    product_name = np.random.choice(category_products[category])
    products.append([i, product_name, np.random.choice(suppliers['SupplierID']), category, np.round(np.random.uniform(5, 100), 2)])

products = pd.DataFrame(products, columns=['ProductID', 'ProductName', 'SupplierID', 'Category', 'UnitPrice'])

# Generate Shippers
shippers = pd.DataFrame({
    'ShipperID': range(1, num_shippers + 1),
    'CompanyName': [fake.company() for _ in range(num_shippers)],
    'Phone': [fake.phone_number() for _ in range(num_shippers)]
})

# Generate Orders (order date adjusted for 10 years)
orders = pd.DataFrame({
    'OrderID': range(1, num_orders + 1),
    'CustomerID': np.random.choice(customers['CustomerID'], num_orders),
    'EmployeeID': np.random.choice(employees['EmployeeID'], num_orders),
    'OrderDate': [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_orders)],
    'ShipperID': np.random.choice(shippers['ShipperID'], num_orders)
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

# Generate Marketing Data (adjusted for 10 years)
marketing = pd.DataFrame({
    'MarketingID': range(1, num_marketing_entries + 1),
    'CustomerID': np.random.choice(customers['CustomerID'], num_marketing_entries),
    'CampaignName': np.random.choice(['Email Blast', 'Social Media Ads', 'TV Commercials', 'Referral Program'], num_marketing_entries),
    'AdCost': np.round(np.random.uniform(500, 5000), 2),
    'Clicks': np.random.randint(100, 10000, num_marketing_entries),
    'Conversions': np.random.randint(5, 500, num_marketing_entries),
    'CampaignDate': [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_marketing_entries)]
})

# Generate Payment Information
payment_information = pd.DataFrame({
    'PaymentID': range(1, num_orders + 1),
    'OrderID': np.random.choice(orders['OrderID'], num_orders),
    'PaymentMethod': np.random.choice(['Cash', 'Debit Card', 'Credit Card'], num_orders),
    'PaymentAmount': np.round(np.random.uniform(10, 500), 2),
    'PaymentDate': [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_orders)],
    'PaymentStatus': np.random.choice(['Paid', 'Pending', 'Failed'], num_orders)
})

# Generate Inventory Information
inventory = pd.DataFrame({
    'ProductID': range(1, num_products + 1),
    'StockQuantity': np.random.randint(0, 500, num_products),
    'ReorderLevel': np.random.randint(50, 150, num_products),
    'ReorderQuantity': np.random.randint(50, 200, num_products),
    'LastRestockDate': [fake.date_between(start_date='-2y', end_date='today') for _ in range(num_products)],
    'SupplierID': np.random.choice(suppliers['SupplierID'], num_products)
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

# Save to CSV
customers.to_csv("customers.csv", index=False)
employees.to_csv("employees.csv", index=False)
suppliers.to_csv("suppliers.csv", index=False)
products.to_csv("products.csv", index=False)
shippers.to_csv("shippers.csv", index=False)
orders.to_csv("orders.csv", index=False)
order_details.to_csv("order_details.csv", index=False)
marketing.to_csv("marketing.csv", index=False)
payment_information.to_csv("payment_information.csv", index=False)
inventory.to_csv("inventory.csv", index=False)
shipping_information.to_csv("shipping_information.csv", index=False)
