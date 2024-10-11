# Data access object - DAO
from flask import current_app as app
from app.conexion.Conexion import Conexion

class MecanicoDao:

    def getMecanicos(self):

        MecanicoSQL = """
        SELECT id, descripcion, correo, telefono
        FROM Mecanico
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(MecanicoSQL)
            Mecanicos = cur.fetchall() # trae datos de la bd

            # Transformar los datos en una lista de diccionarios
            return [{'id': Mecanico[0], 'descripcion': Mecanico[1], 'correo': Mecanico[2], 'telefono': Mecanico[3]} for Mecanico in Mecanicos]

        except Exception as e:
            app.logger.error(f"Error al obtener todas las Mecanicos: {str(e)}")
            return []

        finally:
            cur.close()
            con.close()

    def getMecanicoById(self, id):

        MecanicoSQL = """
        SELECT id, descripcion, correo, telefono
        FROM Mecanico WHERE id=%s
        """
        # objeto conexion
        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()
        try:
            cur.execute(MecanicoSQL, (id,))
            MecanicoEncontrada = cur.fetchone() # Obtener una sola fila
            if MecanicoEncontrada:
                return {
                        "id": MecanicoEncontrada[0],
                        "descripcion": MecanicoEncontrada[1],
                        "correo": MecanicoEncontrada[2],
                        "telefono": MecanicoEncontrada[3]
                    }  # Retornar los datos de la Mecanico
            else:
                return None # Retornar None si no se encuentra la Mecanico
        except Exception as e:
            app.logger.error(f"Error al obtener Mecanico: {str(e)}")
            return None

        finally:
            cur.close()
            con.close()

    def guardarMecanico(self, descripcion, correo, telefono):

        insertMecanicoSQL = """
        INSERT INTO Mecanico(descripcion, correo, telefono) VALUES(%s, %s, %s) RETURNING id
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        # Ejecucion exitosa
        try:
            cur.execute(insertMecanicoSQL, (descripcion, correo, telefono))
            Mecanico_id = cur.fetchone()[0]
            con.commit() # se confirma la insercion
            return Mecanico_id

        # Si algo fallo entra aqui
        except Exception as e:
            app.logger.error(f"Error al insertar Mecanico: {str(e)}")
            con.rollback() # retroceder si hubo error
            return False

        # Siempre se va ejecutar
        finally:
            cur.close()
            con.close()

    def updateMecanico(self, id, descripcion, correo, telefono):

        updateMecanicoSQL = """
        UPDATE Mecanico
        SET descripcion=%s, correo=%s, telefono=%s
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateMecanicoSQL, (descripcion, correo, telefono, id,))
            filas_afectadas = cur.rowcount # Obtener el número de filas afectadas
            con.commit()

            return filas_afectadas > 0 # Retornar True si se actualizó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al actualizar Mecanico: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()

    def deleteMecanico(self, id):

        updateMecanicoSQL = """
        DELETE FROM Mecanico
        WHERE id=%s
        """

        conexion = Conexion()
        con = conexion.getConexion()
        cur = con.cursor()

        try:
            cur.execute(updateMecanicoSQL, (id,))
            rows_affected = cur.rowcount
            con.commit()

            return rows_affected > 0  # Retornar True si se eliminó al menos una fila

        except Exception as e:
            app.logger.error(f"Error al eliminar Mecanico: {str(e)}")
            con.rollback()
            return False

        finally:
            cur.close()
            con.close()
