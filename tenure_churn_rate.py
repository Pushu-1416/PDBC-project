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
    COUNT(*),
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        (SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*)) * 100,
        2
    ) AS churn_rate
FROM customer_churn
GROUP BY tenure_group
ORDER BY churn_rate DESC;
"""

cursor.execute(query)

results = cursor.fetchall()

print("Churn Rate by Tenure Group:")
print()

for row in results:
    print(
        "Tenure:", row[0],
        "| Total Customers:", row[1],
        "| Churned:", row[2],
        "| Churn Rate:", row[3], "%"
    )

cursor.close()
connection.close()