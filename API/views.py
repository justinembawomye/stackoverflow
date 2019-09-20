from flask import Flask

app= Flask (__name__)



@app.route("/")
def stackoverflow():
    return "Welcome to StackOverflow Lite application."
    
