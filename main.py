from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form="""
<!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    backgroud-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                 width: 540px;
                 font: 16px sans-serif;
                 bordere-radius: 10px;
             }
                testarea {
                  margin: 10px 0;
                  width: 540px;
                  height: 120px;
              }
            </style>
        </head>
        <body>
            <form action="/action_page.php" method="POST">
                Rotate By:<input type="text" name="rot" value="0">
                <br>
                <textarea type="text" name="text"></textarea>
                <br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html> """

@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
    rots = int(request.form['rot'])
    msg = request.form['text']
    #e_msg = (rotate_string(msg,rots))
    return rotate_string(msg,rots)
app.run()