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


    
events = [    {
        "id": "1",
        "title": "Python",
        "description": "Aprender python",
        "date": "2025-09-10",
        "time": "14:00",
        "location": "Auditorio Principal",
        "category": "académico"
    },
]

usuarios = [
    {
        "id":"1",
        "nombre": "David  Garcia",
        "email": "David@abc.com"
    }
]


@app.route('/')
def index():
    return render_template('Home.html', events=events)


@app.route('/admin/Form', methods=["GET", "POST"])
def Formulario():
    form = SignupForm()
    if form.validate_on_submit():
        nuevo_evento = {
            "id": form.id.data,
            "title": form.title.data,
            "description": form.description.data,
            "date": form.date.data,
            "time": form.time.data,
            "location": form.location.data,
            "category": form.category.data  
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



