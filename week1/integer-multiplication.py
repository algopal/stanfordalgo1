"""
Implementation of recursive (divide & conquer) integer multiplication
"""

def arithdigits(num):
  # Returns a list containing the digits in a number, from left to right
  digits = []
  while(num):
    digits.insert(0, num % 10)
    num = num // 10
  return digits
