from flask import Flask

app = Flask('__name__')

@app.route('/')
@app.route("/prueba1/<name>")
@app.route("/prueba1/<name>/<int:edad>")
def hello_word(name = None, edad =None):
    if edad == None :
    
       return f"<center><h1>Mi Otro nombre es : {name}</h1></center>"
    else:
         return f"<center><h1>Mi Otro nombre es : {name} y su edad es: {edad}</h1></center>"

     
if (__name__) == ('__main__'):
     app.run(debug = True)