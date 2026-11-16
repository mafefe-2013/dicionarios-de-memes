import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print(' Bem-vindo ao seu assistente de senhas. Vc pode sortear a sua senha')
tamanho = int(input("Quantos caracteres você quer na senha? Mínimo: 4 - máximo: 15: "))

if 4 <= tamanho <= 15:
    senha = ""

    for i in range(tamanho):
        senha += random.choice(caracteres)

    print("Sua senha é:", senha)
else:
    print("O tamanho deve estar entre 4 e 15.")
