import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()
print("Customer Churn Business Insights")
print("--------------------------------")

# 1. Overall churn
cursor.execute("""
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers
FROM customer_churn;
""")
result = cursor.fetchone()
total_customers = result[0]
churned_customers = result[1]
churn_rate = (churned_customers / total_customers) * 100
print("\n1. Overall Churn")
print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Churn Rate:", round(churn_rate, 2), "%")


# 2. Contract with highest churn
cursor.execute("""
SELECT contract, COUNT(*) AS churn_count
FROM customer_churn
WHERE churn = 'Yes'
GROUP BY contract
ORDER BY churn_count DESC
LIMIT 1;
""")
result = cursor.fetchone()
print("\n2. Contract with Highest Churn")
print("Contract:", result[0])
print("Churned Customers:", result[1])


# 3. Internet service with highest churn
cursor.execute("""
SELECT internet_service, COUNT(*) AS churn_count
FROM customer_churn
WHERE churn = 'Yes'
GROUP BY internet_service
ORDER BY churn_count DESC
LIMIT 1;
""")
result = cursor.fetchone()
print("\n3. Internet Service with Highest Churn")
print("Internet Service:", result[0])
print("Churned Customers:", result[1])


# 4. Payment method with highest churn
cursor.execute("""
SELECT payment_method, COUNT(*) AS churn_count
FROM customer_churn
WHERE churn = 'Yes'
GROUP BY payment_method
ORDER BY churn_count DESC
LIMIT 1;
""")
result = cursor.fetchone()
print("\n4. Payment Method with Highest Churn")
print("Payment Method:", result[0])
print("Churned Customers:", result[1])


# 5. Average monthly charges of churned customers
cursor.execute("""
SELECT AVG(monthly_charges)
FROM customer_churn
WHERE churn = 'Yes';
""")
average_monthly_charges = cursor.fetchone()[0]
print("\n5. Average Monthly Charges of Churned Customers")
print("Average Monthly Charges:",
      round(average_monthly_charges, 2))


cursor.close()
connection.close()