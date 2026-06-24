from sympy.combinatorics import Permutation
from sympy.combinatorics import SymmetricGroup
from sympy.combinatorics import PermutationGroup

# From SageMath docs: https://doc.sagemath.org/html/en/reference/groups/sage/groups/perm_gps/cubegroup.html

B = Permutation(1,14,48,27)*Permutation(2,12,47,29)*Permutation(3,9,46,32)*Permutation(33,35,40,38)*Permutation(34,37,39,36)

D = Permutation(14,22,30,38)*Permutation(15,23,31,39)*Permutation(16,24,32,40)*Permutation(41,43,48,46)*Permutation(42,45,47,44) # D
F = Permutation(6,25,43,16)*Permutation(7,28,42,13)*Permutation(8,30,41,11)*Permutation(17,19,24,22)*Permutation(18,21,23,20) # F
L = Permutation(1,17,41,40)*Permutation(4,20,44,37)*Permutation(6,22,46,35)*Permutation(9,11,16,14)*Permutation(10,13,15,12) # L
R = Permutation(3,38,43,19)*Permutation(5,36,45,21)*Permutation(8,33,48,24)*Permutation(25,27,32,30)*Permutation(26,29,31,28) # R
U = Permutation(1,3,8,6)*Permutation(2,5,7,4)*Permutation(9,33,25,17)*Permutation(10,34,26,18)*Permutation(11,35,27,19) # U
