from flask import Flask, render_template, request, redirect, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "secret123"
# ================= DB =================
def db():
    return sqlite3.connect("campus.db")
def create_users_table():
    conn = db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        password TEXT,
        role TEXT
    )
    """)

    # check first (IMPORTANT)
    cur.execute("SELECT * FROM users")
    if not cur.fetchall():
        cur.execute("INSERT INTO users(email,password,role) VALUES('admin@gmail.com','123','admin')")
        cur.execute("INSERT INTO users(email,password,role) VALUES('teacher@gmail.com','123','teacher')")
        cur.execute("INSERT INTO users(email,password,role) VALUES('student@gmail.com','123','student')")

    conn.commit()
    conn.close()

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

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        course TEXT,
        semester TEXT,
        attendance INTEGER DEFAULT 0,
        fees INTEGER DEFAULT 1
    )
    """)

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

    cur.execute(
        "INSERT INTO students(name,course,semester,attendance,fees) VALUES(?,?,?,?,?)",
        (name,course,semester,80,1)
    )

    conn.commit()
    conn.close()
    return redirect('/students')

@app.route('/delete_student/<int:id>')
def delete_student(id):
    conn=db()
    cur=conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?",(id,))
    conn.commit()
    conn.close()
    return redirect('/students')
# ================= NOTICE =================
@app.route('/notice')
def notice():
    conn = db()
    cur = conn.cursor()

    # table create (safe)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notices(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    )
    """)

    cur.execute("SELECT * FROM notices")
    data = cur.fetchall()

    conn.close()
    return render_template("notice.html", data=data)
@app.route('/add_notice', methods=['POST'])
def add_notice():
    title = request.form['title']
    content = request.form['content']

    conn = db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO notices(title, content) VALUES (?, ?)",
        (title, content)
    )

    conn.commit()
    conn.close()

    return redirect('/notice')
@app.route('/delete_notice/<int:id>')
def delete_notice(id):
    conn = db()
    cur = conn.cursor()
    cur.execute("DELETE FROM notices WHERE id=?", (id,))
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
    msg = request.form['msg'].lower()

    # Smart responses
    if "attendance" in msg:
        return "📊 Your attendance is around 75% 👍 Keep it up!"

    elif "fees" in msg:
        return "💰 Your fees status: Pending ❗ Please pay soon."

    elif "hello" in msg or "hi" in msg:
        return "👋 Hello! I am Smart Campus AI"

    elif "teacher" in msg:
        return "👨‍🏫 Teachers are available from 9AM to 4PM."

    elif "event" in msg:
        return "🎉 Upcoming Event: Hackathon 2026 🚀"

    elif "notice" in msg:
        return "📢 Check notice board for latest updates."

    elif "course" in msg:
        return "📚 Courses available: B.Tech, BCA, MBA"

    elif "bye" in msg:
        return "👋 Goodbye! Have a great day!"

    else:
        return "🤖 I am Smart AI — ask about attendance, fees, events etc."
# ================= RUN =================
create_users_table() 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=True)