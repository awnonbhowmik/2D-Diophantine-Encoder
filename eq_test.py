from sympy.solvers.diophantine.diophantine import diop_solve
from sympy.solvers.diophantine.diophantine import base_solution_linear
from sympy.abc import x,y
from random import randint
from numpy import gcd

iteration = 0
# while iteration < 10:
#     a, b, c = randint(1, 20), randint(1, 20), randint(1, 20)

#     if c % gcd(a, b) == 0 and base_solution_linear(a, b, c) != (None, None):
#         print("({},{},{}) = {}".format(a, b, c, base_solution_linear(a, b, c)))
#         iteration += 1

print(base_solution_linear(72,3,5))
print(diop_solve(3*x+5*y-72))