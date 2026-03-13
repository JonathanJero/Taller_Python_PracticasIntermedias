from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ─────────────────────────────────────────────
# BLOQUE 4 — CRUD Completo
# Create · Read · Update · Delete
# ─────────────────────────────────────────────

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Tarea(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    titulo      = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.String(500), nullable=True)
    completada  = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Tarea {self.id}: {self.titulo}>'


with app.app_context():
    db.create_all()


# ─── READ ──────────────────────────────────────
# Mostrar todas las tareas
@app.route('/')
def index():
    tareas = Tarea.query.order_by(Tarea.id.desc()).all()  # Más recientes primero
    return render_template('index.html', tareas=tareas)


# ─── CREATE ────────────────────────────────────
# Recibir el formulario y guardar nueva tarea
@app.route('/agregar', methods=['POST'])
def agregar():
    titulo      = request.form['titulo']
    descripcion = request.form.get('descripcion', '')  # Opcional

    if titulo.strip():  # No guardar tareas vacías
        nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion)
        db.session.add(nueva_tarea)
        db.session.commit()

    return redirect(url_for('index'))


# ─── UPDATE (toggle completada) ────────────────
# Marcar / desmarcar tarea como completada
@app.route('/completar/<int:id>')
def completar(id):
    tarea = Tarea.query.get_or_404(id)    # 404 si no existe
    tarea.completada = not tarea.completada
    db.session.commit()
    return redirect(url_for('index'))


# ─── UPDATE (editar título) ────────────────────
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tarea = Tarea.query.get_or_404(id)

    if request.method == 'POST':
        tarea.titulo      = request.form['titulo']
        tarea.descripcion = request.form.get('descripcion', '')
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('editar.html', tarea=tarea)


# ─── DELETE ────────────────────────────────────
@app.route('/eliminar/<int:id>')
def eliminar(id):
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
