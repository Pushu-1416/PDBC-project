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
    churn,
    COUNT(*) 
FROM customer_churn
GROUP BY internet_service, churn
ORDER BY internet_service, churn;
"""
cursor.execute(query)
results = cursor.fetchall()
print("Churn by Internet Service:")
for row in results:
    print(
        "Internet Service:", row[0],
        "| Churn:", row[1],
        "| Customers:", row[2]
    )
cursor.close()
connection.close()