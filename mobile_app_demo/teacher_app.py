import tkinter as tk
import requests

def check_risk():
    att = int(entry.get())
    res = requests.post("http://127.0.0.1:5000/risk",
                        json={"attendance": att})
    result.set(res.json()['risk'])

app = tk.Tk()
app.title("Teacher App")

tk.Label(app, text="Enter Attendance %").pack()

entry = tk.Entry(app)
entry.pack()

tk.Button(app, text="Check Risk", command=check_risk).pack()

result = tk.StringVar()
tk.Label(app, textvariable=result).pack()

app.mainloop()