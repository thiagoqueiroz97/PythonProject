numeros = ('um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n = int(input("Digite aqui o numero que deseja ver por inteiro: "))

while n > 20:
    n = int(input("Tente novamente. Digite aqui o numero que deseja ver por inteiro: "))

print(numeros[n-1])