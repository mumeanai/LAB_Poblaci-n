import csv
from collections import namedtuple
from datetime import datetime
from matplotlib import pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    '''
    Lee el fichero de entrada y devuelve una lista de tuplas de tipo RegistroPoblacion.
    '''
    
    with open(ruta_fichero, encoding = 'utf-8') as f: 
        lector = csv.reader(f)
        next(lector)
        
        res = []
        
        for pais, codigo, año, censo in lector:
            censo = int(censo)
            año = int(año)
            #año = datetime.strptime(año, "%Y")
            
            tupla = RegistroPoblacion(pais, codigo, año, censo)
            res.append(tupla)
            
        return res
        
        
    return RegistroPoblacion

def calcula_paises(poblaciones):
    '''
     Toma una lista de tuplas de tipo RegistroPoblacion 
     y devuelve una lista ordenada alfabéticamente con los nombres de los países para los que hay datos.
    '''
    
    paises = set()
    
    for p in poblaciones:
        paises.add(p.pais)
    return sorted(paises)

def filtra_por_pais(poblaciones, nombre_o_codigo):
    '''
     Toma una lista de tuplas de tipo RegistroPoblacion, y el nombre o código de un país, 
     y devuelve una lista de tuplas con los datos del país que se pasa como parámetro (año y censo).
     Importante!: 
     el país puede venir expresado en el parámetro nombre_o_codigo con su nombre completo o con su código.
    '''
    datos_paises = []
    for p in poblaciones:
        if nombre_o_codigo == p.pais or nombre_o_codigo == p.codigo:  
            pais = (p.año, p.censo)
            datos_paises.append(pais)
    return datos_paises

def filtra_por_paises_y_anyo(poblaciones, anyo, paises): 
    '''
    Toma una lista de tuplas de tipo RegistroPoblacion, un año y un conjunto de nombres de países, 
    y devuelve una lista de tuplas (nombre_pais, num_habitantes) 
    con los datos del año pasado como parámetro para los países incluidos en el parámetro paises.
    '''
    res = []
    for p in poblaciones: 
        if p.pais in paises and anyo == anyo:
            datos_año_pasado = (p.pais, p.censo)
            res.append(datos_año_pasado)
    return res

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):

    ''' 
    Toma una lista de tuplas de tipo RegistroPoblacion y el nombre o código de un país,
    y genera una gráfica con la curva de evolución de la población del país dado como parámetro. 
    ¡Importante!: el país puede venir expresado en el parámetro nombre_o_codigo con su nombre 
    completo o con su código.
    '''
    lista_años =[]
    lista_habitantes = []
    for p in poblaciones:
        if nombre_o_codigo == p.pais or nombre_o_codigo == p.codigo:
            lista_años.append(p.año)
            lista_habitantes.append(p.censo)

        
    plt.title("Evolucion de la poblacion")
    plt.plot(lista_años, lista_habitantes)
    plt.show()
    
def muestra_comparativa_paises_anyo(poblaciones, año, paises):
    '''
    toma una lista de tuplas de tipo RegistroPoblacion, 
    un año y un conjunto de nombres de países y genera una
    gráfica de barras con la población de esos países en el año dado 
    como parámetro. Los países se mostrarán en el eje X en orden alfabético
    '''
    lista_paises=[]
    lista_habitantes=[]    

    for p in poblaciones:

        if año == p.año and p.pais in paises:
            lista_paises.append(p.pais)
            lista_habitantes.append(p.censo)

            
    plt.title("Censo de cada país")
    plt.bar(lista_paises, lista_habitantes)
    plt.show()