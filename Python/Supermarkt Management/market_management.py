import pandas as pd

# Read products and employees data from CSV files
products = pd.read_csv("products.csv", sep=";")
employees = pd.read_csv("supermarketemployees.csv", sep=";")

# Create DataFrames for products and employees
products = pd.DataFrame(products)
employees = pd.DataFrame(employees)

# Reorder the columns in the DataFrames
products = products.reindex(columns=["Name", "Prod_id", "Category", "PRICE", "SAP ID #1", "SAP ID #22"])
employees = employees.reindex(columns=["Name", "Age", "Pers_id", "JOB_ID"])

# Create lists of employees and products data
employees_list = []
for index, row in employees.iterrows():
    x = row["Name"], row["Age"], row["Pers_id"], row["JOB_ID"]
    employees_list.append(x)

products_list = []
for index, row in products.iterrows():
    x = row["Name"], row["Prod_id"], row["Category"], row["PRICE"]
    products_list.append(x)

from supermarket import *

# Create a Supermarket object
my_supermarket = Supermarket("Supermarkt Deluxe", "Marienplatz 1", "München")

# Create Product and Employee objects from the data lists
my_supermarket.products = [Product(*item) for item in products_list]
my_supermarket.employees = [Employee(*item) for item in employees_list]

# Interact with an employee
my_supermarket.employees[1].greet_customer()
my_supermarket.employees[1].celebrate_birthday()

# Print the number of employees in the supermarket
print(f'The supermarket has {len(my_supermarket.employees)} employees.')

# Function to get the most expensive product
def get_most_expensive_product(prod_list):
    """Returns one Product object with the highest price."""
    max_price = None
    max_prod_position = ""
    for i, prod in enumerate(prod_list):
        if not max_price or max_price <= prod.price:
            max_price = prod.price
            max_prod_position = i
    return prod_list[max_prod_position]

most_expensive_product = get_most_expensive_product(my_supermarket.products)
print(f'The most expensive product in the supermarket is: {most_expensive_product.name} for {most_expensive_product.price} €.')

# Calculate the average product price
average_price = products.PRICE.mean()
print(f'The average product price is: {round(average_price, 2)} €.')

from collections import Counter

# Count the number of products in each category
category_counter = Counter([prod.category for prod in my_supermarket.products])
print(f'The supermarket has the following range of categories: {category_counter}.')

# Function to get the oldest employee
def get_oldest_employee(employee_list):
    """Returns the oldest employee."""
    max_age = None
    max_age_position = ""
    for i, employee in enumerate(employee_list):
        if not max_age or max_age <= employee.age:
            max_age = employee.age
            max_age_position = i
    return employee_list[max_age_position]

oldest_employee = get_oldest_employee(my_supermarket.employees)
print(f'The oldest employee in the supermarket is: {oldest_employee.name}.')