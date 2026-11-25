

print("Name: Rathod Ankitha  \nEnrollment: 92600565030")

import mysql.connector

# Establish connection with MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306
)

# Display success message
if mydb.is_connected():
    print("Database Connected Successfully")

# Close connection
mydb.close()
