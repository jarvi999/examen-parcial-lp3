# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class Estado_civilDao:

    def getEstado_civiles(self):

        estado_civilSQL = """
        SELECT id, descripcion
        FROM estado_civil
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(estado_civilSQL)
            estado_civiles = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': estado_civil[0], 'descripcion': estado_civil[1]} for estado_civil in estado_civiles]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las estado_civiles: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getEstado_civilById(self, id):

        estado_civilSQL = """
        SELECT id, descripcion
        FROM estado_civil WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(estado_civilSQL, (id,))
            estado_civilEncontrada = cur.fetchone() # Obtener una sola fila
            if estado_civilEncontrada:
                return {
                        "id": estado_civilEncontrada[0],
                        "descripcion": estado_civilEncontrada[1]
                    }  # Retornar los datos de la estado_civil
            else:
                return None # Retornar None si no se encuentra la estado_civil
        except Exception as e:
            app.logger.error(f"Error al obtener estado_civil: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarEstado_civil(self, descripcion):

        insertEstado_civilSQL = """
        INSERT INTO estado_civil(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertEstado_civilSQL, (descripcion,))
            estado_civil_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return estado_civil_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar el estado civil: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateEstado_civil(self, id, descripcion):

        updateEstado_civilSQL = """
        UPDATE estado_civil
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateEstado_civilSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar estado civil: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteEstado_civil(self, id):

        updateEstado_civilSQL = """
        DELETE FROM estado_civil
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateEstado_civilSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar estado_civil: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()