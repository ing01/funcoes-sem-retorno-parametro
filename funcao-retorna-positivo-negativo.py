# Algoritmo contendo uma função/método que apresente o valor 1 se o número digitado for positivo e 0 se for negativo.

def num():
    n = int(input('Digite um número: '))
    if n > 0:
        print('1')
    else:
        print('0')

def main():
    num()

main()
