import pymysql

from flask import Flask, jsonify, request
import pymysql
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

@app.route('/users', methods=['GET'])
def get_users():
    # To connect MySQL database
    conn = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6467886', password = 'DP6z6mBZQj', db='sql6467886')

    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    output = cur.fetchall()

    #print(type(output)); #this will print tuple

    #for rec in output:
       # print(rec);

    # To close the connection
    conn.close()

    return jsonify(output);



@app.route('/users', methods=['POST'])
def insertRecord():
  conn = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6467886', password = 'DP6z6mBZQj', db='sql6467886')
  raw_json = request.get_json();
  name= raw_json["name"];
  age= int(raw_json["age"]);
  city = raw_json["city"];
  cur= conn.cursor();
  cur.execute(f"INSERT INTO users (id,name,age,city) VALUES (NULL,'{name}','{age}','{city}')");
  conn.commit();
  return {"result" : "Record inserted Succesfully"}

@app.route('/users', methods=['PUT'])
def updateRecord():
    conn = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6467886', password = 'DP6z6mBZQj', db='sql6467886')

    raw_json = request.get_json();
    id = int(request.args.get('id'))
    raw_json = request.get_json();
    name= raw_json["name"];
    age= int(raw_json["age"]);
    city = raw_json["city"];
    cur = conn.cursor()
    cur.execute(f"UPDATE users SET name = '{name}',age='{age}',city='{city}' WHERE id = '{id}'");
    conn.commit()
    return {"result" : "Record updated Succesfully"}

@app.route('/users', methods=['DELETE'])
def deleteRecord():
    # To connect MySQL database
    conn = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6467886', password = 'DP6z6mBZQj', db='sql6467886')
    cur = conn.cursor()
    id = int(request.args.get('id'));
    res = cur.execute(f"Delete from users WHERE id ={id}");
    conn.commit();
    print(cur.rowcount,"record(s) deleted");

    return {"result" : "Record deleted Succesfully"}

@app.route('/users/id', methods=['GET'])
def read():
    # To connect MySQL database
     conn = pymysql.connect(host='sql6.freesqldatabase.com', user='sql6467886', password = 'DP6z6mBZQj', db='sql6467886')
     cur = conn.cursor()
     id = int(request.args.get('id'))
     cur.execute(f"select * from users WHERE id = {id}");

     output = cur.fetchall()

     print(type(output)); #this will print tuple

     for rec in output:
        print(rec);

    # To close the connection
     conn.close()

     return jsonify(output);



if __name__ == "__main__":
    app.run(debug=True);