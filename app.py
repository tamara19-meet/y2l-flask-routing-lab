from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/shop')
def home():
    return render_template("shop.html")

@app.route('/LIST')
def LIST():
    pets = ["EYELASH GLUE", "EYELEASHES", "TAMARA"] 
    return render_template(
"LIST.html",
pets=pets)

    

if __name__ == '__main__':
   app.run(debug = True)
