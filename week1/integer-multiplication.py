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

def mult(a,b):
  # a and b are two lists of digits, same length
  if len(a) == 1 and len(b) == 1:
    return a[0]*b[0]
  if len(a) == 0 or len(b) == 0:
    return 0
  
  l = len(a)
  mid = l/2
  aleft = a[:mid]
  aright = a[mid:]
  bleft = b[:mid]
  bright = b[mid:]
  
  albl = mult(aleft, bleft)
  albr = mult(aleft, bright)
  arbl = mult(aright, bleft)
  arbr = mult(aright, bright)
  
  term1 = 10**(2*(l-1)) * albl
  term2 = 10**(l-1) * albr
  term3 = 10**(l-1) * arbl
  term4 = arbr
  
  return term1 + term2 + term3 + term4

num1, num2 = raw_input().split(' ')
digits1 = arithdigits(int(num1))
digits2 = arithdigits(int(num2))
print mult(digits1, digits2)
