primeira_linha = input().split()

N = int(primeira_linha[0])
K = int(primeira_linha[1])
U = int(primeira_linha[2])
cartelas = []

for i in range(N):
    cartela = input().split()
    cartelas.append(cartela)

numeros_sorteados = input().split()

vencedores = []
ind = 0
for numero in numeros_sorteados:
    aux = 0
    for cartela in cartelas:
        if not cartela and ind == reg:
            vencedores.append(aux)
            reg = ind
            pass
        elif numero in cartela:
            cartela.remove(numero)
        aux += 1
    ind += 1
    if not vencedores:
        reg = ind

vencedores.sort()

for vencedor in vencedores:
    vencedor += 1
    print(vencedor, end=' ')

