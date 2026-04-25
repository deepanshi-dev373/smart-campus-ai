import cv2
import sqlite3
import datetime

def connect():
    return sqlite3.connect("campus.db")

def mark(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO attendance(username,date) VALUES (?,?)",
                (name, str(datetime.datetime.now())))
    conn.commit()
    conn.close()

def start_camera():
    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()
        mark("student")
        cv2.imshow("AI Attendance", frame)

        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()