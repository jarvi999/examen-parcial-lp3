from flask import Blueprint, render_template

ocupacionmod = Blueprint('ocupacion', __name__, template_folder='templates')

@ocupacionmod.route('/ocupacion-index')
def ocupacionIndex():
    return render_template('ocupacion-index.html')