from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

# DB
def db():
    return sqlite3.connect("campus.db")

# ================= HOME =================
@app.route('/')
def home():
    return render_template("landing.html")

# ================= LOGIN =================
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = db()
        cur = conn.cursor()
        cur.execute("SELECT role FROM users WHERE email=? AND password=?", (email,password))
        user = cur.fetchone()
        conn.close()

        if user:
            session['role'] = user[0]
            if user[0]=='admin':
                return redirect('/admin')
            elif user[0]=='teacher':
                return redirect('/teacher')
            else:
                return redirect('/student')

        return "Invalid Login ❌"

    return render_template("login.html")

# ================= ADMIN =================
@app.route('/admin')
def admin():
    if session.get('role')!='admin':
        return redirect('/login')

    conn = db()
    cur = conn.cursor()

    try:
        cur.execute("SELECT COUNT(*) FROM students")
        students = cur.fetchone()[0]

        cur.execute("SELECT COUNT(*) FROM users WHERE role='teacher'")
        teachers = cur.fetchone()[0]

        cur.execute("SELECT AVG(attendance) FROM students")
        attendance = int(cur.fetchone()[0] or 0)

        cur.execute("SELECT COUNT(*) FROM students WHERE fees=0")
        fees = cur.fetchone()[0]

        cur.execute("SELECT title FROM notices ORDER BY id DESC LIMIT 5")
        notices = cur.fetchall()
    except:
        students=teachers=attendance=fees=0
        notices=[]

    conn.close()

    return render_template("admin.html",
        students=students,
        teachers=teachers,
        attendance=attendance,
        fees=fees,
        notices=notices)

# ================= TEACHER =================
@app.route('/teacher')
def teacher():
    if session.get('role')!='teacher':
        return redirect('/login')
    return render_template("teacher.html")

# ================= STUDENT =================
@app.route('/student')
def student():
    if session.get('role')!='student':
        return redirect('/login')
    return render_template("student.html")

# ================= STUDENTS =================
@app.route('/students')
def students():
    conn=db()
    cur=conn.cursor()
    cur.execute("SELECT * FROM students")
    data=cur.fetchall()
    conn.close()
    return render_template("students.html",data=data)

@app.route('/add_student',methods=['POST'])
def add_student():
    name=request.form['name']
    course=request.form['course']
    semester=request.form['semester']

    conn=db()
    cur=conn.cursor()
    cur.execute("INSERT INTO students(name,course,semester,attendance,fees) VALUES(?,?,?,?,?)",
                (name,course,semester,80,1))
    conn.commit()
    conn.close()
    return redirect('/students')

# ================= EDIT DELETE =================
@app.route('/delete_student/<int:id>')
def delete_student(id):
    conn=db()
    cur=conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?",(id,))
    conn.commit()
    conn.close()
    return redirect('/students')

@app.route('/edit_student/<int:id>',methods=['GET','POST'])
def edit_student(id):
    conn=db()
    cur=conn.cursor()

    if request.method=='POST':
        name=request.form['name']
        cur.execute("UPDATE students SET name=? WHERE id=?",(name,id))
        conn.commit()
        conn.close()
        return redirect('/students')

    cur.execute("SELECT * FROM students WHERE id=?",(id,))
    data=cur.fetchone()
    conn.close()
    return render_template("edit_student.html",data=data)

# ================= NOTICE =================
@app.route('/notice')
def notice():
    conn=db()
    cur=conn.cursor()
    cur.execute("SELECT * FROM notices")
    data=cur.fetchall()
    conn.close()
    return render_template("notice.html",data=data)

@app.route('/add_notice',methods=['POST'])
def add_notice():
    title=request.form['title']
    content=request.form['content']

    conn=db()
    cur=conn.cursor()
    cur.execute("INSERT INTO notices(title,content) VALUES(?,?)",(title,content))
    conn.commit()
    conn.close()
    return redirect('/notice')

# ================= GRAPH =================
@app.route('/attendance_graph')
def attendance_graph():
    conn=db()
    cur=conn.cursor()
    cur.execute("SELECT name,attendance FROM students")
    data=cur.fetchall()
    conn.close()
    return render_template("attendance_graph.html",data=data)

# ================= CHATBOT =================
@app.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

@app.route('/ask',methods=['POST'])
def ask():
    msg=request.form['msg'].lower()

    if "attendance" in msg:
        return "Your attendance is good 👍"
    elif "fees" in msg:
        return "Fees pending check karo"
    elif "hello" in msg:
        return "Hello 👋 I am AI Bot"
    else:
        return "I am Smart AI 🤖"

# ================= RUN =================
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
