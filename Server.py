from flask import Flask, render_template,redirect,url_for, request
from datetime import datetime,date
import bcrypt
import pywhatkit
import time
import keyboard
import random
import string

def checktime():
    with open("current_session.txt","r") as fp:
        log = fp.read()
    log=log.split("\n")
    if log[2] != "Login":
        time = str(datetime.now())[-12:-10]
        with open('session_history.txt', 'r') as fp:
            lines = fp.readlines()
            print(lines)
            last_d_t = str(lines[-2])
            print(last_d_t)
            last_t = str(last_d_t)[-13:-11]
        return int(last_t) - int(time)
    else:
        return -1
    
def update_current_session():
    with open("current_session.txt","w") as fp:
        fp.write("\n\nLogin")
    return "Updated"

def generate_custom_id():
    timestamp = str(int(time.time()))
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{timestamp}{random_chars}"

UPLOAD_FOLDER = "static"
flag = 0
app = Flask(__name__, static_folder='static', template_folder="templates")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    with open("current_session.txt","r") as fp:
        log = fp.read()
    log=log.split("\n")
    return render_template("index.html",Name = log[0], logout = log[1],Login = log[2])
@app.route("/book",methods=['GET','POST'])
def book():
    if checktime()>20 or checktime()==-1:
        update_current_session()
        return redirect("/login")

    doc_id = request.form.get("doc_id")
    Time = request.form.get("time")
    # print(request.form["time"])

    with open("current_session.txt","r") as fp:
        log = fp.read()
    log=log.split("\n")

    booknum = generate_custom_id()
    number = "+91"+str(log[3])
    doc_name = ""
    Date =date.today()
    day = str(Date.day+1)
    month = str(Date.month)
    year = str(Date.year)
    Date=day+"/"+month+"/"+year
    with open("docdb.txt","r") as fp:
        doc_list = fp.read()
    doc_list=doc_list.split("\n")
    for row in doc_list:
        if row.find(str(doc_id))!=-1:
            doc_name = row.split(",")[1]

    with open("booking_db.txt","a") as fp :
        fp.write(booknum+","+number+","+log[0]+","+doc_id+","+doc_name+","+Date+","+Time+"\n")

    pywhatkit.sendwhatmsg_instantly(number, f"This is a confirmation of your appointment with {doc_name} at clinic on {Date} at {Time}. Your booking number is {booknum}..\n We look forward to seeing you soon!\nHealthycare Kolkata",tab_close=False)
    time.sleep(40)
    keyboard.press_and_release("ctrl+w")

    print("booking sent")

        # flag += 1
    # a = redirect("/doctor")
    return render_template("confirm.html",Name = log[0], logout = log[1], Login = log[2],date=Date,time=Time,name=doc_name)

@app.route("/doctor")
def doctor():
    if checktime()>20:
        update_current_session()
        return redirect("/")
    with open("current_session.txt","r") as fp:
        log = fp.read()
    log = log.split("\n")
    return render_template("doctor.html",Name=log[0],logout = log[1],Login = log[2])
    
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/next", methods = ['GET','POST'])
def next():
    number = request.form['phone']
    password = request.form['password']

    # salt = bcrypt.gensalt()
    # username_hash = bcrypt.hashpw(username.encode('UTF-8'))
    # password_hash = bcrypt.hashpw(password.encode('UTF-8'),salt=salt)

    phones=[]
    passwords = []
    names = []
    emails = []

    with open(r'userdb.txt', 'r') as fp:
        lines = fp.readlines()
        for row in lines:
            row = row.strip()
            phones.append(row.split(",")[0])
            passwords.append(row.split(",")[1])
            names.append(row.split(",")[2])
            emails.append(row.split(",")[3])
    if number in phones and bcrypt.checkpw(password.encode('UTF-8'),passwords[phones.index(number)].encode('UTF-8')):
        with open('current_session.txt', 'w') as fp:
            fp.write(names[phones.index(number)]+"\n"+"Logout"+"\n"+"\n"+number+"\n")
        with open ("session_history.txt",'a') as fp:
            fp.write(number+"\n"+names[phones.index(number)]+"\n"+emails[phones.index(number)]+"\n"+str(datetime.now())+"\n"+"------------------------------------------------------------------------"+"\n")
        return redirect("/doctor",code=302)
    return render_template("login.html",message = "Invalid username or password")

@app.route("/logout")
def logout():
    result = update_current_session()
    print(result)
    with open("current_session.txt","r") as fp:
        log = fp.read()
    log=log.split("\n")
    return render_template("index.html",Name = log[0], logout = log[1], Login = log[2])

@app.route("/doctor169")
def doctor_details169():
    with open("current_session.txt","r") as fp:
        log = fp.read()
    log=log.split("\n")
    return render_template("doctor_details169.html",Name = log[0], logout = log[1], Login = log[2])

@app.route("/doctor22")
def doctor_details22():
    with open("current_session.txt","r") as fp:
        log = fp.read()
    log=log.split("\n")
    return render_template("doctor_details22.html",Name = log[0], logout = log[1], Login = log[2])

@app.route("/doctor14")
def doctor_details14():
    with open("current_session.txt","r") as fp:
        log = fp.read()
    log=log.split("\n")
    return render_template("doctor_details14.html",Name = log[0], logout = log[1], Login = log[2])

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/registration",methods = ['GET','POST'])
def registration():
    fullname = request.form['fullname']
    phone = request.form['phone']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    phones = []

    with open(r'userdb.txt', 'r') as fp:
        lines = fp.readlines()
        for row in lines:
            row = row.strip()
            phones.append(row.split(",")[0])
    if phone not in phones:
        if password == confirm_password:
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode("UTF-8"),salt=salt)
            with open("userdb.txt","a") as fp :
                fp.write(str(phone)+","+str(password_hash.decode('UTF-8'))+","+str(fullname)+","+str(email)+"\n")
            return redirect("/")
        else:
            return render_template("signup.html", match = "Password does not match")
    else:
        return render_template("signup.html", phone = "This Phone Number is already registered")

if __name__ == '__main__':
    print("Starting the Flask application.")
    app.run(host = "0.0.0.0", debug= True, use_reloader=False)