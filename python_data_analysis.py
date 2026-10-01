import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()
query = """
SELECT
    customer_id,
    tenure,
    monthly_charges,
    total_charges,
    contract,
    internet_service,
    payment_method,
    churn
FROM customer_churn;
"""
cursor.execute(query)
results = cursor.fetchall()
print("Customer Churn Data")
print("-------------------")
for row in results[:10]:
    print(row)
print()
print("Total Records Retrieved:", len(results))
cursor.close()
connection.close()