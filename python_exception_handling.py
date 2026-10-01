import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="customer_churn_project"
    )
    cursor = connection.cursor()
    query = """
    SELECT COUNT(*)
    FROM customer_churn;
    """
    cursor.execute(query)
    result = cursor.fetchone()
    print("Database connection successful!")
    print("Total Customers:", result[0])
except mysql.connector.Error as error:
    print("Database Error:", error)
except Exception as error:
    print("Error:", error)
finally:
    try:
        cursor.close()
        connection.close()
        print("Database connection closed.")
    except:
        pass