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
    monthly_charges,
    tenure,
    contract,
    churn
FROM customer_churn
ORDER BY monthly_charges DESC
LIMIT 10;
"""
cursor.execute(query)
results = cursor.fetchall()
print("Top 10 Customers by Monthly Charges:")
for row in results:
    print(
        "Customer ID:", row[0],
        "| Monthly Charges:", row[1],
        "| Tenure:", row[2],
        "| Contract:", row[3],
        "| Churn:", row[4]
    )
cursor.close()
connection.close()