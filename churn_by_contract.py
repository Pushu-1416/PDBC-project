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
    contract,
    churn,
    COUNT(*) 
FROM customer_churn
GROUP BY contract, churn
ORDER BY contract, churn;
"""
cursor.execute(query)
results = cursor.fetchall()
print("Churn by Contract Type:")
for row in results:
    print(
        "Contract:", row[0],
        "| Churn:", row[1],
        "| Customers:", row[2]
    )
cursor.close()
connection.close()