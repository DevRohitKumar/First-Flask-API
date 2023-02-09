from simple_flask_api import app, mysql
from flask import jsonify, request

@app.route('/api/users', methods=['GET'])
def fetch_all_users():
    try:
        con_cur = mysql.connection.cursor()
        con_cur.execute("SELECT * FROM users")
        result = con_cur.fetchall()
        if result:
            return jsonify({"data": result}), 200
        else:
            return jsonify({"message": "No data found"}), 404
    except Exception as e:
        print(e)
    finally:
        con_cur.close()
        

@app.route('/api/user/<int:id>', methods=['GET'])
def fetch_single_user(id):
    try:
        con_cur = mysql.connection.cursor()
        con_cur.execute("SELECT * FROM users WHERE id = {}".format(id))
        result = con_cur.fetchone()
        if result:
            return jsonify({"data": result}), 200
        else:
            return jsonify({"error": "No related data found ☹️"}), 404
    except Exception as e:
        print(e)
    finally:
        con_cur.close()      
        

@app.route('/api/create', methods=['POST'])
def create_user():
    try:        
        if request.is_json and request.method == 'POST':           
            data = request.get_json()
            
            fname = data['first_name']
            lname = data['last_name']
            gender = data['gender']
            email = data['email']
            phone = data['phone']
            country_code = data['country_code']
            
            if fname and lname and email and gender and phone and country_code:
                
                conn_cursor = mysql.connection.cursor()
                conn_cursor.execute("""INSERT INTO users (
                    fname, lname, gender, email, phone_number, phone_country_code)
                    VALUES (%s, %s,%s,%s,%s,%s)""", (fname, lname, gender, email, phone, country_code))
                mysql.connection.commit()
                conn_cursor.close()
                
                return jsonify({"message": "User created successfully 🥳 "}), 201              
                
            else:
                return jsonify({"error": "Some data is missing 🙁 "}), 206
              
        else:
            return jsonify({"error": "Request body must be JSON ☠️ "}), 400
        
    except Exception as e:
        return jsonify({"error": "Something went wrong ☠️ "}), 400
        print(e)