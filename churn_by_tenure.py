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
    CASE
        WHEN tenure <= 12 THEN '0-12 Months'
        WHEN tenure <= 24 THEN '13-24 Months'
        WHEN tenure <= 48 THEN '25-48 Months'
        ELSE '49+ Months'
    END AS tenure_group,
    churn,
    COUNT(*) 
FROM customer_churn
GROUP BY tenure_group, churn
ORDER BY tenure_group, churn;
"""
cursor.execute(query)
results = cursor.fetchall()
print("Churn by Tenure Group:")
for row in results:
    print(
        "Tenure:", row[0],
        "| Churn:", row[1],
        "| Customers:", row[2]
    )
cursor.close()
connection.close()