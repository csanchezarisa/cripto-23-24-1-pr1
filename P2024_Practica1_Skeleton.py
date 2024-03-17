#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import ceil
import numpy as np


# --- IMPLEMENTATION GOES HERE -----------------------------------------------
#  Student helpers (functions, constants, etc.) can be defined here, if needed
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

def list_to_string(list: list[int]) -> str:
    """
    Generates a string using a list of character indexes. These indexes should be based on the valid characters list
    :param list: list containing the characters indexes
    :return: a string that translates each index into a valid char
    """
    message: str = ""

    for i in list:
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

    # --------------------------------

    return ciphertext


def uoc_hill_decipher(message, key):
    """
    EXERCISE 3: Hill decipher
    :message: message to decipher (ciphertext)
    :key: key to use when deciphering the message (as it is returned by 
          uoc_hill_genkey() )
    :return: plaintext corresponding to the ciphertext
    """

    plaintext = ""

    #### IMPLEMENTATION GOES HERE ####




    # --------------------------------

    return plaintext








