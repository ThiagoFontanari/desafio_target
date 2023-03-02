# Importando o módulo json e abrindo o arquivo de dados para leitura
import json
with open ("dados.json", encoding='utf8') as arquivo:
    dicionario_dados = json.load(arquivo)

# Selecionando os dias com valores de faturamento validos
faturamentos_validos = []
for i in dicionario_dados:
    if i['valor'] > 0:
        faturamentos_validos.append(i)

# Calculando a soma dos faturamentos validos e criando uma lista com os faturamentos
# individuais.
soma_faturamentos = 0
faturamentos_individuais = []

for i in faturamentos_validos:
    soma_faturamentos = soma_faturamentos + i['valor']
    faturamentos_individuais.append(i['valor'])

# Calculando a média de faturamento e verificando quantos dias tiveram o faturamento
# acima da média.
acima_da_media = 0        
media_faturamento = soma_faturamentos/len(faturamentos_validos)

for i in faturamentos_individuais:
    if i > media_faturamento: acima_da_media += 1

# Exibindo a saída para o usuário
faturamento_maximo = max(faturamentos_individuais)
faturamento_minimo = min(faturamentos_individuais)

print(f"\nNeste mês, o menor faturamento foi de {faturamento_minimo:.2f}, e o maior foi de {faturamento_maximo:.2f}\n")

print(f"A média do faturamento mensal foi de {media_faturamento:.2f}, e em {acima_da_media} dias, o faturamento foi acima da média.\n")
