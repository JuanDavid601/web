from flask import Flask, render_template, redirect, request, url_for
from .forms import SignupForm, UsuarioForm
from collections import defaultdict

"""
GROUP:
-Juan David Hincapie
-Juan David Garcia 
-Juan Felipe Bacca
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'unaclave'


#Estructura para categorias.
categorias = ['deportivo', 'académico', 'cultural']


    
events = [    {
        "id": "0",
        "title": "Python",
        "description": "Aprender python",
        "date": "2025-09-10",
        "time": "14:00",
        "location": "Auditorio Principal",
        "category": "académico",
        "Max_attendees": 50,
        "attendees": [
            {'name': 'Juan Pérez', 'email': 'juan@example.com'},
            {'name': 'Juan Felipe', 'email': 'juan@example.com'},
            {'name': 'Juan David Garcia', 'email': 'juan@example.com'},
            {'name': 'Juan Hincapie', 'email': 'juan@example.com'}
        ],
        "Visible":True
    },{
        "id": "1",
        "title": "C",
        "description": "Aprender C",
        "date": "2025-10-9",
        "time": "10:00",
        "location": "Auditorio Secundario",
        "category": "académico",
        "Max_attendees": 10,
        "attendees": [],
        "Visible":True
    },
    {
        "id": "2",
        "title": "Teatro",
        "description": "Aprender de Guion y Narrativa",
        "date": "2026-1-1",
        "time": "14:00",
        "location": "Auditorio XXX",
        "category": "cultural",
        "Max_attendees": 34,
        "attendees": [],
        "Visible":True
    }
]

@app.route("/Registro", methods=['POST'])
def registro():
    if request.method == "POST":
        id = request.form.get('id')
        return render_template("registro_evento.html", id=id)
    return render_template("registro_evento.html")

@app.route('/procesarRegistro', methods=['POST'])
def procesar_Nuevo_Registro():
    id = int(request.form['id'])
    nombre = request.form['nombre']
    email = request.form['email']

    for event in events:
        if event['id']==id:
            event['attendees'].append({'name': nombre, 'email': email})
            return redirect(url_for('index'))

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        EventosFiltrados=[]
        categoria =request.form["categorias"]
        for event in events:
            if event["category"]==categoria:
                EventosFiltrados.append(event)
        return render_template("Home.html",num_eventos= len(EventosFiltrados), eventos=EventosFiltrados, categorias=categorias)
    return render_template("Home.html",num_eventos= len(events), eventos=events, categorias=categorias)


@app.route('/NewEvent', methods=["GET", "POST"])
def Formulario():
    form = SignupForm()
    return render_template("Form.html", form=form)

@app.route('/procesarEvento', methods=['POST'])
def procesar_Nuevo_Evento():
    id = int(request.form['id'])
    title = request.form['title']
    description = request.form['description']
    date = request.form['date']
    time = request.form['time']
    location = request.form['location']
    category = request.form['category']
    Max_attendees = request.form['Max_attendees']

    nuevo_evento = {
             "id": id,
             "title": title,
             "description": description,
             "date": date,
             "time": time,
             "location": location,
             "category": category,
             "Max_attendees": Max_attendees,
             "attendees": [],
             "Visible":True
         }
    events.append(nuevo_evento)
    
    return redirect(url_for('index'))

# @app.route("/admin/Register", methods=["GET", "POST"])
# def Registro_usuario():
#     form = UsuarioForm()
#     if form.validate_on_submit():
#         nuevo_usuario = {
#             "id": form.id.data,
#             "nombre": form.nombre.data,
#             "email": form.email.data
#         }
#         usuarios.append(nuevo_usuario)
#         return redirect(url_for('index'))
#     return render_template('Registro_eventos.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)



