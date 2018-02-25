from flask import Flask, redirect, render_template, url_for
from tests.user import User
from tests.reviews import Reviews
from tests.business import Business

app = Flask(__name__, template_folder='Designs/UI')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)