from collections import abc
from sympy.solvers.diophantine.diophantine import base_solution_linear
from random import randint
from numpy import gcd


def encrypt(msg):
    ascii_lst = [ord(c) for c in msg]
    print("\nASCII List: {}".format(ascii_lst))

    a, b = randint(1, 10), randint(1, 10)

    print("\n(a,b)\tASCII\tPoint")
    ab_lst = []
    point_lst = []
    for i in range(len(ascii_lst)):
        while True:
            a, b = randint(1, 10), randint(1, 10)
            if ascii_lst[i] % gcd(a, b) == 0 and base_solution_linear(ascii_lst[i], a, b) != (None, None):
                ab_lst.append((a, b))
                point_lst.append(base_solution_linear(ascii_lst[i], a, b))
                break

        print("({},{})\t{}\t{}".format(
            a, b, ascii_lst[i], base_solution_linear(ascii_lst[i], a, b)))

    print("\n\n")
    return ab_lst, point_lst


def decrypt(ab_lst, point_lst):
    dec = []

    for i in range(len(ab_lst)):
        dec.append(ab_lst[i][0]*point_lst[i][0]+ab_lst[i][1]*point_lst[i][1])

    dec_txt_lst = []

    for i in range(len(dec)):
        dec_txt_lst.append(chr(dec[i]))

    print("Decrypted Text: ")
    print(''.join(map(lambda x: str(x), dec_txt_lst)))


msg = input("Enter message: ")

print("Encrypted message\n")
ab_lst, point_lst = encrypt(msg)

decrypt(ab_lst, point_lst)