@app.route('/calculadora/<operation>/<int:num1>/<int:num2>/<int:num3>/<int:num4>')
def calculadora(num1,num2,num3,num4,operation):
    if operation == "suma":
        return f" {num1 + num2 + num3 + num4}"