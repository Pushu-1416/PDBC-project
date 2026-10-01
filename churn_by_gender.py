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
    gender,
    churn,
    COUNT(*) 
FROM customer_churn
GROUP BY gender, churn
ORDER BY gender, churn;
"""
cursor.execute(query)
results = cursor.fetchall()
print("Churn by Gender:")
for row in results:
    print(
        "Gender:", row[0],
        "| Churn:", row[1],
        "| Customers:", row[2]
    )
cursor.close()
connection.close()