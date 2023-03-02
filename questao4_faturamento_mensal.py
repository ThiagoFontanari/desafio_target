faturamento_SP = 67836.43
faturamento_RJ = 36678.66
faturamento_MG = 29229.88
faturamento_ES = 27165.48
faturamento_OUTROS = 19849.53
faturamento_TOTAL = faturamento_SP + faturamento_RJ + faturamento_MG + faturamento_ES + faturamento_OUTROS

# Definindo uma função que calcula a porcentagem que cada valor representa
def calcula_percentual(valor):
    return (valor*100)/faturamento_TOTAL

# Aplicando a função de cálculo da porcentagem aos valores fornecidos
sp = calcula_percentual(faturamento_SP)
print(f'\nO percentual do faturamento referente a SP é {sp:.2f}%')
rj = calcula_percentual(faturamento_RJ)
print(f'\nO percentual do faturamento referente a RJ é {rj:.2f}%')
mg = calcula_percentual(faturamento_MG)
print(f'\nO percentual do faturamento referente a MG é {mg:.2f}%')
es = calcula_percentual(faturamento_ES)
print(f'\nO percentual do faturamento referente a ES é {es:.2f}%')
outros = calcula_percentual(faturamento_OUTROS)
print(f'\nO percentual do faturamento referente a outros estados é {outros:.2f}%')
