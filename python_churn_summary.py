import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()
#Total Customers
cursor.execute("""
SELECT COUNT(*)
FROM customer_churn;
""")
total_customers = cursor.fetchone()[0]

# Churned customers
cursor.execute("""
SELECT COUNT(*)
FROM customer_churn
WHERE churn = 'Yes';
""")
churned_customers = cursor.fetchone()[0]

# Non-churned customers
cursor.execute("""
SELECT COUNT(*)
FROM customer_churn
WHERE churn = 'No';
""")
non_churned_customers = cursor.fetchone()[0]

# Churn rate
churn_rate = (churned_customers / total_customers) * 100
print("Customer Churn Summary")
print("----------------------")
print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Non-Churned Customers:", non_churned_customers)
print("Churn Rate:", round(churn_rate, 2), "%")

cursor.close()
connection.close()