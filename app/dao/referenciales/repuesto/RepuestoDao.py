# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class RepuestoDao:

    def getRepuestos(self):

        RepuestoSQL = """
        SELECT id, descripcion
        FROM Repuesto
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(RepuestoSQL)
            Repuestos = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': Repuesto[0], 'descripcion': Repuesto[1]} for Repuesto in Repuestos]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las Repuestos: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getRepuestoById(self, id):

        RepuestoSQL = """
        SELECT id, descripcion
        FROM Repuesto WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(RepuestoSQL, (id,))
            RepuestoEncontrada = cur.fetchone() # Obtener una sola fila
            if RepuestoEncontrada:
                return {
                        "id": RepuestoEncontrada[0],
                        "descripcion": RepuestoEncontrada[1]
                    }  # Retornar los datos de la Repuesto
            else:
                return None # Retornar None si no se encuentra la Repuesto
        except Exception as e:
            app.logger.error(f"Error al obtener Repuesto: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarRepuesto(self, descripcion):

        insertRepuestoSQL = """
        INSERT INTO Repuesto(descripcion) VALUES(%s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertRepuestoSQL, (descripcion,))
            Repuesto_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return Repuesto_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar Repuesto: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateRepuesto(self, id, descripcion):

        updateRepuestoSQL = """
        UPDATE Repuesto
        SET descripcion=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateRepuestoSQL, (descripcion, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar Repuesto: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteRepuesto(self, id):

        updateRepuestoSQL = """
        DELETE FROM Repuesto
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateRepuestoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar Repuesto: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()