from flask import Flask
## WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome Ram is here CLick here"


@app.route("/members")
def members():
    return "Welcome Ram is here CLick here please"

if __name__=="__main__":
    app.run(debug=True)
