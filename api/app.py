from flask import Flask, jsonify , request, make_response, session, redirect, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
# from flask_mysqldb import MySQL

app = Flask(__name__)


#secret key for session
app.secret_key = "secretkey"

# app.config['MYSQL_HOST'] = '127.0.0.1'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'MyP@ssw0rd123'
# app.config['MYSQL_DB'] = 'data'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:MyP%40ssw0rd123@localhost/data'


db = SQLAlchemy(app)



CORS(app)




    
@app.route('/setCookie', methods=['POST'])
def setCookie():
    data = request.json
    res = make_response( "<h1> Cookie set successfully!")
    res.set_cookie('email', data['email'])
    return res

@app.route('/getCookie',methods=['GET'])
def getCookie():
    data = request.cookies.get('email')
    return f"<h1>Your Email {data}"




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
    
    
  
   

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'email' in session:
        return redirect(url_for('home'))



@app.route('/login', methods= ['POST'])
def login():
    
    data = request.json
    
    #set session
    
    
  
       
    if(data['email'] != '' and data['password']!= ''):
      
        query = f"select * from register_users where user_email = '{data['email']}' and user_password = '{data['password']}'"
        result = db.session.execute(text(query))
        result = [dict(row._mapping) for row in result]
        import pdb; pdb.set_trace()
        
        session['email'] = data['email']
        session['password'] = data['password']
        
    
        return jsonify({
            "ok" : True,
            "msg" : result
        })
    else:
        return jsonify({
            "ok" : False,
            "msg" : "Enter Valid Credentials !"
        })
    
    


@app.route("/get_authenticated_user_information")
def get_authenticated_user_information():
    if "email" in session:
        
        arg = session['email']
        
        query = f"select *from register_users where user_email = '{arg}'"
        result = db.session.execute(text(query))
        
        result = [dict(row._mapping) for row in result]
        
        temp_dict=dict()
        temp_dict['email'] = result['user_email']
        temp_dict['username'] = result['user_username']
        temp_dict['password'] = result['user_password']
        
        return jsonify(ok=True, data = temp_dict)
    else:
       return jsonify(ok=False, error="No such user or incorrect password") 
        
        
   
  
    

@app.route('/home', methods= ['GET', 'POST'])
def home():

    return "<h1> Welcome to home"

app.run(debug=True)