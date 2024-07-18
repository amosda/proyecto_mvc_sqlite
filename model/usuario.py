import sqlite3 as bd

class Usuario:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    
    @staticmethod
    def crear_tabla():
        conn = bd.connect('base_usuarios.db');
        cursor = conn.cursor();
        sql = """ CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    edad INTEGER NOT NULL);"""
        cursor.execute(sql);
        conn.commit();
        conn.close();

    def guardar(self):
        conn = bd.connect('base_usuarios.db');
        cursor = conn.cursor();
        cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES(?, ?)', (self.nombre, self.edad) );
        conn.commit();
        conn.close();


    @staticmethod
    def mostrar_datos():
        conn = bd.connect('base_usuarios.db');
        cursor = conn.cursor();
        cursor.execute('SELECT * FROM usuarios')
        usuarios = cursor.fetchall()
        conn.close();
        return usuarios
    
