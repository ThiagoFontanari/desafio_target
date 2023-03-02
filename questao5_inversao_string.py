# Recebendo a string para inversão
string = input("\nPor favor, informe a string que você deseja inverter:\n")

# Invertendo a string recebida, utilizando slice
string_invertida = string[::-1]

# Apresentando o resultado final
print(f"A string informada, de maneira invertida é:\n{string_invertida}")