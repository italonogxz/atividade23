# Exercício Python 23: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

for n in range(1, 500, 3):
    print(n)
    n = int(input("informe um numero entre 1 e 500: "))
    if n % 3 == 0:
        print(f"o numero informado{n}e multiplo de 3")
    else:
        print(f"o numero informado{n} nao e multiplo de 3")


