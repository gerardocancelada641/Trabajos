import mysql.connector
from mysql.connector import Error
import itertools

def conectar_a_mysql():
    try:
        # Establecer la conexión
        conexion = mysql.connector.connect(
            host='localhost',          
            user='root',         
            password='qwert',  
            database='escuela' 
        )
       
        if conexion.is_connected():
            print('Conexión exitosa a la base de datos MySQL')

            db_info = conexion.get_server_info()
            print(f"Conectado al servidor MySQL versión: {db_info}")

            cursor = conexion.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            print(f"Base de datos activa: {db_name}")
           
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM alumnos")  
            resultados = cursor.fetchall()


            students_data = []

            for fila in resultados:
                student = {"ID:":fila[0], "Name":fila[1]}
                students_data.append(student)
    
            print(students_data)

            cursor.close()

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

    finally:
        if conexion.is_connected():
            conexion.close()
            print("Conexión a MySQL cerrada")

conectar_a_mysql()