import tkinter as tk
import requests

def generate():
    res = requests.get("http://127.0.0.1:5000/report")
    result.set(res.text)

app = tk.Tk()
app.title("Admin App")

tk.Button(app, text="Generate Report", command=generate).pack()

result = tk.StringVar()
tk.Label(app, textvariable=result).pack()

app.mainloop()