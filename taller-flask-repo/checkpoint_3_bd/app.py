from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ─────────────────────────────────────────────
# BLOQUE 3 — Conexión a Base de Datos
# ─────────────────────────────────────────────

# Configuración de SQLite — crea tareas.db en esta carpeta
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ─── MODELO ───────────────────────────────────
# Una clase Python = una tabla en la base de datos
# Un objeto = una fila en esa tabla

class Tarea(db.Model):
    id         = db.Column(db.Integer, primary_key=True)          # ID único, autoincrementado
    titulo     = db.Column(db.String(200), nullable=False)        # Texto obligatorio
    descripcion= db.Column(db.String(500), nullable=True)         # Texto opcional
    completada = db.Column(db.Boolean, default=False)             # True / False

    def __repr__(self):
        return f'<Tarea {self.id}: {self.titulo}>'


# Crear las tablas al iniciar la app
with app.app_context():
    db.create_all()
    print("✅ Base de datos lista — archivo tareas.db creado")


# ─── RUTAS ────────────────────────────────────

@app.route('/')
def index():
    # Por ahora mostramos todas las tareas (vacío al inicio)
    tareas = Tarea.query.all()
    return render_template('index.html', tareas=tareas)


if __name__ == '__main__':
    app.run(debug=True)
