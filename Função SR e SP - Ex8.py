##Faça uma função/método que leia uma hora de início e de término de um jogo, ambas divididas em dois valores distintos: hora e minuto. 
##Deverá ser apresentado a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.

def tempo():
  inicio = int(input('Insira o horário de início do jogo: '))
  minuto_i = int(input('Insira o minuto de início do jogo: '))
  final = int(input('Insira o horário de término do jogo: '))
  minuto_f = int(input('Inira o minuto de término do jogo: '))
  if minuto_f < minuto_i:
    minuto_f = minuto_f + 60
    minuto_f = minuto_f - 1
  if final < inicio:
    final = final + 24
  total_m = minuto_f - minuto_i
  total_h = final - inicio
  total = total_h * 60 + total_m
  print('A duração do jogo é de',total,'minutos.')
 
def main():
  tempo()
 
main()
