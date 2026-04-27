from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

def db():
    return sqlite3.connect("campus.db")

# HOME
@app.route('/')
def home():
    return redirect('/login')

# LOGIN
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
            session['user'] = email
            session['role'] = user[0]

            if user[0] == 'admin':
                return redirect('/admin')
            elif user[0] == 'teacher':
                return redirect('/teacher')
            else:
                return redirect('/student')

        return "Invalid Login ❌"

    return render_template("login.html")

# ================= ADMIN =================
@app.route('/admin')
def admin():
    if session.get('role') != 'admin':
        return redirect('/login')

    conn = db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students")
    students = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM users WHERE role='teacher'")
    teachers = cur.fetchone()[0]

    cur.execute("SELECT AVG(attendance) FROM students")
    attendance = cur.fetchone()[0] or 0

    conn.close()

    return render_template("admin.html", students=students, teachers=teachers, attendance=attendance)

# ================= TEACHER =================
@app.route('/teacher')
def teacher():
    if session.get('role') != 'teacher':
        return redirect('/login')

    return render_template("teacher.html")

# ================= STUDENT =================
@app.route('/student')
def student():
    if session.get('role') != 'student':
        return redirect('/login')

    return render_template("student.html")

# ================= STUDENT MANAGEMENT =================
@app.route('/students')
def students():
    conn = db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()
    return render_template("students.html", data=data)

@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    course = request.form['course']
    semester = request.form['semester']

    conn = db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students(name,course,semester,attendance) VALUES(?,?,?,0)",
                (name,course,semester))
    conn.commit()
    conn.close()

    return redirect('/students')

# ================= NOTICE =================
@app.route('/notice')
def notice():
    conn = db()
    cur = conn.cursor()
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
    cur.execute("INSERT INTO notices(title,content) VALUES(?,?)",(title,content))
    conn.commit()
    conn.close()

    return redirect('/notice')

# ================= AI FEATURE (DEMO) =================
@app.route('/ai_notice', methods=['POST'])
def ai_notice():
    topic = request.form['topic']
    generated = f"Important Notice: {topic} will be conducted tomorrow. All students must attend."
    return generated

if __name__ == "__main__":
    app.run(debug=True)