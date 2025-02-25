# FC-Trading-Database
Creation of a Synthetic Database for Querying and Data Science Applications.

![image](https://github.com/user-attachments/assets/a445c6d2-0898-4ea2-96b1-7132c1d9f0d3)

The goal is to create a comprehensive, synthetic database for FC Trading, a fictional international foods company that imports and exports a variety of food products. This database should serve as a versatile tool for querying, data analysis, and modeling, making it suitable for various data science projects.

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


# Question 2
Which 10 countries generated the highest revenue?

# Question 3
Revenue in 2024 per product category
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

# Question 5
What was the average revenue growth from 2015 to 2024?
