from flask import Flask

app = Flask(__name__)

@app.route('/home/<int:id>')
def hello(id):
   return "Hello there you ID is " + str(id) # We add here str because id is an interger

if __name__ == "__main__":
    app.run(debug=True)