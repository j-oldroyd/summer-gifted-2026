from sympy.combinatorics import Permutation
from sympy.combinatorics import SymmetricGroup
from sympy.combinatorics import PermutationGroup

G = SymmetricGroup(3)

print('Cayley table of S3')
print('='*30)
print('\t|\t'.join([str(perm) for perm in G.elements]), '|')
print('='*52)

table = []
i,j = 0,0
for sigma in G.elements:
    for rho in G.elements:
        row.append(str(sigma*rho))
        j += 1
    row.append('\n')
    # row.insert(0, '||')
    row.insert(0, str(sigma))
    # table.append(row)
    print('\t|\t'.join(row))
    row = []
    i += 1
