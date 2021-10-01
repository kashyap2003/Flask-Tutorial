from flask import Flask

app = Flask(__name__)

@app.route('/home/name/<string:name>/id/<int:id>')
def hello(name, id):
   return "Hello, " + name + "\nYour Id is " +str(id)

@app.route('/onlyget', methods=['GET', 'POST'])
def get_req():
   return '<h1> You can only get this webpage </h1>.'
 
if __name__ == "__main__":
    app.run(debug=True)