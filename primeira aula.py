Nonememe_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            'BETA': 'uma pessoa que não tem aura/ ou pessoa chata',
            'GAG DE LA GAG': 'estou chocada',
            'VDD': 'verdade',
            'BLZ': 'beleza',
            'DIVA': 'pessoa incrivel,maravilhosa',
            'AESTHETIC': 'uma coisa com a estetica/aparença bonita',
            'TLGD': 'ta ligado',
            'OBG': 'obrigado',
            'BJS': 'bejos',
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in Nonememe_dict.keys():
   print(Nonememe_dict[word])
else:
   print('palavra não encontrada')


