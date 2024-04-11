from flask import Flask

app = Flask(__name__)

#Declaracion de ruta.
@app.route('/')
def index():
    return '<h1>Hola Mundo :D</h1>'

# Componente de nombre dinamico.
@app.route('/user/<name>')
def user(name):
    return '<h1>Hola, %s!</h1>' % name

# Inicio del servidor.
if __name__ == '__main__':
    app.run(debug=True)
