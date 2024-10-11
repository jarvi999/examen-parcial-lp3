from flask import Blueprint, render_template

piezamod = Blueprint('pieza', __name__, template_folder='templates')

@piezamod.route('/pieza-index')
def piezaIndex():
    return render_template('pieza-index.html')