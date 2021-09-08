# Prueba técnica realizada por Diego Antivil Curaqueo


# Importaciones
# Se utilizarán 2 librerías, por un lado "re" el cual se utilizara para
# realizar operaciones de expresiones regulares. Para este caso en particular
# la utilizaremos para extraer los valores de los interiores de los parentesis
# en caso de que existan.
# La segunda importación es "product" de la librería "itertools". Product sirve
# para realizar el producto cartesiano de al menos 2 conjuntos de elementos.
# Para este caso en particular lo utilizaremos para combinar y generar las
# posibles palabras que pudieran calzar con el diccionario de palabras inicial.
import re
from itertools import product


# Funciones para obtención de datos
# La función "get_words" retornará un listado con las palabras conocidas del
# lenguaje alienígena.
def get_words() -> list:
    return ["abc", "bca", "dac", "dbc", "cba"]


# La función "get_cases" retornará un listado con los casos de prueba.
def get_cases() -> list:
    return ["(ab)(bc)(ca)", "abc", "(abc)(abc)(abc)", "(xyz)(bc)"]


# Funciones auxiliares

# La funcion "extract_paretheses" utiliza regex para extraer los parentesis y
# guardar los valores en una lista.
# Por ejemplo: '(ab)b(bc)' => ['ab', 'b', 'bc']
# Sin embargo, exite un inconveniente y es que dentro de la lista resultante
# podrían existir vacios  es decir: '(ab)b(bc)' => ['', 'ab', 'b', '', 'bc']
# por ello se recorre la lista para quitar estos vacios. Finalmente se
# individualizan las opciones combinables para crear una matriz,
# para el ejemplo, el resultado final sería: [['a', 'b'], ['b'], ['b', 'c']]
def extract_paretheses(value: str) -> list:
    return [
        [char for char in token]
        for token in re.split(r'\((.*?)\)', value)
        if token != ''
    ]


# Esta funcion se utiliza para definir las posibles combinacones que se puedan
# dar para un conjunto de patrones. Para ello se utiliza "product" para generar
# una combinación de elementos siguiendo el principio del producto cartesiano.
# Ejemplo: [['a'], ['b', 'c'], ['d']] => [['a', 'b', 'd']['a', 'c', 'd']]
# Finalmente para cada vector se unen nuevamente sus caracteres para crear la
# palabra, es decir: [['a', 'b', 'd']['a', 'c', 'd']] => ['abd', 'acd'].
def combinations(case: list) -> list:
    return [
        ''.join(combination)
        for combination in list(product(*case))
    ]


# Con el objetivo de crear código escalable, todos los casos de prueba pasarán
# por el proceso de combinación, para ello todos los casos de pruebas deben
# tener una estructura uniforme, siendo esta estructura como en los siguientes
# ejemplos:
# 'abc' => [['a'], ['b'], ['c']]
# '(ab)(bc)(dc)' => [['a', 'b'], ['b', 'c'], ['d', 'c']]
# El resultado de esta función es una lista de listados (matriz).
def get_cases_with_matrix(cases: list) -> list:
    return [
        [[char for char in token] for token in case]
        if not re.search(r'\((.*?)\)', case)
        else extract_paretheses(case)

        for case in cases
    ]


# Esta función responderá con un listado donde cada valor de cada indice
# corresponde a la cantidad de combinaciones que acertaron con alguna de las
# palabras del listado de palabras alienígenas.
def get_success_cases(words: list, cases: list) -> list:
    # A partir del listado original de casos de prueba se crea el listado que
    # se utilizará a lo largo de la ejecución.
    new_list_cases = get_cases_with_matrix(cases)
    results = list()
    for case in new_list_cases:
        combinations_of_case = combinations(case)
        # "success_words" es el listado de palabras que existen en el idioma
        # alienígena y que se generaron a partir de la combinación de cada caso
        # de prueba.
        success_words = [
            combination
            for combination in combinations_of_case
            if combination in words
        ]
        # Solo por comodidad la respuesta será la cantidad de palabras
        # generadas que coinciden con el listado de palabras alienigenas
        # conocidas.
        results.append(len(success_words))
    return results


if __name__ == "__main__":
    words = get_words()
    cases = get_cases()

    results = get_success_cases(words, cases)
    for i in range(len(results)):
        print(f"Case #{i+1}: {results[i]}")
