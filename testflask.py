from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/name")
def hellochakrit():
    return "Hello, Chakrit!"

#webapp
@app.route("/home")
def home():
    return render_template("home.html")
   
if __name__ == "__main__":
    app.run()#host='0.0.0.0' รันบน Vm