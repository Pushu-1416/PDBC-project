import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()
query = """
SELECT tenure, churn
FROM customer_churn;
"""
cursor.execute(query)
results = cursor.fetchall()
short_tenure_churn = 0
short_tenure_no_churn = 0
medium_tenure_churn = 0
medium_tenure_no_churn = 0
long_tenure_churn = 0
long_tenure_no_churn = 0
for row in results:
    tenure = row[0]
    churn = row[1]
    if tenure <= 12 and churn == "Yes":
        short_tenure_churn += 1
    elif tenure <= 12 and churn == "No":
        short_tenure_no_churn += 1
    elif tenure <= 36 and churn == "Yes":
        medium_tenure_churn += 1
    elif tenure <= 36 and churn == "No":
        medium_tenure_no_churn += 1
    elif tenure > 36 and churn == "Yes":
        long_tenure_churn += 1
    elif tenure > 36 and churn == "No":
        long_tenure_no_churn += 1

print("Churn Analysis by Tenure")
print("------------------------")
print("Short Tenure (0-12 months) Churned:", short_tenure_churn)
print("Short Tenure (0-12 months) Non-Churned:", short_tenure_no_churn)
print("Medium Tenure (13-36 months) Churned:", medium_tenure_churn)
print("Medium Tenure (13-36 months) Non-Churned:", medium_tenure_no_churn)
print("Long Tenure (37+ months) Churned:", long_tenure_churn)
print("Long Tenure (37+ months) Non-Churned:", long_tenure_no_churn)

cursor.close()
connection.close()