from flask import Flask

app = Flask(_name_)

@app.route('/return')
def return_message():
    return '<h1>Hello from Saurabh</h1>'

@app.route('/magicbus')
def magicbus_message():
    return '<h1>Hello from Magicbus</h1>'

if _name_ == '_main_':
    app.run(debug=True)
