print('')
print ('Escolha entre "Separando Numeros Por Digito", "Silva", "Cidade Santo", e "Letra A" ')
print('')
print ('Separando Numeros Por Digito: 1')
print ('Silva: 2')
print ('Cidade Santo: 3')
print ('Letra A: 4')
print('')

nome = int(input('Escolha entre 1, 2, 3, e 4: '))

match nome:
    case 1:
        import SeparandoNumerosPorDigito

    case 2:
        import Silva

    case 3:
        import CidadeSanto

    case 4:
        import LetraA

    case _:
        ValueError
        print('ERRO: Digite apenas NÚMEROS entre 1, 2, 3, e 4! ')