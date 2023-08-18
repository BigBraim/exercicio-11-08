print('')
n = int(input('Digite um número inteiro: '))

unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10

print('Verificando o número {}...'.format(n))
print('{} Milhar(es) {} Centena(s) {} Dezena(s) {} Unidade(s)'.format(milhar, centena, dezena, unidade))

