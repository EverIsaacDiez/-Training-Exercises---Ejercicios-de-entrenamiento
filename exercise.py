lista_personas = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Fito', 'Garcia', 23),
    ('33333333', 'Leo', 'Peralta', 26),
    ('44444444', 'Bruno', 'Mac', 25),
    ('55555555', 'Nico', 'Zaoral', 27),
    ('44444444', 'Bruno', 'Mac', 25),
]



""" El metodo debe devolver una lista con las edades ordenadas de menor a mayor"""
def ordenar(lista_personas):
    edades_desordenadas = []
    """ Se guardan las edades desordenadas """
    for i in lista_personas:
        edades_desordenadas = edades_desordenadas + [i[3]]

    edades_ordenadas = []
    """ Se agrega el minimo a edades_ordenadas y se modifican como modo de borrar en edades_desordenadas """
    for i in edades_desordenadas:
        minimo = min(edades_desordenadas)
        edades_ordenadas = edades_ordenadas + [minimo]
        for j in range(0,len(edades_desordenadas)):
            if (edades_desordenadas[j] == minimo):
                edades_desordenadas[j] = max(edades_desordenadas)
                break
    
    return edades_ordenadas

"""
OTRA FORMA PODIA SER CON QUICK SORT
def ordenar(lista_personas):
    edades_desordenadas = []
    # Se guardan las edades desordenadas
    for i in lista_personas:
        edades_desordenadas = edades_desordenadas + [i[3]]

    edades_ordenadas = quick_sort(edades_desordenadas)
    
    return edades_ordenadas
"""



""" Hacer un diccionario que tenga como claves los “dni” y como valores tuplas con nombre, apellido y edad """
def convertir_a_diccionario(lista_personas):
    diccionario = {}
    for i in range(0, len(lista_personas)):
        diccionario[lista_personas[i][0]] = (lista_personas[i][1],lista_personas[i][2],lista_personas[i][3])
    return diccionario



""" Para la 'lista_personas' devuelve la edad de la persona que tenga el dni definido.
    Tip: intentar usar el método convertir_a_diccionario"""
def devolver_edad(lista_personas, dni):
    diccionario = convertir_a_diccionario(lista_personas)
    edad = diccionario[dni][2]
    return edad



""" El metodo debe devolver los elementos unicos """
def eliminar_repetidos(lista_personas):
    unicos = []
    for i in lista_personas:
        if ((i in unicos) == False):
            unicos = unicos + [i]
    return unicos



""" Devolver dos listas
    * lista 1: mayores de 25 (incluido)
    * lista 2: menores de 25
"""
def separar_por_edad(lista_personas):
    lista_mayores = []
    lista_menores = []
    EDAD = 25
    
    for i in lista_personas:
        if (i[3] >= EDAD):
            lista_mayores = lista_mayores + [i]
        else:
            lista_menores = lista_menores + [i]
            
    return lista_mayores, lista_menores



""" Implementar obtener el promedio de la lista de números que se recibe.
    Capturar con un try/except la excepción de dividir por cero"""
def obtener_promedio(lista):
    try:
        return sum(lista)/len(lista)
    except ZeroDivisionError:
        print("La lista está vacía, intentá agregando elementos.")
        


def main():
    """ Este metodo no debe modificarse y es solo a fines de probar el codigo """
    print('Resultados:\n')
    print(' * Edades ordenadas: %s\n' % ordenar(lista_personas))
    print(' * Elementos como diccionario: %s\n' % convertir_a_diccionario(lista_personas))
    print(' * La edad para dni 55555555 es: %s\n' % devolver_edad(lista_personas, '55555555'))
    print(' * Elementos únicos: %s\n' % eliminar_repetidos(lista_personas))
    print(' * Los mayores de 25 son: %s\n' % separar_por_edad(lista_personas)[0])
    print(' * Los menores de 25 son: %s\n' % separar_por_edad(lista_personas)[1])
    print(' * El promedio de las edades es: %s\n' % obtener_promedio(ordenar(lista_personas)))
    print(' * El promedio de una lista vacía es: %s\n' % obtener_promedio([]))

