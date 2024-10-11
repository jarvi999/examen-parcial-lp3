from flask import Blueprint, render_template

estado_civilmod = Blueprint('estado_civil', __name__, template_folder='templates')

@estado_civilmod.route('/estado_civil-index')
def estado_civilIndex():
    return render_template('estado_civil-index.html')