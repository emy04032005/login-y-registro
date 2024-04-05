from flask import Flask

app= Flask(__name__ )

@app.route('/')
def run():
    return '<center><h1>hello, world!</h1><center/>'

@app.route("/login/<name>")
def login(name):
    return f'Tu nombre es {name}'


if __name__ == '__main__':
    app.run(debug = True)