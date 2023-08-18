print('')
palavra = input("Digite uma frase: ").upper().strip()

print("A letra A aparece {} vez(es) nesta(s) palavra(s).".format(palavra.count('A')))
print("A primeira letra A aparece na posição {}.".format(palavra.find('A')+1))
print("A última letra A aparece na posição {}.".format(palavra.rfind('A')+1))