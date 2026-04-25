def chatbot_reply(msg):
    msg = msg.lower()

    if "attendance" in msg:
        return "Your attendance is good 👍"
    elif "hello" in msg:
        return "Hello student!"
    else:
        return "Ask something about campus."