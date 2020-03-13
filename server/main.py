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






@app.route('/api/user', methods=['GET', 'POST'])
def usercall():
    cur = mysql.connection.cursor()
    cur.execute("select * from users where uname='tonydbs'")
    d = cur.fetchall()
    u=d[0][0]
    
    print('usercall')
    print (d[0][2])#jkkkkkkkkkkkkkkkkkkkjkjkkkkkkk
    cur.close()
    return  jsonify (d)
    
################################################
@app.route('/api/reg', methods=['GET', 'POST'])
def reg():
    usr = request.form.get('uname')
    print("reg",usr)
    cur = mysql.connection.cursor()
    cur.execute("select * from users where uname=%s ",[usr])
    data = cur.fetchall()
    print (data [0][2])
    cur.execute("insert into admin (uname,phone,email) values (%s,%s,%s)",[data[0][0],data[0][6],data[0][4]])
    mysql.connection.commit()
    cur.close()
    print('inserted')
################################################
@app.route('/api/admin', methods=['GET', 'POST'])
def adm():
    cur = mysql.connection.cursor()
    cur.execute("select * from admin ")
    d = cur.fetchall()
    print (d)#jkkkkkkkkkkkkkkkkkkkjkjkkkkkkk
    cur.close()
    return jsonify (d)
################################################



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
    cur.execute("select * from users where uname=%s or email=%s",[un,eml])
    data = cur.fetchall()
    print(data)
    print ("here in reg___",len(data))
    if len(data) == 0:
        cur.execute("insert into users (uname,pword,firstname,lastname,email,phone,address) values (%s,%s,%s,%s,%s,%s,%s)",(un,pw,fn,ln,eml,ph,ad))
        mysql.connection.commit()
        cur.close()
        print('inserted')
        return jsonify(data)
    elif len(data) == 1:
        cur.close()    
        print('donr---reg already in table not inserted')
        return 'jsonify(data)'
#####################################################################
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
    print (len(data))##khhhhhhhhhhkkkkhkhk
    if len(data) > 0:
        #print('if true')
        return( jsonify(data))
        #return render_template('products.html',useridx = data[0][2])
    else:
        print ('if false')
        return (jsonify(data))
        

    
# @app.route('/products', methods=['GET', 'POST'])
# def products():
#     return  render_template('products.html')

# @app.route('/sign_up', methods=['GET', 'POST'])
# def sign_up():
#      return  render_template('sign_up.html')
# @app.route('/render-user-creation', methods=['GET', 'POST'])
# def renderusercreation():
#     return  render_template('user-creation.html')

        
    
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
