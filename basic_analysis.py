import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM customer_churn")
result = cursor.fetchone()
print("Total Customers:", result[0])
cursor.close()
connection.close()