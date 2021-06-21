## Jinja 2 template 
'''
With the help of jinja 2 Template we can add the following things to html page
{% for %}
{% if %}
{% while %}
{% else %}
{% elif %}

{{ to put the vale dynamically }}

{{# Comments #}}
'''

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)


@app.route("/")
def Welcome():
    return render_template("index.html")
    

@app.route("/success/<int:scores>")  
def success(scores):
    res=""
    if scores>=50:
        res="SUCCESS"
    else:
        res="FAIL" 
    exp={"scores":scores,"result":res}       
    return render_template("result.html",result=exp)

@app.route("/fail/<int:scores>")    
def fail(scores):
    return "The student has failed the exam by  "+str(scores)

@app.route("/submit",methods=["POST","GET"])  
def submit():
    
    total=0
    if request.method=="POST":
        science=float(request.form["science"])
        maths=float(request.form["maths"])
        c=float(request.form["c"])
        ds=float(request.form["datascience"])
        total=float(science+maths+c+ds)/4
    
    return redirect(url_for("success",scores=total))   
     


if __name__=="__main__":
    app.run(debug=True)        