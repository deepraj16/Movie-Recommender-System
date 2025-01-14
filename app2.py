from flask import Flask 

app=Flask(__name__)

@app.route("/home/<int:t>")
def home(t): 
    return t

if "__main__"==__name__ : 
    app.run(debug=True)