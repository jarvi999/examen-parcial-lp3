# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class EstadoDao:

    def getEstados(self):

        EstadoSQL = """
        SELECT id, descripcion
        FROM Estado
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(EstadoSQL)
            Estados = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': Estado[0], 'descripcion': Estado[1]} for Estado in Estados]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las Estados: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getEstadoById(self, id):

        EstadoSQL = """
        SELECT id, descripcion
        FROM Estado WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(EstadoSQL, (id,))
            EstadoEncontrada = cur.fetchone() # Obtener una sola fila
            if EstadoEncontrada:
                return {
                        "id": EstadoEncontrada[0],
                        "descripcion": EstadoEncontrada[1]
                    }  # Retornar los datos de la Estado
            else:
                return None # Retornar None si no se encuentra la Estado
        except Exception as e:
            app.logger.error(f"Error al obtener Estado: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarEstado(self, descripcion):

        insertEstadoSQL = """
        INSERT INTO Estado(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertEstadoSQL, (descripcion,))
            Estado_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return Estado_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar Estado: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateEstado(self, id, descripcion):

        updateEstadoSQL = """
        UPDATE Estado
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateEstadoSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar Estado: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteEstado(self, id):

        updateEstadoSQL = """
        DELETE FROM Estado
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateEstadoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar Estado: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()