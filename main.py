from imports import datetime, np
from simplex import SimplexSolver
print(f"{datetime.now()}\n")

c = np.array([2, -3, 0, -5])  
A = np.array([
    [-1, 1, -1, -1], 
    [2, 4, 0, 0],
    [0, 0, 1, 1]
])
b = np.array([8, 10, 3])  

print("(b = [8, 10, 3]):")
solver = SimplexSolver(c, A, b)
solution = solver.solve()
print("Simplex Table:")
print(solution['table'])
print(f"Optimal solution x = {solution['x']}")                  
print(f"Objective value = {solution['objective']}\n")
print("\n(b = [1, 5, 7]):")
b = np.array([1, 5, 7])
solver2 = SimplexSolver(c, A, b)
solution2 = solver2.solve()
print("Simplex Table:")
print(solution2['table'])
print(f"Optimal solution x = {solution2['x']}")                 
print(f"Objective value = {solution2['objective']}\n")