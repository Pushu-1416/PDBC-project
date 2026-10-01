import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="customer_churn_project"
    )
    cursor = connection.cursor()

    # Test database connection
    print("1. Database Connection: PASS")

    # Test customer table
    cursor.execute("SELECT COUNT(*) FROM customer_churn")
    total_customers = cursor.fetchone()[0]
    print("2. Customer Table: PASS")
    print("   Total Customers:", total_customers)

    # Test churn data
    cursor.execute("""
    SELECT COUNT(*)
    FROM customer_churn
    WHERE churn = 'Yes'
    """)
    churned_customers = cursor.fetchone()[0]
    print("3. Churn Data: PASS")
    print("   Churned Customers:", churned_customers)

    # Test churn rate
    churn_rate = (churned_customers / total_customers) * 100
    print("4. Churn Rate Calculation: PASS")
    print("   Churn Rate:", round(churn_rate, 2), "%")
    print("\nProject Testing Completed Successfully!")
except mysql.connector.Error as error:
    print("Database Error:", error)
except Exception as error:
    print("Error:", error)
finally:
    try:
        cursor.close()
        connection.close()
    except:
        pass