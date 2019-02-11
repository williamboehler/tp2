# -*- coding: utf-8 -*-
from unittest import TestCase
from unittest.mock import patch
from solver import ProblemSolver


def mock_convert(number):
    # (2a) Du coup, on n'a plus du tout un fonctionnel de FizzBuzz.
    # Ici, au lieu de renvoyer le nombre, 'Fizz', 'Buzz' ou 'Fizzbuzz',
    # notre méthode mockée renvoie le carré du nombre dans tous les cas.
    # Je l'ai fait exprès, afin de tenter de mieux vous faire comprendre que,
    # dans ce module de tests, on ne cherche pas à tester le fonctionnement
    # de l'objet FizzBuzz, qui est déjà testé dans le module test_fizzbuzz.py.
    # Ici, on cherche à tester l'objet ProblemSolver en lui même,
    # indépendamment de tout autre objet qui pourrait être buggé.
    return str(number * number)


def mock_display(string):
    # (3b) La spécification de FizzBuzz nous dit d'_afficher_ le résultat.
    # Cependant, un affichage console n'est pas aisément testable.
    # En conséquence, dans un cadre de tests unitaires, plutôt que d'afficher
    # la chaîne de caractères résultat, nous choisissons de la retourner,
    # afin de pouvoir la comparer à ce que nous nous attendons à avoir.
    return string


class ProblemSolverTest(TestCase):

    def setUp(self):
        # (2a) On crée un "faux objet" (appelé un mock)
        # afin de simuler un objet de type Int2String.
        # Int2String étant en effet une classe abstraite,
        # on ne pourrait l'instancier sans cela ;
        # on _pourrait_ utiliser un objet réel de type FizzBuzz,
        # mais si on constatait des erreurs en testant ProblemSolver,
        # qu'est-ce qui pourrait nous dire si le bug est dans
        # la classe ProblemSolver elle-même, ou dans FizzBuzz ?
        # Tester les objets indépendamment les uns des autres grâce aux mocks
        # nous permet de répondre à ce problème.
        with patch('solver.Int2String') as mock:
            mock.convert = mock_convert
            self.converter = mock
        # (3a) Idem: on utilise un mock qui va se comporter comme un Displayer.
        with patch('solver.Displayer') as mock:
            mock.display = mock_display
            self.displayer = mock
        # (1) Ce ProblemSolver, c'est l'objet qu'on veut tester en isolation
        self.solver = ProblemSolver(self.converter, self.displayer)

    ''' (4)
    Les trois méthodes de test suivantes suivent chacune les 3 mêmes étapes :
    1- GIVEN .. la situation initiale décrite dans la méthode setUp ...
    2- WHEN ... la méthode solver.solve est appelée
    3- THEN ... on compare le résultat observé (ie. le retour de solver.solve)
                au résultat attendu (prédéfini dans chaque test)
    Ce schéma en 3 étapes est habituel, et vise à maximiser l'atomicité,
    la clarté et la concision de chaque test.
    '''
    def test_display_1_time(self):
        self.solver.solve(1)
        observed_result = ':'.join(self.solver.results)
        expected_result = '1'
        self.assertEqual(observed_result, expected_result)

    def test_display_3_times(self):
        self.solver.solve(3)
        observed_result = ':'.join(self.solver.results)
        expected_result = '1:4:9'
        self.assertEqual(observed_result, expected_result)

    def test_display_10_times(self):
        self.solver.solve(10)
        observed_result = ':'.join(self.solver.results)
        expected_result = '1:4:9:16:25:36:49:64:81:100'
        self.assertEqual(observed_result, expected_result)
