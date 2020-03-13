from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from flask import jsonify

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'web_ise'
mysql = MySQL(app)#for the route test
@app.route('/api/', methods=['GET', 'POST'])
def index():
    cur = mysql.connection.cursor()
    cur.execute("select * from users ")
    d = cur.fetchall()
    print (d)
    cur.close()
    return jsonify (d)
@app.route('/api/userdet', methods=['GET', 'POST'])
def userdef():
    return 'ok'
@app.route('/api/user', methods=['GET', 'POST'])
def usercall():
    cur = mysql.connection.cursor()
    cur.execute("select * from users where uname='tonydbs'")
    d = cur.fetchall()
    u=d[0][0]
    print('usercall')
    print (d[0][2])
    cur.close()
    return  jsonify (d)
    
#for trigger call
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
#admin request
@app.route('/api/admin', methods=['GET', 'POST'])
def adm():
    cur = mysql.connection.cursor()
    cur.execute("select * from admin ")
    d = cur.fetchall()
    print (d)
    cur.close()
    return jsonify (d)
#register
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
#login
@app.route('/api/login', methods=['GET','POST'])
def login():
    print("now reached in flask")
    usr = request.form.get('uname')
    psd = request.form.get('psw')
    print (usr, psd)
    cur = mysql.connection.cursor()
    cur.execute("select * from users where uname=%s and pword=%s",[usr.strip(),psd.strip()])
    data = cur.fetchall() 
    print (data)
    cur.close()
    print('sql close')
    print (len(data))#
    if len(data) > 0:
        #print('if true')
        return( jsonify(data))
        #return render_template('products.html',useridx = data[0][2])
    else:
        print ('if false')
        return (jsonify(data))
        
if __name__ == '__main__':
    app.run(debug=True)
