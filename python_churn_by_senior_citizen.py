import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()
query = """
SELECT senior_citizen, churn
FROM customer_churn;
"""
cursor.execute(query)
results = cursor.fetchall()
senior_churn = 0
senior_no_churn = 0
non_senior_churn = 0
non_senior_no_churn = 0
for row in results:
    senior_citizen = row[0]
    churn = row[1]
    if senior_citizen == 1 and churn == "Yes":
        senior_churn += 1
    elif senior_citizen == 1 and churn == "No":
        senior_no_churn += 1
    elif senior_citizen == 0 and churn == "Yes":
        non_senior_churn += 1
    elif senior_citizen == 0 and churn == "No":
        non_senior_no_churn += 1

print("Churn Analysis by Senior Citizen Status")
print("----------------------------------------")
print("Senior Citizens Churned:", senior_churn)
print("Senior Citizens Non-Churned:", senior_no_churn)
print("Non-Senior Citizens Churned:", non_senior_churn)
print("Non-Senior Citizens Non-Churned:", non_senior_no_churn)

cursor.close()
connection.close()