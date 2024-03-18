#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import ceil

import numpy as np
from sympy import Matrix

# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed
PADDING_CHAR: str = 'X'
VALID_CHARS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,:? "

def get_random_number() -> int:
    """
    Generates a random integer number and returns it.
    This number is limited to the number of valid characters
    :return: Random integer number
    """
    return np.random.randint(len(VALID_CHARS))

def get_character_position(character: str) -> int:
    """
    Returns the index of the character based on valid chars list
    :param character: character which to find the position
    :return: the index of the character based on the valid chars list
    """
    return VALID_CHARS.find(character)


def string_to_index_list(string: str) -> list[int]:
    """
    Converts a string into a list of indexes based on valid characters list
    :param string: message to be converted to list
    :return: index list based on valid characters list
    """
    index_list: list[int] = []

    for c in string:
        index: int = get_character_position(c)
        index_list.append(index)

    return index_list


def index_list_to_string(index_list: list[int]) -> str:
    """
    Generates a string using a list of character indexes. These indexes should be based on the valid characters list
    :param index_list: list containing the characters indexes
    :return: a string that translates each index into a valid char
    """
    message: str = ""

    for i in index_list:
        message += VALID_CHARS[i]

    return message
# ----------------------------------------------------------------------------





def uoc_hill_genkey(size: int):
    """
    EXERCISE 1: Hill Key Generation
    :size: matrix size
    :return: size x size matrix containing the key
    """

    matrix: list[list[int]] = []

    # --- IMPLEMENTATION GOES HERE ---

    # Generamos tantas listas como indique size, con el mismo número de elementos
    # y las vamos añadiendo a matrix
    for i in range(size):
        row: list[int] = []
        for j in range(size):
            row.append(get_random_number())
        matrix.append(row)

    # --------------------------------

    return matrix



def uoc_hill_cipher(message: str, key: list[list[int]]):
    """
    EXERCISE 2: Hill cipher
    :message: message to cipher (plaintext)
    :key: key to use when ciphering the message (as it is returned by 
          uoc_hill_genkey() )
    :return: ciphered text
    """

    ciphertext = ""

    #### IMPLEMENTATION GOES HERE ####
    key_matrix = np.array(key)
    key_size = len(key)  # Tamaño de la clave empleada
    reps: int = ceil(len(message) / key_size)  # Calcula cuantas veces se debera ejecutar el cifrado para poder
    # aplicarlo en caso de tener un mensaje más largo que la clave

    for i in range(reps):

        # Dividimos el mensaje porciones que puedan ser encriptadas con el tamaño de la clave
        substr: str = message[(key_size * i):(key_size * i + key_size)]
        # Calculamos cuántas 'X' habrá que añadir si el tamaño de la porción es menor al de la clave
        exes: str = PADDING_CHAR * (key_size - len(substr))
        substr += exes

        # Bucamos el índice de cada caracter en base a la lista de caracteres válidos
        char_index: list[int] = string_to_index_list(substr)

        # Realizamos la operación de Hill con las matrices
        result_matrix = key_matrix.dot(np.array(char_index))
        result_matrix = np.mod(result_matrix, len(VALID_CHARS))

        # Traducimos la matriz resultante en mensaje cifrado
        ciphertext += index_list_to_string(result_matrix)

    # --------------------------------

    return ciphertext


def uoc_hill_decipher(message: str, key: list[list[int]]):
    """
    EXERCISE 3: Hill decipher
    :message: message to decipher (ciphertext)
    :key: key to use when deciphering the message (as it is returned by 
          uoc_hill_genkey() )
    :return: plaintext corresponding to the ciphertext
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####
    key_size: int = len(key)
    reps: int = ceil(len(message) / key_size)  # Calcula cuantas veces se debera ejecutar el cifrado para poder

    # Calculamos la matriz inversa de key
    key_matrix = Matrix(key)
    inv_key_matrix = key_matrix.inv_mod(len(VALID_CHARS))

    for i in range(reps):
        # Dividimos el mensaje porciones que puedan ser desencriptadas con el tamaño de la clave
        substr: str = message[(key_size * i):(key_size * i + key_size)]

        # Bucamos el índice de cada caracter en base a la lista de caracteres válidos
        char_index: list[int] = string_to_index_list(substr)

        # Realizamos la operación de Hill con las matrices
        result_matrix = np.dot(inv_key_matrix, np.array(char_index))
        result_matrix = np.mod(result_matrix, len(VALID_CHARS))

        # Traducimos la matriz resultante en mensaje descifrado
        plaintext += index_list_to_string(result_matrix)

    # Eliminamos el padding de 'X'
    plaintext = plaintext.rstrip(PADDING_CHAR)
    # --------------------------------

    return plaintext








