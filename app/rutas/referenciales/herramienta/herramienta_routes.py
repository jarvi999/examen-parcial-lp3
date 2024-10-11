from flask import Blueprint, render_template

herramientamod = Blueprint('herramienta', __name__, template_folder='templates')

@herramientamod.route('/herramienta-index')
def herramientaIndex():
    return render_template('herramienta-index.html')