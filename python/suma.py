from flask import Flask

app = Flask('__name__')



@app.route('/calculadora/<int:num1>/<int:num2>/<int:num3>/<int:num4>')
def calculadora(num1,num2,num3,num4,operation):
    if operation == "suma":
        return f" {num1 + num2 + num3 + num4}"
@app.route('/')
def suma():

    return 'suma'
if __name__ == '__main__':
    app.run(debug=True) 