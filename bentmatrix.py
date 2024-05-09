def dobrar_matriz(matriz, n):
    matriz_dobrada = [[0 for _ in range(n // 2)] for _ in range(n // 2)]
    for i in range(n // 2):
        for j in range(n // 2):
            matriz_dobrada[i][j] = matriz[i][j] + matriz[n - i - 1][j] + matriz[i][n - j - 1] + matriz[n - i - 1][n - j - 1]
    return matriz_dobrada
n = int(input())
matriz = []
for _ in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)
resultado = dobrar_matriz(matriz, n)
for linha in resultado:
    print(*linha)