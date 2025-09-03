from flask import Flask, render_template, redirect, request, url_for
from forms import SignupForm, UsuarioForm

"""
GROUP:
-Juan David Hincapie
-Juan David Garcia 
-Juan Felipe Bacca
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'unaclave'


#Estructura para categorias.
categoria = ['deportivo', 'académico', 'cultural']


    
events = [    {
        "id": "0",
        "title": "Python",
        "description": "Aprender python",
        "date": "2025-09-10",
        "time": "14:00",
        "location": "Auditorio Principal",
        "category": "académico",
        "attendees": [
            {'name': 'Juan Pérez', 'email': 'juan@example.com'},
            {'name': 'Juan Felipe', 'email': 'juan@example.com'},
            {'name': 'Juan David Garcia', 'email': 'juan@example.com'},
            {'name': 'Juan Hincapie', 'email': 'juan@example.com'}
        ],
        "Visible":True
    },
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

    events[id]['attendees'].append({'name': nombre, 'email': email})
    
    return redirect(url_for('index'))

@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("Home.html",num_eventos= len(events), eventos=events)


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

    nuevo_evento = {
             "id": id,
             "title": title,
             "description": description,
             "date": date,
             "time": time,
             "location": location,
             "category": category,
             "attendees": [],
             "Visible":True
         }
    events.append(nuevo_evento)
    
    return redirect(url_for('index'))



@app.route("/admin/Register", methods=["GET", "POST"])
def Registro_usuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        nuevo_usuario = {
            "id": form.id.data,
            "nombre": form.nombre.data,
            "email": form.email.data
        }
        usuarios.append(nuevo_usuario)
        return redirect(url_for('index'))
    return render_template('Registro_eventos.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)



