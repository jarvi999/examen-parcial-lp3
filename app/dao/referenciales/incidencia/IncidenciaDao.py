# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class IncidenciaDao:

    def getIncidencias(self):

        IncidenciaSQL = """
        SELECT id, descripcion
        FROM Incidencia
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(IncidenciaSQL)
            Incidencias = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': Incidencia[0], 'descripcion': Incidencia[1]} for Incidencia in Incidencias]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las Incidencias: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getIncidenciaById(self, id):

        IncidenciaSQL = """
        SELECT id, descripcion
        FROM Incidencia WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(IncidenciaSQL, (id,))
            IncidenciaEncontrada = cur.fetchone() # Obtener una sola fila
            if IncidenciaEncontrada:
                return {
                        "id": IncidenciaEncontrada[0],
                        "descripcion": IncidenciaEncontrada[1]
                    }  # Retornar los datos de la Incidencia
            else:
                return None # Retornar None si no se encuentra la Incidencia
        except Exception as e:
            app.logger.error(f"Error al obtener Incidencia: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarIncidencia(self, descripcion):

        insertIncidenciaSQL = """
        INSERT INTO Incidencia(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertIncidenciaSQL, (descripcion,))
            Incidencia_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return Incidencia_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar Incidencia: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateIncidencia(self, id, descripcion):

        updateIncidenciaSQL = """
        UPDATE Incidencia
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateIncidenciaSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar Incidencia: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteIncidencia(self, id):

        updateIncidenciaSQL = """
        DELETE FROM Incidencia
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateIncidenciaSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar Incidencia: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()