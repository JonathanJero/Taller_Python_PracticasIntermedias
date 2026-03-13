# 🐍 Taller: Desarrollo Web con Python — Flask + SQLite

Repositorio del taller de desarrollo web. Aquí encontrás el código base de cada bloque para que puedas seguir el taller paso a paso, o retomar desde donde te quedaste.

---

## 🗂️ Estructura del repositorio

```
taller-flask/
├── checkpoint_0_base/        ← Punto de partida — entorno listo, app vacía
├── checkpoint_1_servidor/    ← Bloque 1: primer servidor y rutas
├── checkpoint_2_templates/   ← Bloque 2: templates, formularios GET/POST
├── checkpoint_3_bd/          ← Bloque 3: base de datos y modelo
├── checkpoint_4_crud/        ← Bloque 4: CRUD completo
└── checkpoint_5_final/       ← App final con estilos CSS
```

Cada carpeta es **independiente** — podés hacer pull de cualquiera y arrancá desde ahí.

---

## 🚀 Cómo empezar (desde cero)

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/taller-flask.git
cd taller-flask

# 2. Entrar al checkpoint que quieras
cd checkpoint_0_base

# 3. Crear entorno virtual
python -m venv venv

# 4. Activar entorno virtual
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 5. Instalar dependencias
pip install -r requirements.txt

# 6. Correr la aplicación
python app.py
```

Luego abrí tu navegador en **http://localhost:5000**

---

## 📦 Checkpoints

| Checkpoint | Bloque | Qué incluye |
|-----------|--------|-------------|
| `checkpoint_0_base` | — | Entorno vacío listo para arrancar |
| `checkpoint_1_servidor` | Bloque 1 | `app.py` con rutas básicas y parámetros |
| `checkpoint_2_templates` | Bloque 2 | Templates Jinja2, base.html, formularios GET/POST |
| `checkpoint_3_bd` | Bloque 3 | Modelo SQLite con SQLAlchemy configurado |
| `checkpoint_4_crud` | Bloque 4 | CRUD completo: crear, leer, completar, eliminar |
| `checkpoint_5_final` | Bloque 5 | App terminada con CSS y funcionalidades extra |

---

## 🛠️ Stack tecnológico

- **Python 3.11+**
- **Flask 3.x** — framework web
- **Flask-SQLAlchemy** — ORM para base de datos
- **SQLite** — base de datos (viene con Python, sin instalación)
- **Jinja2** — motor de templates (incluido en Flask)

---

## 📚 Recursos para seguir aprendiendo

- [Documentación oficial de Flask](https://flask.palletsprojects.com)
- [Real Python — Flask tutorials](https://realpython.com/tutorials/flask/)
- [Full Stack Python](https://www.fullstackpython.com)
- [Flask-SQLAlchemy docs](https://flask-sqlalchemy.palletsprojects.com)

---

## ❓ ¿Tenés preguntas?

Podés escribirle a los tutores del taller. ¡Éxito!
