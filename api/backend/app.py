from flask import Flask, jsonify , request
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)




app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'MyP@ssw0rd123'
app.config['MYSQL_DB'] = 'data'

mysql = MySQL(app)



CORS(app)





@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if(data['username'] != '' and data['email'] != '' and data['password']!= ''):
        
        connection = mysql.connection.cursor()
        sql ="insert into register_users(user_name ,user_email,user_password ) values (%s, %s,%s)"
        values = (data['username'] , data['email'], data['password'])
        connection.execute(sql,values)
        mysql.connection.commit()
        connection.close()
        
        return jsonify({
            "ok" : True,
            "msg" : "Register Successfully!"
        })
    else:
        return jsonify({
            "ok" : False,
            "msg" : "Enter Valid Credentials !"
        })
    
    
  
   





@app.route('/login', methods= ['POST'])
def login():
    data = request.json
    if(data['email'] != '' and data['password']!= ''):
        connection = mysql.connection.cursor()
        sql = "select user_email from register_users where user_email = %s and user_password= %s"
        
        res = connection.execute(sql, [data['email'],data['password']])
        mysql.connection.commit()
        connection.close()
    
    
        return jsonify({
            "ok" : True,
            "msg" : res
        })
    else:
        return jsonify({
            "ok" : False,
            "msg" : "Enter Valid Credentials !"
        })
    
    
    
    

@app.route('/home', methods= ['GET', 'POST'])
def home():
    return "<h1> Welcome to home"

app.run(debug=True)