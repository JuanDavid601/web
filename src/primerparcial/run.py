from flask import Flask, render_template, redirect, request, url_for
from .forms import SignupForm, UsuarioForm

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
usuarios = []

    
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
        ]
    },
]

@app.route("/Registro", methods=['POST'])
def registro():
    if request.method == "POST":
        id = request.form.get('id')
        return render_template("registro_evento.html", id=id)
    
    return render_template("registro_evento.html")

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        id = int(request.form.get('id'))
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        
        try:
            events[id]['attendees'].append({'name': nombre, 'email': email})
        except:
            return render_template("Home.html",num_eventos= len(events), eventos=events)

    return render_template("Home.html",num_eventos= len(events), eventos=events)


@app.route('/Admin/Form', methods=["GET", "POST"])
def Formulario():
    form = SignupForm()
    if form.validate_on_submit():
        id = form.id.data
        title = form.time.data
        descripcion = form.description.data
        date = form.date.data
        time = form.time.data
        localisacion = form.location.data
        categoria = form.category.data

        print(id, title, descripcion, date, time, localisacion, categoria)

        nuevo_evento = {
            "id": id,
            "title": title,
            "description": descripcion,
            "date": date,
            "time": time,
            "location": localisacion,
            "category": categoria,
            "attendees": []
        }
        events.append(nuevo_evento)

        next_page = request.args.get('next', None)
        if next_page:
            return redirect(next_page)
        return redirect(url_for('index'))
    return render_template("Form.html", form=form)




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



