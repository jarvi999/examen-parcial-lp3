from flask import Blueprint, render_template

mecanicomod = Blueprint('mecanico', __name__, template_folder='templates')

@mecanicomod.route('/mecanico-index')
def mecanicoIndex():
    return render_template('mecanico-index.html')