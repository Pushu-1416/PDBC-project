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
    churn
FROM customer_churn
ORDER BY total_charges DESC
LIMIT 10;
"""
cursor.execute(query)
results = cursor.fetchall()
print("Top 10 Customers by Total Charges:")
for row in results:
    print(
        "Customer ID:", row[0],
        "| Tenure:", row[1],
        "| Monthly Charges:", row[2],
        "| Total Charges:", row[3],
        "| Churn:", row[4]
    )
cursor.close()
connection.close()