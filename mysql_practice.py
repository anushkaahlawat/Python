import mysql.connector

# MySQL password
pw = "anushkaSQL1906@2026"

# Connect to MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=pw
)

print("MySQL connection successful!")

# Create a cursor
cursor = connection.cursor()

# Create a database
cursor.execute("CREATE DATABASE IF NOT EXISTS mysql_python")

# Select the database
cursor.execute("USE mysql_python")

# Create the orders table
create_orders_table = """
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    product_name VARCHAR(20) NOT NULL,
    date_ordered DATE,
    quantity INT,
    unit_price FLOAT,
    phone_number VARCHAR(20)
)
"""

# Execute the SQL query
cursor.execute(create_orders_table)

print("Orders table created successfully!")


# Insert data into the orders table
data_orders = """
INSERT INTO orders
(order_id, customer_name, product_name, date_ordered,
 quantity, unit_price, phone_number)
VALUES
(101, 'Steve', 'Laptop', '2018-06-12', 2, 800, '6293730802'),
(102, 'Jos', 'Books', '2019-02-10', 10, 12, '8367489124'),
(103, 'Stacy', 'Trousers', '2019-12-25', 5, 50, '8976123645'),
(104, 'Nancy', 'T-Shirts', '2018-07-14', 7, 30, '7368145099'),
(105, 'Maria', 'Headphones', '2019-05-30', 6, 48, '8865316698'),
(106, 'Danny', 'Smart TV', '2018-08-20', 10, 300, '7720130449')
"""

# Display orders where unit_price is greater than 100
'''cursor.execute("SELECT * FROM orders WHERE unit_price > 100")'''


# Display only customer names and phone numbers
cursor.execute("SELECT customer_name, phone_number FROM orders")
for customer in cursor.fetchall(): print(customer)


'''for order in cursor.fetchall():
    print(order)'''


# Close the connection
cursor.close()
connection.close()















