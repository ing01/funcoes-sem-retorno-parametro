##(Função sem retorno sem parâmetro) Faça uma função/método que leia um valor inteiro e positivo N e mostre o valor de S, obtido pelo seguinte cálculo:
##S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!

def calcular_fatorial ():
  n =  int(input("Insira um valor: "))
  s = 1
  for i in range(1,n+1):
    fatorado = 1
    while i > 1:
      fatorado = fatorado * i
      i = i - 1 #decremento
    s = s + 1 / fatorado
  print(s)
 
def main ():
    calcular_fatorial ()
 
main ()
