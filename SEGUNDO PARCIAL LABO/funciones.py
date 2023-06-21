import pygame
import sqlite3

def cargar_foto(path:str,ancho:int,alto:int):
    '''Recibe por parametro el path de la foto a cargar.
    Carga la imagen y la escala segun el ancho y el alto.
    Retorna la imagen'''
    fondo_inicio = pygame.image.load(path)
    fondo_inicio = pygame.transform.scale(fondo_inicio, (ancho,alto))
    return fondo_inicio

def crear_tabla():
    '''Realiza la creacion de la tabla de jugadores con sus scores'''
    with sqlite3.connect("record_scores.db") as conexion:
        try:
            sentencia = ''' create  table jugadores
            (
            id integer primary key autoincrement,
            usuario text,
            score integer
            )
            '''
            conexion.execute(sentencia)
            print("Se creo la tabla jugadores")                       
        except sqlite3.OperationalError:
            print("La tabla jugadores ya existe")

def commitear_tabla(usuario,score):
    '''Actualiza los valores de usuario y score pasador por parametro
    en la base de datos'''
    with sqlite3.connect("record_scores.db") as conexion:
        try:
            conexion.execute("insert into jugadores(usuario,score) values (?,?)", (f"{usuario}",score))
            conexion.commit()# Actualiza los datos realmente en la tabla
        except:
            print("Error")

def get_scores_ordenados():
    '''Obtiene los valores ordenados segun score de forma descendente.
    Retorna una lista con los valores de cada jugador ordenados'''
    with sqlite3.connect("record_scores.db") as conexion:
        cursor=conexion.execute("SELECT * FROM jugadores ORDER BY score DESC;")
        lista_filas = []
    for fila in cursor:
        lista_filas.append(fila)    
    return lista_filas

        
    
