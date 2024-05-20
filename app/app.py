from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    jugadores = ['mbappe','jouse','jaimito','roberto carlos']
    data = {
        'jugadores':jugadores,
        'titulo': 'mejores',
        'bienvenida': '4',
        'numero_de_jugadores':len(jugadores)
    }
    return render_template('index.html', data=data)
@app.route('/contacto/<nombre>')
def contacto(nombre):
    data={
        'titulo':'contacto',
        'nombre':nombre
    }
    return render_template('contacto.html', data=data)
    
if __name__ =='__main__':
    app.run(debug=True,port=5000)