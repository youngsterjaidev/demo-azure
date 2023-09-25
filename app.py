from flask import Flask

app = Flask(__name__)

@app.route('/')
def return_message():
    return '<h1>Hello from Saurabh</h1>'

@app.route('/magicbus')
def magicbus_message():
    return '<h1>Hello from Magicbus</h1>'

if __name__ == '__main__':
    app.run(debug=True)
