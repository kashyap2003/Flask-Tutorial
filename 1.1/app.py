from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
   {
      'title': 'Post 1',
      'content': 'This is the content of post 1.'
   },
   {
      'title': 'Post 2',
      'content': 'This is the content of post 2.'
   }
]

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/posts')
def posts():
   return render_template('posts.html', posts=all_posts)

@app.route('/home/name/<string:name>/id/<int:id>')
def hello(name, id):
   return "Hello, " + name + "\nYour Id is " +str(id)

@app.route('/onlyget', methods=['GET'])
def get_req():
   return '<h1> You can only get this webpage </h1>.'
 
if __name__ == "__main__":
    app.run(debug=True)