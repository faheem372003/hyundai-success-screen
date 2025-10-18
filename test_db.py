import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Faheem@2003",  # 🔁 Use your actual password
        database="hyundai_test"
    )
    print("✅ Connected to MySQL successfully!")
    conn.close()
except mysql.connector.Error as err:
    print("❌ Error:", err)
    return None