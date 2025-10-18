from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_test_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Faheem@2003",  # 🔁 Change this to your MySQL password
        database="hyundai_test"   # 🔁 Make sure this DB exists
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM test_drive ORDER BY id DESC LIMIT 1")
    data = cursor.fetchone()
    conn.close()
    return data

@app.route('/')
def dashboard():
    test_data = get_test_data()
    return render_template('dashboard.html', data=test_data)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        driver_name = request.form['driver_name']
        vehicle_id = request.form['vehicle_id']
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Faheem@2003",
            database="hyundai_test"
        )
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE test_drive
            SET driver_name = %s, vehicle_id = %s
            WHERE id = (SELECT id FROM test_drive ORDER BY id DESC LIMIT 1)
        """, (driver_name, vehicle_id))
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        data = get_test_data()
        return render_template('edit.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)