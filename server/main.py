from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from flask import jsonify

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'web_ise'


mysql = MySQL(app)

@app.route('/api/', methods=['GET', 'POST'])
def index():
    return  ('gg')
@app.route('/api/userdet', methods=['GET', 'POST'])
def userdef():
    return  ('testttt')

# @app.route('/products', methods=['GET', 'POST'])
# def products():
#     return  render_template('products.html')

# @app.route('/sign_up', methods=['GET', 'POST'])
# def sign_up():
#      return  render_template('sign_up.html')
# @app.route('/render-user-creation', methods=['GET', 'POST'])
# def renderusercreation():
#     return  render_template('user-creation.html')

@app.route('/login', methods=['POST'])
def login():
    usr = request.form.get('uname')
    psd = request.form.get('psw')
    print (usr, psd)#jokkjjjjjjjjmmmjjjjjjjjjjjjjjjjj
    cur = mysql.connection.cursor()
    cur.execute("select * from users where uname=%s and pword=%s",[usr.strip(),psd.strip()])
    data = cur.fetchall()
    print (data)#jkkkkkkkkkkkkkkkkkkkjkjkkkkkkk
    cur.close()
    if len(data) > 0:
     return render_template('products.html',useridx = data[0][2])
    else:
     return render_template('test1.html')
    
@app.route('/signup', methods=['POST'])
def signup():
    return render_template('sign_up.html')
@app.route('/usercreation',methods=['POST'])
def usercreation():    
    print ("start")
    usr = request.form.get('uname')
    psw = request.form.get('psw')
    email=request.form.get('Email')
    print("c=begore")
    cur = mysql.connection.cursor()
    print("after")
    cur.execute("select * from users where uname=%s or email=%s",[usr,email])
    data = cur.fetchall()
    print(data)
    print ("here")

    if len(data) == 0:
        print("anddddd")
        cur.execute("insert into users (uname,pword,firstname,lastname,email,address) values (%s,%s,%s,%s,%s,%s)",(usr,psw,email,usr,email,psw))
        mysql.connection.commit()
        cur.close()
        print("now")
        return render_template('loginpage.html')
    else:
        cur.close()
        return render_template('test1.html') 
if __name__ == '__main__':
    app.run(debug=True)
