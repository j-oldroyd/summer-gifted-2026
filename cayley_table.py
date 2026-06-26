from sympy.combinatorics import Permutation
from sympy.combinatorics import SymmetricGroup
from sympy.combinatorics import PermutationGroup
from sympy import TableForm

G = SymmetricGroup(3)

print('Cayley table of S3')
print('='*18)

table = []
row = []
i,j = 0,0
for sigma in G.elements:
    for rho in G.elements:
        row.append(sigma*rho)

    row.insert(0, sigma)
    table.append(row)
    row = []

table.insert(0, [perm for perm in G.elements])
table[0].insert(0, '')

TableForm(table)
