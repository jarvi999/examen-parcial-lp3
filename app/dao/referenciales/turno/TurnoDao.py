# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class TurnoDao:

    def getTurnos(self):

        TurnoSQL = """
        SELECT id, descripcion
        FROM Turno
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(TurnoSQL)
            Turnos = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': Turno[0], 'descripcion': Turno[1]} for Turno in Turnos]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las Turnos: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getTurnoById(self, id):

        TurnoSQL = """
        SELECT id, descripcion
        FROM Turno WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(TurnoSQL, (id,))
            TurnoEncontrada = cur.fetchone() # Obtener una sola fila
            if TurnoEncontrada:
                return {
                        "id": TurnoEncontrada[0],
                        "descripcion": TurnoEncontrada[1]
                    }  # Retornar los datos de la Turno
            else:
                return None # Retornar None si no se encuentra la Turno
        except Exception as e:
            app.logger.error(f"Error al obtener Turno: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarTurno(self, descripcion):

        insertTurnoSQL = """
        INSERT INTO Turno(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertTurnoSQL, (descripcion,))
            Turno_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return Turno_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar Turno: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateTurno(self, id, descripcion):

        updateTurnoSQL = """
        UPDATE Turno
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateTurnoSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar Turno: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteTurno(self, id):

        updateTurnoSQL = """
        DELETE FROM Turno
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateTurnoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar Turno: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()