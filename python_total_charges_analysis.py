import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()
query = """
SELECT churn, total_charges
FROM customer_churn;
"""
cursor.execute(query)
results = cursor.fetchall()
churned_total = 0
churned_count = 0
non_churned_total = 0
non_churned_count = 0
for row in results:
    churn = row[0]
    total_charges = row[1]
    if churn == "Yes":
        churned_total += total_charges
        churned_count += 1
    elif churn == "No":
        non_churned_total += total_charges
        non_churned_count += 1
churned_average = churned_total / churned_count
non_churned_average = non_churned_total / non_churned_count
print("Total Charges Analysis")
print("----------------------")
print("Average Total Charges - Churned Customers:",
      round(churned_average, 2))
print("Average Total Charges - Non-Churned Customers:",
      round(non_churned_average, 2))

cursor.close()
connection.close()