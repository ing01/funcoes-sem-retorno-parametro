##Faça uma função/método que leia três notas de um aluno e uma letra, se a letra for igual a A, deverá calcular a média aritimética das notas dos alunos, 
##se for P, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média deve ser mostrada ao final.

def media():
  nota1 = int(input('Insira a primeira nota: '))
  nota2 = int(input('Insira a segunda nota: '))
  nota3 = int(input('Insira a terceira nota: '))
  letra = input('Insira A para média aritmética e P para média ponderada: ')
  if letra == 'a' or letra =='A':
    mediaA = (nota1 + nota2 + nota3) / 3
    print('A média aritmética das nota é: ',mediaA)
  elif letra == 'p' or letra == 'P':
    mediaP = (nota1 * 5 + nota2 * 3 + nota3 * 2) / (5 + 3 + 2)
    print('A média ponderada das nota é: ',mediaP)

def main():
  media()

main()
