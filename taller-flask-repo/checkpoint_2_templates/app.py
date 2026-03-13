from flask import Flask, render_template, request

app = Flask(__name__)


# ─────────────────────────────────────────────
# BLOQUE 2 — Templates Jinja2 y Formularios
# ─────────────────────────────────────────────

@app.route('/')
def inicio():
    # Pasamos variables al template
    tareas_ejemplo = ['Aprender Flask', 'Crear templates', 'Conectar BD']
    return render_template('index.html', titulo='Inicio', tareas=tareas_ejemplo)


@app.route('/acerca')
def acerca():
    return render_template('acerca.html', titulo='Acerca del Taller')


# Ruta que acepta GET (mostrar form) y POST (procesar form)
@app.route('/saludo', methods=['GET', 'POST'])
def saludo():
    nombre = None
    if request.method == 'POST':
        nombre = request.form['nombre']  # Leer dato del formulario
    return render_template('saludo.html', titulo='Saludo', nombre=nombre)


if __name__ == '__main__':
    app.run(debug=True)
