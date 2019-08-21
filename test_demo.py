from flask import Flask, send_file, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def hello_world():
    return render_template('login.html')


@app.route('/register')
def hello():
    return render_template('register.html')


if __name__ == '__main__':
    app.run()
