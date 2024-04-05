from flask import Flask

app = Flask('__name__')

@app.route('/')#pagina principal
def index():
    return ('Tu nombre es:')

@app.route('/home/<name>')#inicio
def home(name):  
    return f'Tu nombre es: {name}'  

@app.route("/login") 
def login():
    return "Bienvenido" 
  
if __name__ == '__main__':
    app.run(debug=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
