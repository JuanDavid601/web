from flask import Flask, render_template, redirect, request, url_for
from .forms import SignupForm

"""
GROUP:
-Juan David Hincapie
-Juan David Garcia 
-Juan Felipe Bacca
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'unaclave'
# Estructura para eventos
# events = [
#     {
#         'id': 1,
#         'title': 'Conferencia de Python',
#         'slug': 'conferencia-python',
#         'description': 'Descripción del evento...',
#         'date': '2025-09-15',
#         'time': '14:00',
#         'location': 'Auditorio Principal',
#         'category': 'Tecnología',
#         'max_attendees': 50,
#         'attendees': [
#             {'name': 'Juan Pérez', 'email': 'juan@example.com'}
#         ],
#         'featured': True
#     }
# ]

## Estructura para categorias.
# categoria = ['deportivo', 'académico', 'cultural']

# @app.route('/')
# def Home():
#     render_template("Home.html", id=events[0]['id'],
#                     title=events[0]['title'],
#                     description=events[0]['description'],
#                     date=events[0]['date'],
#                     location=events[0]['location'],
#                     category=events[0]['category']
#     )
    

@app.route('/', methods=["GET", "POST"] )
def Formulario():
    form = SignupForm()
    if form.validate_on_submit():
        id = form.id.data
        title = form.title.data
        description = form.description.data
        date = form.date.data
        time = form.time.data
        location = form.location.data
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))
    return render_template("Form.html", form=form)









if __name__ == "__main__":
    app.run(debug=True)



