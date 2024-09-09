from flask import Flask, request, jsonify, render_template
import pyodbc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# SQL Server configuration
server = 'localhost'
database = 'Python_Flask_Crud_db'
username = 'sa'
password = 'aitisam24'

app.config['SQL_SERVER'] = {
    'driver': '{ODBC Driver 17 for SQL Server}',
    'server': server,
    'database': database,
    'username': username,
    'password': password
}

def get_db_connection():
    conn_str = (
        f"DRIVER={app.config['SQL_SERVER']['driver']};"
        f"SERVER={app.config['SQL_SERVER']['server']};"
        f"DATABASE={app.config['SQL_SERVER']['database']};"
        f"UID={app.config['SQL_SERVER']['username']};"
        f"PWD={app.config['SQL_SERVER']['password']};"
    )
    return pyodbc.connect(conn_str)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accept', methods=['POST'])
def submit_nurse():
    data = request.json

    # Validate data
    if not all(key in data for key in ('name', 'age', 'gender')):
        return jsonify({"error": "Missing required fields"}), 400

    id = data.get('id')
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        if id:
            cursor.execute("UPDATE nurse SET name = ?, age = ?, gender = ? WHERE id = ?", (name, age, gender, id))
        else:
            cursor.execute("INSERT INTO nurse (name, age, gender) VALUES (?, ?, ?)", (name, age, gender))
        conn.commit()
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "Nurse added/updated successfully"}), 201

@app.route('/patient', methods=['POST'])
def submit_patient():
    data = request.json

    # Validate data
    if not all(key in data for key in ('name', 'age', 'gender', 'nurse_id')):
        return jsonify({"error": "Missing required fields"}), 400

    id = data.get('id')
    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    nurse_id = data.get('nurse_id')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        if id:
            cursor.execute("UPDATE patient SET name = ?, age = ?, gender = ?, nurse_id = ? WHERE id = ?", (name, age, gender, nurse_id, id))
        else:
            cursor.execute("INSERT INTO patient (name, age, gender, nurse_id) VALUES (?, ?, ?, ?)", (name, age, gender, nurse_id))
        conn.commit()
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "Patient added/updated successfully"}), 201

@app.route('/nurses', methods=['GET'])
def get_nurses():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, gender FROM nurse")
        rows = cursor.fetchall()
        nurses = [{"id": row[0], "name": row[1], "age": row[2], "gender": row[3]} for row in rows]
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify(nurses)

@app.route('/patients', methods=['GET'])
def get_patients():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, gender, nurse_id FROM patient")
        rows = cursor.fetchall()
        patients = [{"id": row[0], "name": row[1], "age": row[2], "gender": row[3], "nurse_id": row[4]} for row in rows]
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify(patients)

@app.route('/nurse/<int:id>', methods=['PUT'])
def update_nurse(id):
    data = request.json

    # Validate data
    if not all(key in data for key in ('name', 'age', 'gender')):
        return jsonify({"error": "Missing required fields"}), 400

    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE nurse SET name = ?, age = ?, gender = ? WHERE id = ?", (name, age, gender, id))
        conn.commit()
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "Nurse updated successfully"}), 200

@app.route('/patient/<int:id>', methods=['PUT'])
def update_patient(id):
    data = request.json

    # Validate data
    if not all(key in data for key in ('name', 'age', 'gender', 'nurse_id')):
        return jsonify({"error": "Missing required fields"}), 400

    name = data.get('name')
    age = data.get('age')
    gender = data.get('gender')
    nurse_id = data.get('nurse_id')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE patient SET name = ?, age = ?, gender = ?, nurse_id = ? WHERE id = ?", (name, age, gender, nurse_id, id))
        conn.commit()
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "Patient updated successfully"}), 200

@app.route('/nurse/<int:id>', methods=['DELETE'])
def delete_nurse(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM nurse WHERE id = ?", (id,))
        conn.commit()
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "Nurse deleted successfully"}), 200

@app.route('/patient/<int:id>', methods=['DELETE'])
def delete_patient(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM patient WHERE id = ?", (id,))
        conn.commit()
    except pyodbc.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "Patient deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
