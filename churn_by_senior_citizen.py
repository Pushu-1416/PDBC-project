import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_MYSQL_PASSWORD",
    database="customer_churn_project"
)

cursor = connection.cursor()

query = """
SELECT
    senior_citizen,
    churn,
    COUNT(*) AS customer_count
FROM customer_churn
GROUP BY senior_citizen, churn
ORDER BY senior_citizen, churn;
"""

cursor.execute(query)

results = cursor.fetchall()

print("Churn by Senior Citizen Status:")

for row in results:
    status = "Senior Citizen" if row[0] == 1 else "Non-Senior Citizen"

    print(
        "Status:", status,
        "| Churn:", row[1],
        "| Customers:", row[2]
    )

cursor.close()
connection.close()