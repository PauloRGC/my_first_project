
# Operações

# Usuario escolhe 2 numeros ja convertidos para "float" e a operação desejada:
num_1 = float(input('Digite o primeiro numero: '))
num_2 = float(input('Digite o segundo numero: '))
choice = input('Digite a operação desejada(soma, subtração, multiplicação, divisão, média):' )

# De acordo com a escolha do usurio retornar a resposta
if choice == 'soma':
  print('A soma dos numero é: ', num_1 + num_2)
elif choice == 'subtração':
  print('A subtração é: ', num_1 - num_2)
elif choice == 'multiplicação':
  print('A multiplicação é: ', num_1 * num_2)
elif choice == 'divisão':
  print('A divisão é: ', num_1 / num_2)
elif choice == 'média':
  print('A média é: ', (num_1 + num_2) / 2)
else:
  print('Operação inválida')

