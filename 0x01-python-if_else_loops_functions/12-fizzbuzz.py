#!/usr/bin/python3
# Author - Edun Damilare

"""Printing from 1 to 100 and check which is Buzz, Fizz or FizzBuzz"""
def fizzbuzz():
  for number in range(1, 101):
      if number % 3 == 0 and number % 5 == 0:
          print("FizzBuzz ", end="")
      elif number % 3 == 0:
          print("Fizz ", end="")
      elif number % 5 == 0:
          print("Buzz ", end="")
      else:
          print("{} ".format(number), end="")
