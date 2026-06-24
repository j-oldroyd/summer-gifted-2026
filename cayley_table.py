from sympy.combinatorics import Permutation
from sympy.combinatorics import SymmetricGroup


S3 = SymmetricGroup(3)


# Taken from https://www.math.uchicago.edu/~may/VIGRE/VIGRE2009/REUPapers/Provenza.pdf
L = Permutation(1, 41, 29, 33)*Permutation(7, 47, 27, 39)* Permutation(8, 48, 28, 40)*Permutation(13, 15, 9, 11)*Permutation(12, 10, 14, 16)

R = Permutation(5, 37, 25, 45)*Permutation(3, 35, 31, 43)* Permutation(3, 36, 32, 44)*Permutation(17, 19, 21, 23)*Permutation(24, 18, 20, 22)

F = Permutation(7, 23, 31, 15)*Permutation(5, 21, 29, 13)* Permutation(6, 22, 30, 14)*Permutation(41, 43, 45, 47)*Permutation(42, 44, 46, 48)

B = Permutation(1, 9, 25, 17)*Permutation(11, 27, 19, 3)*Permutation(2, 10, 26, 18)*Permutation(39, 33, 35, 37)*Permutation(38, 40, 34, 36)

U = Permutation(1, 3, 5, 7)*Permutation(2, 4, 6, 8)*Permutation(39, 17, 43, 13)*Permutation(37, 23, 41, 11)*Permutation(12, 38, 24, 42)

D = Permutation(19, 33, 15, 45)*Permutation(21, 35, 9, 47)*Permutation(20, 34, 16, 46)*Permutation(25, 27, 29, 31)*Permutation(26, 28, 30, 32)
