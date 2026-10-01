import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)

if connection.is_connected():
    print("Connected to MySQL successfully!")

connection.close()