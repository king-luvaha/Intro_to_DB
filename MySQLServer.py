import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (adjust credentials as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'  # replace with your actual MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database using IF NOT EXISTS (avoids using SELECT or SHOW)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Could not connect or execute query. {e}")

    finally:
        # Clean up resources
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
