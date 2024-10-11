# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class HerramientaDao:

    def getHerramientas(self):

        HerramientaSQL = """
        SELECT id, descripcion
        FROM Herramienta
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(HerramientaSQL)
            Herramientas = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': Herramienta[0], 'descripcion': Herramienta[1]} for Herramienta in Herramientas]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las Herramientas: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getHerramientaById(self, id):

        HerramientaSQL = """
        SELECT id, descripcion
        FROM Herramienta WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(HerramientaSQL, (id,))
            HerramientaEncontrada = cur.fetchone() # Obtener una sola fila
            if HerramientaEncontrada:
                return {
                        "id": HerramientaEncontrada[0],
                        "descripcion": HerramientaEncontrada[1]
                    }  # Retornar los datos de la Herramienta
            else:
                return None # Retornar None si no se encuentra la Herramienta
        except Exception as e:
            app.logger.error(f"Error al obtener Herramienta: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarHerramienta(self, descripcion):

        insertHerramientaSQL = """
        INSERT INTO Herramienta(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertHerramientaSQL, (descripcion,))
            Herramienta_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return Herramienta_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar Herramienta: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateHerramienta(self, id, descripcion):

        updateHerramientaSQL = """
        UPDATE Herramienta
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateHerramientaSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar Herramienta: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteHerramienta(self, id):

        updateHerramientaSQL = """
        DELETE FROM Herramienta
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateHerramientaSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar Herramienta: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()