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
        WHEN monthly_charges < 30 THEN 'Low Charges'
        WHEN monthly_charges < 70 THEN 'Medium Charges'
        ELSE 'High Charges'
    END AS charge_group,
    churn,
    COUNT(*) 
FROM customer_churn
GROUP BY charge_group, churn
ORDER BY charge_group, churn;
"""
cursor.execute(query)
results = cursor.fetchall()
print("Churn by Monthly Charges:")
for row in results:
    print(
        "Charge Group:", row[0],
        "| Churn:", row[1],
        "| Customers:", row[2]
    )
cursor.close()
connection.close()