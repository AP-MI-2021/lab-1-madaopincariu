'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
    """
    :param n: o valoare intreaga
    :return: True, daca n este prim, respectiv False in caz contrar
    """
    if n < 2:
      return False
    for i in range(2, n// 2 + 1):
      if n % i == 0:
        return False
    return True

'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  '''
  :param lst: lista de numere naturale
  :return: produsul numerelor din lista
  '''
  product = 1
  for x in lst:
    product = product * x
  return product

'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  '''
  :param x: primul numar
  :param y: al doilea numar
  :return: cmmdc al celor 2 numere
  '''
  while x != y:
    if x > y:
      x = x - y
    else:
      y = y - x
  return x

'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
 '''
 :param x: primul numar
 :param y: al doilea numar
 :return: cmmdc al celor 2 numere
 '''
 while y != 0:
   z = x % y
   x = y
   y = z
 return x

def main():
    print(is_prime(9))
    print(get_product([1, 2, 3, 5, 4]))
    print(get_cmmdc_v1(24, 60))
    print(get_cmmdc_v2(24, 60))

if __name__ == '__main__':
  main()
