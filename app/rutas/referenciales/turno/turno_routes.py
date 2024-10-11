from flask import Blueprint, render_template

turnomod = Blueprint('turno', __name__, template_folder='templates')

@turnomod.route('/turno-index')
def turnoIndex():
    return render_template('turno-index.html')