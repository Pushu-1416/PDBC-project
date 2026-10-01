import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()
query = """
SELECT internet_service, churn
FROM customer_churn;
"""
cursor.execute(query)
results = cursor.fetchall()
dsl_churn = 0
dsl_no_churn = 0
fiber_churn = 0
fiber_no_churn = 0
no_service_churn = 0
no_service_no_churn = 0
for row in results:
    internet_service = row[0]
    churn = row[1]
    if internet_service == "DSL" and churn == "Yes":
        dsl_churn += 1
    elif internet_service == "DSL" and churn == "No":
        dsl_no_churn += 1
    elif internet_service == "Fiber optic" and churn == "Yes":
        fiber_churn += 1
    elif internet_service == "Fiber optic" and churn == "No":
        fiber_no_churn += 1
    elif internet_service == "No" and churn == "Yes":
        no_service_churn += 1
    elif internet_service == "No" and churn == "No":
        no_service_no_churn += 1

print("Churn Analysis by Internet Service")
print("-----------------------------------")
print("DSL Churned:", dsl_churn)
print("DSL Non-Churned:", dsl_no_churn)
print("Fiber optic Churned:", fiber_churn)
print("Fiber optic Non-Churned:", fiber_no_churn)
print("No Internet Service Churned:", no_service_churn)
print("No Internet Service Non-Churned:", no_service_no_churn)

cursor.close()
connection.close()