import numpy as np

print("=== MATRICES SIMÉTRICAS Y ANTISIMÉTRICAS ===")

# 🔹 SIMÉTRICAS

A = np.array([[1, 2], [2, 1]])
print("\n=== EJERCICIO 1 (SIMÉTRICA) ===")
print("Matriz:\n", A)

print("\nPaso 1: Transpuesta")
print(A.T)

print("\nPaso 2: Comparar A == A^T")
print("Resultado:", np.all(A == A.T))


B = np.array([[3, 0], [0, 3]])
print("\n=== EJERCICIO 2 (SIMÉTRICA) ===")
print("Transpuesta:\n", B.T)
print("Resultado:", np.all(B == B.T))


C = np.array([[5, -1], [-1, 5]])
print("\n=== EJERCICIO 3 (SIMÉTRICA) ===")
print("Transpuesta:\n", C.T)
print("Resultado:", np.all(C == C.T))


# 🔹 ANTISIMÉTRICAS

D = np.array([[0, 2], [-2, 0]])
print("\n=== EJERCICIO 4 (ANTISIMÉTRICA) ===")
print("Transpuesta:\n", D.T)

print("\nPaso: verificar A = -A^T")
print("-A^T:\n", -D.T)
print("Resultado:", np.all(D == -D.T))


E = np.array([[0, -3], [3, 0]])
print("\n=== EJERCICIO 5 (ANTISIMÉTRICA) ===")
print("-A^T:\n", -E.T)
print("Resultado:", np.all(E == -E.T))


F = np.array([[0, 1], [-1, 0]])
print("\n=== EJERCICIO 6 (ANTISIMÉTRICA) ===")
print("-A^T:\n", -F.T)
print("Resultado:", np.all(F == -F.T))
