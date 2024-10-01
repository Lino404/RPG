
import random

##Inicio
print(f"---->Bem-vindo ao sistema de RPG do Alumnio<---- \nPrimeiro teste sua sorte, digite um numero de 1 a 10 \nVoce terá 3 tentativas para acertar o numero \nCaso acerte, terá 50% de sorte")
aleatorio = random.randint(1, 10)
pulaLinha = "**********"
print(pulaLinha)
jogo = input("Voce deseja jogar?: [S/N]: ").upper()


##Sistema de escolha de personagem
while True:
    ##sistema de sorte
    if jogo == "S":
        tentativa = int(input("Digite um numero: "))
        chances = 1

        while chances < 3:
            if tentativa == aleatorio:
                break
            else:
                if chances < 3:
                    tentativa = int(input("Incorreto, digite outro numero: "))
                    chances += 1
        #sistema caso sorte for verdadeira
        if tentativa == aleatorio:
            print(f'O numero escolhido foi {aleatorio} e voce acertou, parabens, voce recebeu 50% de sorte')
            escolha = input("Voce deseja rodar o dado? [S]/[N]: ").upper()
            if escolha == 'S':
                dado = random.randint(10, 20)
                if dado >= 10 and dado < 14:
                    classe = "Assassino"
                    vida = 70
                    dano = 15 or 25
                    atributo = 'Destreza'
                    print(f"Voce tirou {dado} no dado, sua classe é {classe}")
                    item = int(input(f"Escolha seu item \n(1)Laminas duplas (2)Elixir de invisibilidade (3)Perda de memoria"))
                    if item == 1:
                        item = "Laminas Duplas, você dará ataques rapidos com uma pequena chance de dano critico"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o item escolhido foi {item} ")
                    elif item == 2:
                        item = "Elixir da invisibilidade, você foge da batalha"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}")
                    elif item == 3:
                        item = f"Perda de memoria, caso o inimigo esteja com 20% de vida, misteriosamente você desmaia e ele aparece morto"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano, você adquiriu {item}")
                    else:
                        print("Digite um numero valido")
                elif dado >= 14 and dado < 17:
                    classe = "Mago"
                    vida = 60
                    dano = 3 or 6
                    atributo = 'Magia'
                    print(f"Voce tirou {dado} no dado, sua classe é {classe}")
                    item = int(input(f"Escolha seu item \n(1)Bola de fogo (2)Escudo arcano (3)Tempestade eletrica"))
                    if item == 1:
                        item = "Bola de fogo, lança uma esfera de fogo causando de 20 a 30 de dano"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o item escolhido foi {item} ")
                    elif item == 2:
                        item = "Escudo arcano, cria um escudo de energia magica, tankando ate 30 de dano"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}")
                    elif item == 3:
                        item = "Tempestade eletrica, conjura uma tempestade de raios, podendo causar de 25 a 35 de dano"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}")
                    else:
                        print("Digite um numero valido")
                elif dado >= 17 and dado < 20:
                    classe = "Necromante"
                    vida = 65
                    dano = 12 or 22
                    atributo = 'Controle sobre os mortos'
                    print(f"Voce tirou {dado} no dado, sua classe é {classe}")
                    item = int(input(f"Escolha seu item \n(1)Vara de ossos (2)Grimorio do Submundo (3)Toque da morte"))
                    if item == 1:
                        item = "Vara de ossos, você conjura um exercito de esqueletos podendo causar de 1 ate 35 de dano"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o item escolhido foi {item} ")
                    elif item == 2:
                        item = "Grimorio do Submundo, concede ao jogador a possibilidade de invocar uma das duas entidades do livro"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}")
                    elif item == 3:
                        item = f"Toque da morte, você pode rodar um d6, tendo a chance de tirar 0 de dano, 50% de dano ou dano critico"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}")
                    else:
                        print("Digite um numero valido")
                elif dado == 20:
                    classe = "Arquimago"
                    vida = 80
                    dano = 25 or 35
                    atributo = 'Sabedoria'
                    print(f"Voce tirou {dado} no dado, sua classe é {classe}")
                    item = int(input(f"Escolha seu item \n(1)Meteorito arcano (2)Tempestade de mana (3)Barreira mistica"))
                    if item == 1:
                        item = f"Meteorito arcano, invoca um meteorito imbuído de energia mágica que causa 50-60 de dano, com uma chance de 20% de atordoar os inimigos por 1 turno."
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o item escolhido foi {item} ")
                    elif item == 2:
                        item = "tempestade de mana, causa uma tempestade mágica causando 45 de dano"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}")
                    elif item == 3:
                        item = f"Barreira mistica, conjura um escudo de energia tankando ate 50% de dano"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}")
        ##sistema caso sorte for falsa
        else:
            print(f'O numero escolhido foi {aleatorio} e voce errou, voce jogará no seco')
            print(pulaLinha)
            escolha = input("Voce deseja rodar o dado? [S]/[N]: ").upper()
            if escolha == 'S':
                dado = random.randint(1, 20)
                ##Sistema do mendigo
                if dado >= 1 and dado <=4:
                    classe = "mendigo"
                    vida = 30
                    dano = 3 or 6
                    atributo = 'sorte'
                    print(f"Voce tirou {dado} no dado, sua classe é {classe}")
                    item = int(input(f"Escolha seu item \n(1)Pedaço de madeira (2)Roupa esfarrapada (3)Pão velho: "))
                    if item == 1:
                        item = "Pedaço de madeira"
                        item_desc = "voce dará 2 de dano a mais"
                        dano = dano + 2
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o item escolhido foi {item}, {item_desc}")
                    elif item == 2:
                        item = "Roupa esfarrapada"
                        item_desc = "vocé recebe 1 de dano a menos"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}, {item_desc}")
                    elif item == 3:
                        item = "Pão velho"
                        item_desc = "voce pode recuperar 5 de HP"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}, {item_desc}")
                    else:
                        print("Digite um numero valido")
                ##Sistema do ladrao
                elif dado > 4 and dado <= 7:
                    classe = "Ladrão"
                    vida = 50
                    dano = 7 or 10
                    atributo = 'Agilidade'
                    print(f"Voce tirou {dado} no dado, sua classe é {classe}")
                    item = int(input(f"Escolha seu item \n(1)Adaga (2)Capa das sombras (3)Bolsa de moedas roubadas: " ))
                    if item == 1:
                        item = "Adaga"
                        item_desc = "voce pode dar de 2 a 5 de dano a mais"
                        dano = dano + 2
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o item escolhido foi {item}, {item_desc} ")
                    elif item == 2:
                        item = "Capa das sombras"
                        item_desc = "voce recebe a possibilidade de desviar dos ataques"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}, {item_desc}")
                    elif item == 3:
                        item = "Bolsa de moedas roubadas"
                        item_desc = "você pode tentar subornar o oponente, talvez conseguindo escapar de um combate"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}, {item_desc}")
                    else:
                        print("Digite um numero valido")
                ##Sistema do espadachim
                elif dado > 7 and dado <= 10:
                    classe = "Espadachim"
                    vida = 80
                    dano = 10 or 15
                    atributo = 'Força'
                    print(f"Voce tirou {dado} no dado, sua classe é {classe}")
                    item = int(input(f"Escolha seu item \n(1)Espada curta (2)Armadura leve (3)Poção de vida: "))
                    if item == 1:
                        item = "Espada curta"
                        item_desc = ", você dará 5 de dano a mais"
                        dano = dano + 5
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o item escolhido foi {item}{item_desc} ")
                    elif item == 2:
                        item = "Amadura leve"
                        item_desc = ", você recebe 3 de dano a menos" 
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}{item_desc}")
                    elif item == 3:
                        item = "Poção de vida"
                        item_desc = ", voce pode recuperar 20 de HP"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}{item_desc}")
                    else:
                        print("Digite um numero valido")
                ##Sistema do assassino
                elif dado >= 10 and dado < 14:
                    classe = "Assassino"
                    vida = 70
                    dano = 15 or 25
                    atributo = 'Destreza'
                    print(f"Voce tirou {dado} no dado, sua classe é {classe}")
                    item = int(input(f"Escolha seu item \n(1)Laminas duplas (2)Elixir de invisibilidade (3)Perda de memoria: "))
                    if item == 1:
                        item = "Laminas Duplas"
                        item_desc = ", você dará ataques rapidos com uma pequena chance de dano critico"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o item escolhido foi {item}{item_desc} ")
                    elif item == 2:
                        item = "Elixir da invisibilidade"
                        item_desc = ", você foge da batalha"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}{item_desc}")
                    elif item == 3:
                        item = f"Perda de memoria"
                        item_desc = ", caso o inimigo esteja com 20% de vida, misteriosamente você desmaia e ele aparece morto"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano, você adquiriu {item}{item_desc}")
                    else:
                        print("Digite um numero valido")
                ##Sistema do mago
                elif dado >= 14 and dado < 17:
                    classe = "Mago"
                    vida = 60
                    dano = 3 or 6
                    atributo = 'Magia'
                    print(f"Voce tirou {dado} no dado, sua classe é {classe}")
                    item = int(input(f"Escolha seu item \n(1)Bola de fogo (2)Escudo arcano (3)Tempestade eletrica: "))
                    if item == 1:
                        item = "Bola de fogo"
                        item_desc = ", lança uma esfera de fogo causando de 20 a 30 de dano"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o item escolhido foi {item}{item_desc} ")
                    elif item == 2:
                        item = "Escudo arcano"
                        item_desc = ", cria um escudo de energia magica, tankando ate 30 de dano"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}{item_desc}")
                    elif item == 3:
                        item = "Tempestade eletricao"
                        item_desc = 'Conjura uma tempestade de relâmpagos ao redor do Mago, causando 25-35 de dano a todos os inimigos '
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}{item_desc}")
                    else:
                        print("Digite um numero valido")
                ##Sistema do necromante
                elif dado >= 17 and dado < 20:
                    classe = "Necromante"
                    vida = 65
                    dano = 12 or 22
                    atributo = 'Controle sobre os mortos'
                    print(f"Voce tirou {dado} no dado, sua classe é {classe}")
                    item = int(input(f"Escolha seu item \n(1)Vara de ossos (2)Grimorio do Submundo (3)Toque da morte: "))
                    if item == 1:
                        item = "Vara de ossos"
                        item_desc = ", você conjura um exercito de esqueletos podendo causar de 1 ate 35 de dano"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o item escolhido foi {item}{item_desc} ")
                    elif item == 2:
                        item = "Grimorio do Submundo"
                        item_desc = ", concede ao jogador a possibilidade de invocar uma das duas entidades do livro"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}{item_desc}")
                    elif item == 3:
                        item = "Toque da morte"
                        item_desc = f", você pode rodar um d6, tendo a chance de tirar 0 de dano, 50% de dano ou dano critico" 
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}")
                    else:
                        print("Digite um numero valido")
                ##Sistema do arquimago
                elif dado == 20:
                    classe = "Arquimago"
                    vida = 80
                    dano = 25 or 35
                    atributo = 'Sabedoria'
                    print(f"Voce tirou {dado} no dado, sua classe é {classe}")
                    item = int(input(f"Escolha seu item \n(1)Meteorito arcano (2)Tempestade de mana (3)Barreira mistica: "))
                    if item == 1:
                        item = "Meteorito arcano"
                        item_desc = f", invoca um meteorito imbuído de energia mágica que causa 50-60 de dano, com uma chance de 20% de atordoar os inimigos por 1 turno."
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o item escolhido foi {item}{item_desc} ")
                    elif item == 2:
                        item = "Tempestade de mana"
                        item_desc = ", causa uma tempestade mágica causando 45 de dano"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}{item_desc}")
                    elif item == 3:
                        item = f"Barreira mistica"
                        item_desc = f", conjura um escudo de energia tankando ate 50% de dano"
                        print(f"Voce terá {vida} de vida, dará {dano} de dano e o iten escolhido foi {item}{item_desc}")
                    else:
                        print("Digite um numero valido")
            elif escolha == 'N':
                escolha = input("Deseja jogar novamente? [S/N]: ").upper()
                if escolha == "S":
                    print("RESET")
                else:
                    print("Volte sempre")
                    break


    ##repetir o codigo
    print(pulaLinha)
    jogo = input("Deseja jogar com essa classe? [S/N]: ").upper()
    if jogo == "S":
            break
    elif jogo == "N":
        jogo = input("Deseja jogar novamente? [S/N]: ").upper()
        if jogo == "S":
            print("Nova partida iniciada")
        else:
            print("Volte sempre")
            break



print("***JOGO INICIADO***")

print(pulaLinha)

print(f"Classe: {classe}, item: {item}, atributo: {atributo}")

print("******************")
if item == "Pedaço de madeira":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e aparenta ser um pobre coitado \nEm sua mao você empunha um pedaço de madeira, talves seja util")
elif item == "Roupa esfarrapada":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e aparenta ser um pobre coitado \nVocê se sente mais aquecido que o normal, talvez esses panos velhos sirvam pra algo mais")
elif item == "Pão velho":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e aparenta ser um pobre coitado \nEm sua mao tem um..... Pao seco??? quem escolheria isso??")
if item == "Adaga":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e aparenta ser um ladrão astuto \nEm sua mão, uma adaga brilha, pronta para o combate.")
elif item == "Capa das Sombras":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e aparenta ser um ladrão astuto \nVestindo uma capa que parece se fundir com as sombras, você se sente mais ágil e furtivo.")
elif item == "Bolsa de Moedas":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e aparenta ser um ladrão astuto \nNa sua mão, uma bolsa de moedas tilinta, prometendo riqueza, mas também atraindo olhares indesejados.")
if item == "Espada curta":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e aparenta ser um espadachim habilidoso \nEm sua mão, uma espada curta reluzente, pronta para cortar seus inimigos.")
elif item == "Armadura leve":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e aparenta ser um espadachim habilidoso \nVestindo uma armadura leve, você se sente protegido e ágil, pronto para a batalha.")
elif item == "Poção de vida":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e aparenta ser um espadachim habilidoso \nEm sua mão, uma poção de vida brilha, prometendo restaurar sua energia em momentos de necessidade.")
if item == "Laminas duplas":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e aparenta ser um assassino ágil \nEm suas mãos, duas lâminas brilhantes, prontas para atacar de forma silenciosa e mortal.")
elif item == "Elixir de invisibilidade":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e aparenta ser um assassino ágil \nEm sua mão, um elixir de invisibilidade reluz, prometendo torná-lo invisível aos olhos de seus inimigos.")
elif item == "Perda de memoria":
    print(f'Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e aparenta ser um assassino ágil \n"Eu deveria estar segurando algo? estranho..."')
elif item == "Bola de fogo":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e sente o poder das chamas correndo por suas veias \nEm suas mãos, uma esfera de fogo começa a se formar, pronta para consumir seus inimigos.")
elif item == "Escudo arcano":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e sente uma poderosa proteção ao seu redor \nUm escudo arcano brilha, protegendo você de ataques enquanto você canaliza sua magia.")
elif item == "Tempestade eletrica":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha pra si mesmo e sente a energia elétrica pulsar ao seu redor \nAo levantar suas mãos, o céu escurece e uma tempestade eletrica se forma, pronta para devastar tudo ao redor.")
if item == "Vara de ossos":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha para si mesmo e sente a energia sombria que emana da terra \nEm suas mãos, uma vara feita de ossos vibra, conectando você às forças que comandam os mortos.")
elif item == "Grimorio do Submundo":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha para si mesmo e sente o conhecimento proibido fluindo por sua mente \nO Grimório do Submundo repousa em suas mãos, repleto de segredos que invocam criaturas das profundezas.")
elif item == "Toque da morte":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha para si mesmo e percebe que sua própria carne está pálida e fria \nSeu toque carrega a essência da morte, drenando a vida de qualquer ser que ousar cruzar seu caminho.")
if item == "Meteorito arcano":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê olha para o céu, sentindo o poder arcano se acumulando em suas mãos \nO Meteorito Arcano é sua arma, capaz de devastar seus inimigos com o poder concentrado dos céus.")
elif item == "Tempestade de mana":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê sente a energia mágica pulsar ao seu redor, vibrando com poder puro \nA Tempestade de Mana se prepara em suas mãos, pronta para consumir qualquer oponente com um ataque de energia bruta.")
elif item == "Barreira mistica":
    print(f"Você misteriosamente aparece nesse mundo de aparencia arcaica \nVocê sente uma proteção invisível cercá-lo, uma parede de pura energia mágica \nA Barreira Mística brilha ao seu redor, protegendo você de qualquer perigo iminente.")


print(pulaLinha)
print("Voce ouve um galho se quebrando, o que pode ser?")
escolhaI = input("Deseja rodar um dado? [S/N]: ").upper()



##Sistema de combate

if escolhaI == "S":
    dado1 = random.randint(5, 6)
    if dado1 <=4:
        print("era apenas um esquilo")
    elif dado1 > 4 and dado1 <= 6:
        escolhaI = int(input("Um Goblin aparece do meio do mato, o que quer fazer? (1)Lutar (2)Ignorar"))
        if escolhaI == 1:
            print(pulaLinha)
            print('Prepare-se para a batalha')
            inimigo = "Goblin"
            dadoInimigo = random.randint(1, 20)


            while True:
                dadoInimigo = random.randint(1, 6)
                if dadoInimigo <= 2:
                    ataque1 = "Garra veloz"
                    ataque1_desc = "O goblin se aproxima rapidamente, desferindo um golpe com suas garras sujas e afiadas, tentando rasgar a pele do oponente"
                    print(f"O Goblin desfere {ataque1}")
                    escolhaA = int(input("(1)Desviar (2)nao fazer nada"))
                    if escolhaA == 1:
                        desvio = random.randint(1, 10)
                        if desvio == 10:
                            print(f"Voce tirou {desvio} no dado, seu desvio foi perfeito")
                        elif desvio < 10 and desvio >= 7:
                            vida = vida - 10
                            print(f"Voce recebeu 10 de dano, voce esta com {vida} de vida")
                        elif desvio < 7 and desvio >= 4:
                            vida = vida - 15
                            print(f"Voce recebeu 10 de dano, voce esta com {vida} de vida")
                        elif desvio < 4 and desvio >= 1:
                            vida = vida - 20
                            print(f"Voce recebeu 10 de dano, voce esta com {vida} de vida")

        elif escolhaI == 2:
            print("Voce escolheu ignora-lo")




