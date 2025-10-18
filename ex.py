import mysql.connector
try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Faheem@2003",
        database="faheem"
    )

    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS worker (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT
        )
    """)

    # Insert data
    sql = "INSERT INTO worker (name, age) VALUES (%s, %s)"
    val = ("Fahem", 22)
    cursor.execute(sql, val)

    # Commit changes
    conn.commit()
    print("Table created and data inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close connection
    if conn.is_connected():
        cursor.close()
        conn.close()
