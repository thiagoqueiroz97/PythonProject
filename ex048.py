pessoa = []
pessoas = []
continuar = 'S'
menor = maior = 0

while continuar == 'S':

    pessoa.append(str(input("Digite o nome da pessoa: ")))
    pessoa.append(float(input("Digite o peso da pessoa: ")))

    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    continuar = str(input("Deseja continuar? S/N"))

print(f"Ao todo voce registrou {len(pessoas)} pessoas")

print(f'O maior peso foi de {maior} KG. peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor} KG. peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')

