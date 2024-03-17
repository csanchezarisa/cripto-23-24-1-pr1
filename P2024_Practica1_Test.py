#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import numpy as np

from P2024_Practica1_Skeleton import *


class Test_1_1_KeyGen(unittest.TestCase):

    def test_1(self):
        key = uoc_hill_genkey(2)
        self.assertEqual(len(key), 2)
        self.assertEqual(len(key[0]), 2)
        self.assertLessEqual(np.max(key), 40)
        self.assertGreaterEqual(np.min(key), 0)

    def test_2(self):
        key = uoc_hill_genkey(3)
        self.assertEqual(len(key), 3)
        self.assertEqual(len(key[0]), 3)
        self.assertLessEqual(np.max(key), 40)
        self.assertGreaterEqual(np.min(key), 0)

    def test_3(self):
        key = uoc_hill_genkey(4)
        self.assertEqual(len(key), 4)
        self.assertEqual(len(key[0]), 4)
        self.assertLessEqual(np.max(key), 40)
        self.assertGreaterEqual(np.min(key), 0)

    def test_4(self):
        key = uoc_hill_genkey(5)
        self.assertEqual(len(key), 5)
        self.assertEqual(len(key[0]), 5)
        self.assertLessEqual(np.max(key), 40)
        self.assertGreaterEqual(np.min(key), 0)



class Test_1_2_Cipher(unittest.TestCase):

    def test_1(self):
        key = [[6, 28, 5], [0, 37, 20], [35, 6, 39]]
        plaintext = "SECRET TEXT"
        ciphertext = "ZY9W.HNE4GPM"
        ciphertext_new = uoc_hill_cipher(plaintext, key)
        self.assertEqual(ciphertext_new, ciphertext)

    def test_2(self):
        key = [[13, 17], [10, 16]]
        plaintext = "AB"
        ciphertext = "RQ"
        ciphertext_new = uoc_hill_cipher(plaintext, key)
        self.assertEqual(ciphertext_new, ciphertext)

    def test_3(self):
        key = [[3, 16, 7], [31, 19, 8], [25, 20, 25]]
        plaintext = "CBA"
        ciphertext = "W 3"
        ciphertext_new = uoc_hill_cipher(plaintext, key)
        self.assertEqual(ciphertext_new, ciphertext)

    def test_4(self):
        key = [[40, 29, 28], [31, 19, 13], [12, 17, 30]]
        plaintext = "HELLO WORLD."
        ciphertext = "H05?UM V2SF7"
        ciphertext_new = uoc_hill_cipher(plaintext, key)
        self.assertEqual(ciphertext_new, ciphertext)

    def test_5(self):
        key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
        plaintext = "ONE, TWO OR THREE?"
        ciphertext = "VJ03HX,OH?5G7OVE6IID"
        ciphertext_new = uoc_hill_cipher(plaintext, key)
        self.assertEqual(ciphertext_new, ciphertext)

    def test_6(self):
        key = [[13, 17], [10, 16]]
        plaintext = "THIS IS MY SECRET"
        ciphertext = ":PA A.MA5MG6E5C3XZ"
        ciphertext_new = uoc_hill_cipher(plaintext, key)
        self.assertEqual(ciphertext_new, ciphertext)


class Test_1_3_Decipher(unittest.TestCase):

    def test_1(self):
        key = [[6, 28, 5], [0, 37, 20], [35, 6, 39]]
        plaintext = "SECRET TEXT"
        ciphertext = "ZY9W.HNE4GPM"
        plaintext_new = uoc_hill_decipher(ciphertext, key)
        self.assertEqual(plaintext_new, plaintext)

    def test_2(self):
        key = [[13, 17], [10, 16]]
        plaintext = "AB"
        ciphertext = "RQ"
        plaintext_new = uoc_hill_decipher(ciphertext, key)
        self.assertEqual(plaintext_new, plaintext)

    def test_3(self):
        key = [[3, 16, 7], [31, 19, 8], [25, 20, 25]]
        plaintext = "CBA"
        ciphertext = "W 3"
        plaintext_new = uoc_hill_decipher(ciphertext, key)
        self.assertEqual(plaintext_new, plaintext)

    def test_4(self):
        key = [[40, 29, 28], [31, 19, 13], [12, 17, 30]]
        plaintext = "HELLO WORLD."
        ciphertext = "H05?UM V2SF7"
        plaintext_new = uoc_hill_decipher(ciphertext, key)
        self.assertEqual(plaintext_new, plaintext)

    def test_5(self):
        key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
        plaintext = "ONE, TWO OR THREE?"
        ciphertext = "VJ03HX,OH?5G7OVE6IID"
        plaintext_new = uoc_hill_decipher(ciphertext, key)
        self.assertEqual(plaintext_new, plaintext)

    def test_6(self):
        key = [[13, 17], [10, 16]]
        plaintext = "THIS IS MY SECRET"
        ciphertext = ":PA A.MA5MG6E5C3XZ"
        plaintext_new = uoc_hill_decipher(ciphertext, key)
        self.assertEqual(plaintext_new, plaintext)




if __name__ == '__main__':

    # create a suite with all tests
    test_classes_to_run = [Test_1_1_KeyGen, Test_1_2_Cipher, Test_1_3_Decipher]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    all_tests_suite = unittest.TestSuite(suites_list)

    # run the test suite with high verbosity
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(all_tests_suite)



