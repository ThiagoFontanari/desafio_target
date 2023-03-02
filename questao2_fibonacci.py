# Recebendo do usuário até qual o valor se deseja calcular a sequência de Fibonacci
numero_recebido = int(input("\nOlá! Por gentileza, informe até qual valor você deseja calcular a sequência de Fibonacci:\n"))

# Valores iniciais para calcular a sequência
valor1 = 0
valor2 = 1
sequencia = [0, 1]

# Realizando o cálculo da sequência, até o valor informado pelo usuário
while max(sequencia) < numero_recebido:
    
    valor3 = valor1 + valor2
    valor1 = valor2
    valor2 = valor3
    if valor3 > numero_recebido: break
    sequencia.append(valor3)

# Exibindo a sequência calculada
print(f"\nA sequência de Fibonacci calculada, até o valor informado, é {sequencia}.\n")

# Verificando se o valor informado encontra-se na sequência
if numero_recebido in sequencia : 
    print(f"\nO número informado foi {numero_recebido}, e ele encontra-se na sequência calculada.\n")
else:
    print("\nO número informado não encontra-se na sequência calculada.\n")
