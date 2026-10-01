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
    payment_method,
    churn,
    COUNT(*) 
FROM customer_churn
GROUP BY payment_method, churn
ORDER BY payment_method, churn;
"""
cursor.execute(query)
results = cursor.fetchall()
print("Churn by Payment Method:")
for row in results:
    print(
        "Payment Method:", row[0],
        "| Churn:", row[1],
        "| Customers:", row[2]
    )
cursor.close()
connection.close()