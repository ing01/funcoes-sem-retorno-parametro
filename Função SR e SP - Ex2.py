##Faça uma função/método que leia dois valores positivos e apresente a soma dos N números existentes entre eles (inclusive).

def somar_entre():
  a = int(input('Informe um valor: '))
  b = int(input('Informe outro valor: '))
  soma = 0
  while (a > 0 and b > 0) and a <= b:
    soma = soma + a
    a = a + 1
  print('O resultado é', soma)
  acumuladora = 0
  if (a > 0 and b > 0) and a <= b:
    for c in range(a,b+1):
      acumuladora = acumuladora + c

def main():
    somar_entre()

main()
