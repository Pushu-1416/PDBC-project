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
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        (SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*)) * 100,
        2
    ) AS churn_rate
FROM customer_churn;
"""
cursor.execute(query)
result = cursor.fetchone()
print("Total Customers:", result[0])
print("Churned Customers:", result[1])
print("Churn Rate:", result[2], "%")
cursor.close()
connection.close()