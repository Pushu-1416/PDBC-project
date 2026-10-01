import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="customer_churn_project"
)
cursor = connection.cursor()

query = """
SELECT payment_method, churn
FROM customer_churn;
"""
cursor.execute(query)
results = cursor.fetchall()
electronic_churn = 0
electronic_no_churn = 0
mailed_churn = 0
mailed_no_churn = 0
bank_churn = 0
bank_no_churn = 0
credit_churn = 0
credit_no_churn = 0
for row in results:
    payment_method = row[0]
    churn = row[1]
    if payment_method == "Electronic check" and churn == "Yes":
        electronic_churn += 1
    elif payment_method == "Electronic check" and churn == "No":
        electronic_no_churn += 1
    elif payment_method == "Mailed check" and churn == "Yes":
        mailed_churn += 1
    elif payment_method == "Mailed check" and churn == "No":
        mailed_no_churn += 1
    elif payment_method == "Bank transfer (automatic)" and churn == "Yes":
        bank_churn += 1
    elif payment_method == "Bank transfer (automatic)" and churn == "No":
        bank_no_churn += 1
    elif payment_method == "Credit card (automatic)" and churn == "Yes":
        credit_churn += 1
    elif payment_method == "Credit card (automatic)" and churn == "No":
        credit_no_churn += 1

print("Churn Analysis by Payment Method")
print("---------------------------------")
print("Electronic Check Churned:", electronic_churn)
print("Electronic Check Non-Churned:", electronic_no_churn)
print("Mailed Check Churned:", mailed_churn)
print("Mailed Check Non-Churned:", mailed_no_churn)
print("Bank Transfer Churned:", bank_churn)
print("Bank Transfer Non-Churned:", bank_no_churn)
print("Credit Card Churned:", credit_churn)
print("Credit Card Non-Churned:", credit_no_churn)

cursor.close()
connection.close()