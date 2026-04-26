def chatbot_reply(msg):
    if "hello" in msg.lower():
        return "Hello student 👋"
    return "Ask something about campus"