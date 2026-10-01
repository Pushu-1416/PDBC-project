import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()
query = """
SELECT gender, churn
FROM customer_churn;
"""
cursor.execute(query)
results = cursor.fetchall()
female_churn = 0
female_no_churn = 0
male_churn = 0
male_no_churn = 0
for row in results:
    gender = row[0]
    churn = row[1]
    if gender == "Female" and churn == "Yes":
        female_churn += 1
    elif gender == "Female" and churn == "No":
        female_no_churn += 1
    elif gender == "Male" and churn == "Yes":
        male_churn += 1
    elif gender == "Male" and churn == "No":
        male_no_churn += 1

print("Churn Analysis by Gender")
print("------------------------")
print("Female Churned:", female_churn)
print("Female Non-Churned:", female_no_churn)
print("Male Churned:", male_churn)
print("Male Non-Churned:", male_no_churn)

cursor.close()
connection.close()