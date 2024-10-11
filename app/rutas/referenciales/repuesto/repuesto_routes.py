from flask import Blueprint, render_template

repuestomod = Blueprint('repuesto', __name__, template_folder='templates')

@repuestomod.route('/repuesto-index')
def repuestoIndex():
    return render_template('repuesto-index.html')