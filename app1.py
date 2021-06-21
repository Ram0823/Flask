## Building url dynamically in Flask
### Variable Rules and URL Building
from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route("/")
def Welcome():
    return"Welcome to Ram's Youtube Channel"


@app.route("/success/<int:scores>")
def Success(scores):
    return "The person has passed the exam by "+str(scores)


@app.route("/fail/<int:scores>")
def fail(scores):
    return "The person has failed the exam by "+str(scores)    


@app.route("/results/<int:marks>")
def result(marks):
    results=""
    if marks<50:
        results="fail"
    else:
        results="success"    
    return redirect(url_for(results,scores=marks))
     

if __name__=="__main__":
    app.run(debug=True)


