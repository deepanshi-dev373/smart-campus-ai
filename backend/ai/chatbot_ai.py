def chatbot_reply(msg):
    if "hello" in msg.lower():
        return "Hello 👋"
    return "Ask campus related question"