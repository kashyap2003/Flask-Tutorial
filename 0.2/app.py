from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
   return "Hello World 2!"

if __name__ == "__main__":
    app.run(debug=True)