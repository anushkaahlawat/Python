import mysql.connector

# Connect Python to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anushkaSQL1906@2026",
    database="sql_iq"
)

print("Connected to MySQL successfully!")

# Create a cursor
mycursor = mydb.cursor()

# Fetch player data
mycursor.execute("SELECT * FROM player")

# Display the results
players = mycursor.fetchall()

for player in players:
    print(player)

# Close the connection
mycursor.close()
mydb.close()