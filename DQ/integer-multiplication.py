def arithdigits(num):
  # Returns a list containing the digits in a number, from left to right
  digits = []
  while(num):
    digits.insert(0, num % 10)
    num = num // 10
  return digits

def mult(a,b):
  if len(a) == 1 and len(b) == 1:
    return a[0]*b[0]
  if len(a) == 0 or len(b) == 0:
    return 0

  alen = len(a)
  blen = len(b)
  amid = alen/2
  bmid = blen/2
  aleft = a[:amid]
  aright = a[amid:]
  bleft = b[:bmid]
  bright = b[bmid:]

  albl = mult(aleft, bleft)
  albr = mult(aleft, bright)
  arbl = mult(aright, bleft)
  arbr = mult(aright, bright)

  term1 = 10**(alen-len(aleft)+blen-len(bleft)) * albl
  term2 = 10**(alen-len(aleft)) * albr
  term3 = 10**(blen-len(bleft)) * arbl
  term4 = arbr

  return term1 + term2 + term3 + term4

num1, num2 = raw_input().split(' ')
digits1 = arithdigits(int(num1))
digits2 = arithdigits(int(num2))
print mult(digits1, digits2)
