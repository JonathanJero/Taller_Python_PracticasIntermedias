from flask import Flask

app = Flask(__name__)


# ─────────────────────────────────────────────
# BLOQUE 1 — Primer servidor web
# ─────────────────────────────────────────────

# Ruta principal
@app.route('/')
def inicio():
    return '<h1>¡Bienvenido al Taller Flask!</h1><p>El servidor está corriendo correctamente.</p>'


# Ruta secundaria fija
@app.route('/acerca')
def acerca():
    return '<h1>Sobre el Taller</h1><p>Desarrollo Web con Python — Flask + SQLite</p>'


# Ruta con parámetro dinámico (string)
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'<h1>¡Hola, {nombre}! 👋</h1>'


# Ruta con parámetro tipado (entero)
@app.route('/item/<int:id>')
def item(id):
    return f'<p>Estás viendo el item número: <strong>{id}</strong></p>'


# ─────────────────────────────────────────────
# ACTIVIDAD: Agregá tu propia ruta aquí abajo
# Ejemplo: /mi-ruta que devuelva tu nombre
# ─────────────────────────────────────────────


if __name__ == '__main__':
    app.run(debug=True)
