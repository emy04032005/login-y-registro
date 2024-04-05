from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos de ejemplo: nombre de usuario y contraseña
usuarios = {'usuario1': 'contraseña1', 'usuario2': 'contraseña2'}

@app.route('/')
def redireccionar_a_login():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    mensaje = ''
    if request.method == 'POST':
        usuario = request.form['username']
        contraseña = request.form['password']
        if usuario in usuarios and usuarios[usuario] == contraseña:
            # Iniciar sesión exitosa, redireccionar a la página de inicio
            return redirect(url_for('inicio_bienvenida'))
        else:
            mensaje = 'Nombre de usuario o contraseña incorrectos'
    return render_template('login.html', mensaje=mensaje)

@app.route('/inicio')
def inicio_bienvenida():
    return '¡Bienvenido! Has iniciado sesión correctamente.'

@app.route('/registro')
def registro():
    return render_template('registro.html')


if __name__ == '__main__':
    app.run(debug=True)
