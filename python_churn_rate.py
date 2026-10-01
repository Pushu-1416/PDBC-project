import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()
query = """
SELECT churn
FROM customer_churn;
"""
cursor.execute(query)
results = cursor.fetchall()
total_customers = len(results)
churned_customers = 0
for row in results:
    if row[0] == "Yes":
        churned_customers += 1

churn_rate = (churned_customers / total_customers) * 100

print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Churn Rate:", round(churn_rate, 2), "%")

cursor.close()
connection.close()