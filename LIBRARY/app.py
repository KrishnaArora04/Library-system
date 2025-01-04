from flask import Flask, render_template
from routes.books import books_blueprint
from routes.members import members_blueprint

app = Flask(__name__)

app.register_blueprint(books_blueprint, url_prefix='/api/books')
app.register_blueprint(members_blueprint, url_prefix='/api/members')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/members')
def members():
    return render_template('members.html')

if __name__ == '__main__':
    app.run(debug=True)
