"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
data_list = []
with open("./data.csv", "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter="\t")
    for row in reader_variable:
        data_list.append(row)
#print("--------------------------------------------------")

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    result = 0
    for number in data_list:
        result += int(number[1])
    
    return result



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    final_list = []
    letter_counts = {}
    
    for row in data_list:
        if row[0] in letter_counts:
            letter_counts[row[0]] += 1
        else:
            letter_counts[row[0]] = 1

    for letter, count in letter_counts.items():
        final_list.append((letter, count))
    final_list.sort(key=lambda x: x[0])
    
    return final_list

pregunta_02()

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    sum_dict = {}
    final_list = []

    for row in data_list:
        if row[0] in sum_dict:
            sum_dict[row[0]] += int(row[1])
        else:
            sum_dict[row[0]] = int(row[1])

    for letter, sum in sum_dict.items():
        final_list.append((letter, sum))
    final_list.sort(key=lambda x: x[0])
    

    return final_list


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    month_dict = {}
    final_list = []

    for row in data_list:
        month = row[2].split("-")[1]
        if month in month_dict:
            month_dict[month] += 1
        else:
            month_dict[month] = 1

    for month, count in month_dict.items():
        final_list.append((month, count))
    final_list.sort(key=lambda x: x[0])
    
    return final_list




def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    final_list = []
    letter_dict = {}
    for row in data_list:
        if row[0] in letter_dict:
            letter_dict[row[0]].append(int(row[1]))
        else:
            letter_dict[row[0]] = [int(row[1])]

    for letter, values in letter_dict.items():
        final_list.append((letter, max(values), min(values)))
    final_list.sort(key=lambda x: x[0])
    

    return final_list



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    key_dict = {}
    final_list = []

    for row in data_list:
        key_list = row[4].split(",")
        for key in key_list:
            if key.split(":")[0] in key_dict:
                key_dict[key.split(":")[0]].append(int(key.split(":")[1]))
            else:
                key_dict[key.split(":")[0]] = [int(key.split(":")[1])]

    for key, values in key_dict.items():
        final_list.append((key, min(values), max(values)))
    final_list.sort(key=lambda x: x[0])
    

    return final_list


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    number_dict = {}
    final_list = []

    for row in data_list:
        if row[1] in number_dict:
            number_dict[row[1]].append(row[0])
        else:
            number_dict[row[1]] = [row[0]]

    for number, letters in number_dict.items():
        final_list.append((int(number), letters))
    final_list.sort(key=lambda x: x[0])

    return final_list




def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data_list = pregunta_07()
    final_list = []
    for row in data_list:
        unique_letters = []
        [unique_letters.append(x) for x in row[1] if x not in unique_letters]
        unique_letters.sort()
        final_list.append((row[0], unique_letters))
    return final_list



def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    letter_dict = {}
    
    for row in data_list:
        key_list = row[4].split(",")
        for key in key_list:
            if key.split(":")[0] in letter_dict:
                letter_dict[key.split(":")[0]] += 1
            else:
                letter_dict[key.split(":")[0]] = 1

    letter_dict = {key: letter_dict[key] for key in sorted(letter_dict.keys())}

    return letter_dict


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    final_list = []
    for row in data_list:
        final_list.append((row[0], len(row[3].split(",")), len(row[4].split(","))))

    return final_list


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    letter_dict = {}
    for row in data_list:
        letter_list = row[3].split(",")
        for letter in letter_list:
            if letter in letter_dict:
                letter_dict[letter] += int(row[1])
            else: 
                letter_dict[letter] = int(row[1])
    letter_dict = {key: letter_dict[key] for key in sorted(letter_dict.keys())}                
    return letter_dict

pregunta_11()


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    letter_dict = {}
    for row in data_list:
        number_sum = row[4].split(",")
        number_sum = sum([int(x.split(":")[1]) for x in number_sum])
        if row[0] in letter_dict:
            letter_dict[row[0]] += number_sum
        else:
            letter_dict[row[0]] = number_sum
    letter_dict = {key: letter_dict[key] for key in sorted(letter_dict.keys())}


    return letter_dict

