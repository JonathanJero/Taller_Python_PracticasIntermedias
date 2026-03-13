from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# ─────────────────────────────────────────────
# CHECKPOINT 5 — App Final Completa
# ─────────────────────────────────────────────

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# ─── MODELO (versión extendida) ────────────────
class Tarea(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    titulo      = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.String(500), nullable=True)
    completada  = db.Column(db.Boolean, default=False)
    creada_en   = db.Column(db.DateTime, default=datetime.utcnow)  # ← EXTRA: fecha automática

    def __repr__(self):
        return f'<Tarea {self.id}: {self.titulo}>'


with app.app_context():
    db.create_all()


# ─── READ ──────────────────────────────────────
@app.route('/')
def index():
    filtro = request.args.get('filtro', 'todas')  # ← EXTRA: filtrado por URL

    if filtro == 'pendientes':
        tareas = Tarea.query.filter_by(completada=False).order_by(Tarea.id.desc()).all()
    elif filtro == 'completadas':
        tareas = Tarea.query.filter_by(completada=True).order_by(Tarea.id.desc()).all()
    else:
        tareas = Tarea.query.order_by(Tarea.id.desc()).all()

    total       = Tarea.query.count()
    completadas = Tarea.query.filter_by(completada=True).count()
    pendientes  = total - completadas

    return render_template('index.html',
        tareas=tareas,
        filtro=filtro,
        total=total,
        completadas=completadas,
        pendientes=pendientes
    )


# ─── CREATE ────────────────────────────────────
@app.route('/agregar', methods=['POST'])
def agregar():
    titulo      = request.form['titulo']
    descripcion = request.form.get('descripcion', '')

    if titulo.strip():
        nueva_tarea = Tarea(titulo=titulo.strip(), descripcion=descripcion.strip())
        db.session.add(nueva_tarea)
        db.session.commit()

    return redirect(url_for('index'))


# ─── UPDATE (toggle) ───────────────────────────
@app.route('/completar/<int:id>')
def completar(id):
    tarea = Tarea.query.get_or_404(id)
    tarea.completada = not tarea.completada
    db.session.commit()
    return redirect(url_for('index'))


# ─── UPDATE (editar) ───────────────────────────
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tarea = Tarea.query.get_or_404(id)

    if request.method == 'POST':
        tarea.titulo      = request.form['titulo']
        tarea.descripcion = request.form.get('descripcion', '')
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('editar.html', tarea=tarea)


# ─── ACERCA ───────────────────────────────────
@app.route('/acerca')
def acerca():
    return render_template('acerca.html')


# ─── DELETE ────────────────────────────────────
@app.route('/eliminar/<int:id>')
def eliminar(id):
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
