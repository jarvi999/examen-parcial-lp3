from flask import Blueprint, render_template

incidenciamod = Blueprint('incidencia', __name__, template_folder='templates')

@incidenciamod.route('/incidencia-index')
def incidenciaIndex():
    return render_template('incidencia-index.html')