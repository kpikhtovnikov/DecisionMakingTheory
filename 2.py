import numpy as np
from cvxopt import matrix, solvers

c = matrix([0, -1, -1, -1, -1, 0, -1, 0, -1], tc='d') #Целевая функция (минусы, потому что решаем задачу максимизации) 

G = matrix([[0, 0.007,  0.006,  0.004, 0.009, 0, 0.003,  0, 0.005],   # Коэффициенты при ограничениях-неравенствах (вида <=)
            [    0,     9, 14,  0,     0,     0,     0,  0,     0],
            [    0,     0,  0, 16,     9,     0,     0,  0,     0],
            [    0,     0,  0,  0,     0,     0,    12,  0,    12],
            [    0,     1,  1, -1,     -1,    0,     0,  0,     0],
            [    0,     1,  1,  0,     0,     0,    -1,  0,    -1],
            [   -1,     0,  0,  0,     0,     0,     0,  0,     0],
            [    0,    -1,  0,  0,     0,     0,     0,  0,     0],
            [    0,     0, -1,  0,     0,     0,     0,  0,     0],
            [    0,     0,  0, -1,     0,     0,     0,  0,     0],
            [    0,     0,  0,  0,    -1,     0,     0,  0,     0],
            [    0,     0,  0,  0,     0,    -1,     0,  0,     0],
            [    0,     0,  0,  0,     0,     0,    -1,  0,     0],
            [    0,     0,  0,  0,     0,     0,     0, -1,     0],
            [    0,     0,  0,  0,     0,     0,     0,  0,    -1]], tc='d')
h = matrix([97,79800,49800,83400,0,0,0,0,0,0,0,0,0,0,0], tc='d')

solution = solvers.lp(c, G.T, h, solver='glpk')
print('Status:', solution['status'])
print('Objective :', solution['primal objective'])
print('x = \n', solution['x'])

print(solution['z'])
dh = matrix([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);     # приращение к вектору правых частей
solution1 = solvers.lp(c, G.T, h + dh, solver='glpk')
print('Status:', solution1['status'])
print('Objective:', -solution1['primal objective'], 'delta:', -solution1['primal objective']-(-solution['primal objective']))
print('x = \n', solution1['x'])
print('z = \n',solution1['z'])
