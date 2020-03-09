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
    cur = mysql.connection.cursor()
    cur.execute("select * from users ")
    d = cur.fetchall()
    print (d)#jkkkkkkkkkkkkkkkkkkkjkjkkkkkkk
    cur.close()
    return jsonify (d)
@app.route('/api/userdet', methods=['GET', 'POST'])
def userdef():
    return  ('testttt')





@app.route('/api/register', methods=['POST'])
def register():
    fn = request.form.get('fname_r')
    ln = request.form.get('lname_r')
    eml = request.form.get('email_r')
    un = request.form.get('uname_r')
    ph = request.form.get('phone_r')
    ad = request.form.get('address_r')
    pw = request.form.get('psw_r')
    cur = mysql.connection.cursor()
    print('brf')
    cur.execute("insert into users (uname,pword,firstname,lastname,email,address) values (%s,%s,%s,%s,%s,%s)",(un,pw,fn,ln,eml,ad))
    mysql.connection.commit()
    cur.close()
    cur.close()
    print('donr')

    
# @app.route('/products', methods=['GET', 'POST'])
# def products():
#     return  render_template('products.html')

# @app.route('/sign_up', methods=['GET', 'POST'])
# def sign_up():
#      return  render_template('sign_up.html')
# @app.route('/render-user-creation', methods=['GET', 'POST'])
# def renderusercreation():
#     return  render_template('user-creation.html')

@app.route('/api/login', methods=['GET','POST'])
def login():
    print("now reached in flask")#kkkkkkkkkkkkkkkkkkk
    usr = request.form.get('uname')
    psd = request.form.get('psw')
    print (usr, psd)#jokkjjjjjjjjmmmjjjjjjjjjjjjjjjjj
    cur = mysql.connection.cursor()
    cur.execute("select * from users where uname=%s and pword=%s",[usr.strip(),psd.strip()])
    data = cur.fetchall() 
    print (data)#jkkkkkkkkkkkkkkkkkkkjkjkkkkkkk
    cur.close()
    print('sql close')
    print (len(data))

    if len(data) > 0:
        print('if true')
        return ('ok')
        #return render_template('products.html',useridx = data[0][2])
        
    else:
        print ('if false')
        return ('no')
        
        
    
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
