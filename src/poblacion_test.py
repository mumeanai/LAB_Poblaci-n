from poblacion import *

def test_lee_poblacion(datos):
    print("Probando la funcion lee_poblacion: ")
    datos = lee_poblaciones("data/population.csv")
    print("Primer elemento:", datos[0])
    print("Segundo elemento:", datos[1])
    print("Tercer elemento:", datos[2])

def test_calcula_paises(datos):
    print("Probando la funcion calcula_paises: ")
    print("Los paises para los que hay datos son:")
    print(calcula_paises(datos))  
    
def test_filtra_por_pais(datos):  
    print("Probando la funcion filtra_por_pais: ")
    print("Los datos que hay para este pais son:")
    print(filtra_por_pais(datos, "Spain"))
    
def test_muestra_evolucion_poblacion(datos):    
    print("Probando la funcion muestra_evolucion_poblacion ")
    print("La gráfica obtenida es:")
    print(muestra_evolucion_poblacion(datos, "Spain"))
    


if __name__== "__main__":
    datos = lee_poblaciones("data/population.csv")
    test_lee_poblacion(datos)
    test_calcula_paises(datos)
    test_filtra_por_pais(datos)
    