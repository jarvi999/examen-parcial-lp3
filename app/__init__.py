from flask import Flask

app = Flask(__name__)

# importar referenciales

#ciudad importar
from app.rutas.referenciales.ciudad.ciudad_routes import ciumod
#nacionalidad importar
from app.rutas.referenciales.nacionalidad.nacionalidad_routes import nacmod
#cliente importar
from app.rutas.referenciales.cliente.cliente_routes import clientemod
#estado civil
from app.rutas.referenciales.estado_civil.estado_civil_routes import estado_civilmod
#sexo
from app.rutas.referenciales.sexo.sexo_routes import sexomod
#repuesto
from app.rutas.referenciales.repuesto.repuesto_routes import repuestomod
#servicio
from app.rutas.referenciales.servicio.servicio_routes import serviciomod
#pais
from app.rutas.referenciales.pais.pais_routes import paismod
#ocupacion
from app.rutas.referenciales.ocupacion.ocupacion_routes import ocupacionmod
#turno
from app.rutas.referenciales.turno.turno_routes import turnomod
#estado
from app.rutas.referenciales.estado.estado_routes import estadomod
#mecanico
from app.rutas.referenciales.mecanico.mecanico_routes import mecanicomod
#pieza
from app.rutas.referenciales.pieza.pieza_routes import piezamod
#herramienta
from app.rutas.referenciales.herramienta.herramienta_routes import herramientamod
#incidencia
from app.rutas.referenciales.incidencia.incidencia_routes import incidenciamod










# registrar referenciales
modulo0 = '/referenciales'
app.register_blueprint(ciumod, url_prefix=f'{modulo0}/ciudad')
app.register_blueprint(nacmod, url_prefix=f'{modulo0}/nacionalidad')
app.register_blueprint(clientemod, url_prefix=f'{modulo0}/cliente')
app.register_blueprint(estado_civilmod, url_prefix=f'{modulo0}/estado_civil')
app.register_blueprint(sexomod, url_prefix=f'{modulo0}/sexo')
app.register_blueprint(repuestomod, url_prefix=f'{modulo0}/repuesto')
app.register_blueprint(serviciomod, url_prefix=f'{modulo0}/servicio')
app.register_blueprint(paismod, url_prefix=f'{modulo0}/pais')
app.register_blueprint(ocupacionmod, url_prefix=f'{modulo0}/ocupacion')
app.register_blueprint(turnomod, url_prefix=f'{modulo0}/turno')
app.register_blueprint(estadomod, url_prefix=f'{modulo0}/estado')
app.register_blueprint(mecanicomod, url_prefix=f'{modulo0}/mecanico')
app.register_blueprint(piezamod, url_prefix=f'{modulo0}/pieza')
app.register_blueprint(herramientamod, url_prefix=f'{modulo0}/herramienta')
app.register_blueprint(incidenciamod, url_prefix=f'{modulo0}/incidencia')







#ciudad
from app.rutas.referenciales.ciudad.ciudad_api import ciuapi
#nacionalidad
from app.rutas.referenciales.nacionalidad.nacionalidad_api import nacapi
#cliente
from app.rutas.referenciales.cliente.cliente_api import clienteapi
#estado civil
from app.rutas.referenciales.estado_civil.estado_civil_api import estado_civilapi
#sexo
from app.rutas.referenciales.sexo.sexo_api import sexoapi
#repuesto
from app.rutas.referenciales.repuesto.repuesto_api import repuestoapi
#servicio
from app.rutas.referenciales.servicio.servicio_api import servicioapi
#pais
from app.rutas.referenciales.pais.pais_api import paisapi
#ocupacion
from app.rutas.referenciales.ocupacion.ocupacion_api import ocupacionapi
#turno
from app.rutas.referenciales.turno.turno_api import turnoapi
#estado
from app.rutas.referenciales.estado.estado_api import estadoapi
#mecanico
from app.rutas.referenciales.mecanico.mecanico_api import mecanicoapi
#pieza
from app.rutas.referenciales.pieza.pieza_api import piezaapi
#herramienta
from app.rutas.referenciales.herramienta.herramienta_api import herramientaapi
#incidencia
from app.rutas.referenciales.incidencia.incidencia_api import incidenciaapi








# APIS v1
version1 = '/api/v1'
#apis ciudad
app.register_blueprint(ciuapi, url_prefix=version1)
#apis nacionalidad
app.register_blueprint(nacapi, url_prefix=version1)
#apis cliente
app.register_blueprint(clienteapi, url_prefix=version1)
#estado civil
app.register_blueprint(estado_civilapi, url_prefix=version1)
#sexo
app.register_blueprint(sexoapi, url_prefix=version1)
#repuesto
app.register_blueprint(repuestoapi, url_prefix=version1)
#servicio
app.register_blueprint(servicioapi, url_prefix=version1)
#pais
app.register_blueprint(paisapi, url_prefix=version1)
#ocupacion
app.register_blueprint(ocupacionapi, url_prefix=version1)
#turno
app.register_blueprint(turnoapi, url_prefix=version1)
#estado
app.register_blueprint(estadoapi, url_prefix=version1)
#mecanico
app.register_blueprint(mecanicoapi, url_prefix=version1)
#pieza
app.register_blueprint(piezaapi, url_prefix=version1)
#herramienta
app.register_blueprint(herramientaapi, url_prefix=version1)
#incidencia
app.register_blueprint(incidenciaapi, url_prefix=version1)
