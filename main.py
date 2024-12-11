'''
Tiesinio programavimo uždavinys:
min 2x1 - 3x2 - 5x4
    -x1 + x2 - x3 - x4 ≤ 8
    2x1 + 4x2          ≤ 10
               x3 + x4 ≤ 3
                    xi ≥ 0

1. Suprogramuokite simplekso algoritmą tiesinio programavimo uždaviniams.
2. Užrašykite duotą uždavinį matriciniu pavidalu standartine forma.
3. Išspręskite uždavinį suprogramuotu simplekso algoritmu. 
4. Pakeiskite apribojimų dešinės pusės konstantas į a, b ir c - a = 1, b = 5, c = 7. Išspręskite individualų uždavinį suprogramuotu simplekso algoritmu.
5. Palyginkite uždavinių sprendimo rezultatus: minimali tikslo funkcijos reikšmė, optimalus sprendinys ir bazė.
'''
from imports import datetime, np
from scipy.optimize import linprog
from simplex import SimplexSolver
print(f"{datetime.now()}\n")

c = np.array([2, -3, 0, -5])  
A = np.array([
    [-1, 1, -1, -1], 
    [2, 4, 0, 0],
    [0, 0, 1, 1]
])
b = np.array([0, 0, 0])  

print("(b = [8, 10, 3]):")
solver = SimplexSolver(c, A, b)
solution = solver.solve()
print("Simplex Table:")
print(solution['table'])
print(f"Optimal solution x = {solution['x']}")                  
print(f"Objective value = {solution['objective']}\n")

actualAnswer = linprog(c, A_ub=A, b_ub=b, method='simplex')
print(f"Optimal solution x = {actualAnswer.x}")
print(f"Objective value = {actualAnswer.fun}\n")

print("\n(b = [1, 5, 7]):")
b = np.array([1, 5, 7])
solver2 = SimplexSolver(c, A, b)
solution2 = solver2.solve()
print("Simplex Table:")
print(solution2['table'])
print(f"Optimal solution x = {solution2['x']}")                 
print(f"Objective value = {solution2['objective']}\n")

actualAnswer2 = linprog(c, A_ub=A, b_ub=b, method='simplex')
print(f"Optimal solution x = {actualAnswer2.x}")
print(f"Objective value = {actualAnswer2.fun}\n")
