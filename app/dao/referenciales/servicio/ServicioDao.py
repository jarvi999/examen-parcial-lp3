# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class ServicioDao:

    def getServicios(self):

        servicioSQL = """
        SELECT id, descripcion
        FROM servicio
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(servicioSQL)
            servicios = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': servicio[0], 'descripcion': servicio[1]} for servicio in servicios]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las servicios: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getServicioById(self, id):

        servicioSQL = """
        SELECT id, descripcion
        FROM servicio WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(servicioSQL, (id,))
            servicioEncontrada = cur.fetchone() # Obtener una sola fila
            if servicioEncontrada:
                return {
                        "id": servicioEncontrada[0],
                        "descripcion": servicioEncontrada[1]
                    }  # Retornar los datos de la servicio
            else:
                return None # Retornar None si no se encuentra la servicio
        except Exception as e:
            app.logger.error(f"Error al obtener servicio: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarServicio(self, descripcion):

        insertServicioSQL = """
        INSERT INTO servicio(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertServicioSQL, (descripcion,))
            servicio_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return servicio_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar servicio: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateServicio(self, id, descripcion):

        updateServicioSQL = """
        UPDATE servicio
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateServicioSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar servicio: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteServicio(self, id):

        updateServicioSQL = """
        DELETE FROM servicio
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateServicioSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar servicio: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()