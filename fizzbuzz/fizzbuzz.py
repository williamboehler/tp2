# -*- coding: utf-8 -*-
from solver import Int2String


class FizzBuzz(Int2String):

    def convert(self, number):
        is_fizz = not number % 3
        is_buzz = not number % 5

        if is_fizz and is_buzz:
            return 'FizzBuzz'
        elif is_fizz:
            return 'Fizz'
        elif is_buzz:
            return 'Buzz'
        return str(number)
