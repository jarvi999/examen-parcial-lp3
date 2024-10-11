# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class PiezaDao:

    def getPiezas(self):

        PiezaSQL = """
        SELECT id, descripcion
        FROM Pieza
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(PiezaSQL)
            Piezas = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': Pieza[0], 'descripcion': Pieza[1]} for Pieza in Piezas]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las Piezas: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getPiezaById(self, id):

        PiezaSQL = """
        SELECT id, descripcion
        FROM Pieza WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(PiezaSQL, (id,))
            PiezaEncontrada = cur.fetchone() # Obtener una sola fila
            if PiezaEncontrada:
                return {
                        "id": PiezaEncontrada[0],
                        "descripcion": PiezaEncontrada[1]
                    }  # Retornar los datos de la Pieza
            else:
                return None # Retornar None si no se encuentra la Pieza
        except Exception as e:
            app.logger.error(f"Error al obtener Pieza: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarPieza(self, descripcion):

        insertPiezaSQL = """
        INSERT INTO Pieza(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertPiezaSQL, (descripcion,))
            Pieza_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return Pieza_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar Pieza: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updatePieza(self, id, descripcion):

        updatePiezaSQL = """
        UPDATE Pieza
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updatePiezaSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar Pieza: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deletePieza(self, id):

        updatePiezaSQL = """
        DELETE FROM Pieza
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updatePiezaSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar Pieza: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()