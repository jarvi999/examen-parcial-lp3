from flask import Blueprint, render_template

estadomod = Blueprint('estado', __name__, template_folder='templates')

@estadomod.route('/estado-index')
def estadoIndex():
    return render_template('estado-index.html')