from flask import Flask

app = Flask(__name__)

@app.route('/home/name/<string:name>/id/<int:id>')
def hello(name, id):
   return "Hello, " + name + "\nYour Id is " +str(id)
 
if __name__ == "__main__":
    app.run(debug=True)