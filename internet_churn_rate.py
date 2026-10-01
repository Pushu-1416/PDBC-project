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
    internet_service,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        (SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*)) * 100,
        2
    ) AS churn_rate
FROM customer_churn
GROUP BY internet_service
ORDER BY churn_rate DESC;
"""
cursor.execute(query)
results = cursor.fetchall()
print("Churn Rate by Internet Service:")
print()
for row in results:
    print(
        "Internet Service:", row[0],
        "| Total Customers:", row[1],
        "| Churned:", row[2],
        "| Churn Rate:", row[3], "%"
    )
cursor.close()
connection.close()