import tkinter as tk
import requests

def send():
    msg = entry.get()
    res = requests.post("http://127.0.0.1:5000/chat",
                        json={"message": msg})
    reply.set(res.json()['reply'])

app = tk.Tk()
app.title("Student App")
app.geometry("300x200")

tk.Label(app, text="AI Chatbot").pack()

entry = tk.Entry(app)
entry.pack()

tk.Button(app, text="Send", command=send).pack()

reply = tk.StringVar()
tk.Label(app, textvariable=reply).pack()

app.mainloop()