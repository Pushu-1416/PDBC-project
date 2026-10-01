import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()

query = """
SELECT churn, COUNT(*) 
FROM customer_churn
GROUP BY churn;
"""
cursor.execute(query)
results = cursor.fetchall()
print("Customer Churn Distribution:")
for row in results:
    print("Churn:", row[0], "| Customers:", row[1])
cursor.close()
connection.close()