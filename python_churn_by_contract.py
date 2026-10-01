import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()
query = """
SELECT contract, churn
FROM customer_churn;
"""
cursor.execute(query)
results = cursor.fetchall()
month_to_month_churn = 0
month_to_month_no_churn = 0
one_year_churn = 0
one_year_no_churn = 0
two_year_churn = 0
two_year_no_churn = 0
for row in results:
    contract = row[0]
    churn = row[1]
    if contract == "Month-to-month" and churn == "Yes":
        month_to_month_churn += 1
    elif contract == "Month-to-month" and churn == "No":
        month_to_month_no_churn += 1
    elif contract == "One year" and churn == "Yes":
        one_year_churn += 1
    elif contract == "One year" and churn == "No":
        one_year_no_churn += 1
    elif contract == "Two year" and churn == "Yes":
        two_year_churn += 1
    elif contract == "Two year" and churn == "No":
        two_year_no_churn += 1
print("Churn Analysis by Contract Type")
print("--------------------------------")
print("Month-to-month Churned:", month_to_month_churn)
print("Month-to-month Non-Churned:", month_to_month_no_churn)
print("One year Churned:", one_year_churn)
print("One year Non-Churned:", one_year_no_churn)
print("Two year Churned:", two_year_churn)
print("Two year Non-Churned:", two_year_no_churn)

cursor.close()
connection.close()