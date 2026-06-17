import time
print("Olá! eu sou Nilo, seu assitente digital")

time.sleep(2)
print("fui criado para saber sobre como você está.")
time.sleep(1)
print("\nPara comecar, digite 'vamos'")
comeco = input("vamos começar? ")
if comeco.lower() == "vamos":
    time.sleep(1)
    print("\nPara comecar diga seu nome")
    nome = input("Meu nome é: ")
    time.sleep(1)
    print(f"\nOlá,{nome}")
    time.sleep(1)
    print("\nMe diga como você está")
    resposta = input("digite 'bem' ou 'mal': ")
    if resposta.lower() == "bem":
        time.sleep(1)
        print("\nque coisa boa!")
    elif resposta.lower() == "mal":
        time.sleep(1)
        print(f"\nEita, {nome}; sinto muito")
    else:
        time.sleep(1)
        print("\nnao entendi a resposta")
        print("responda com 'bem' ou 'mal'")
        bem_mal = input("Eu estou: ")
        if bem_mal == "bem":
            time.sleep(1)
            print(f"\nque coisa boa, {nome}!")
        elif bem_mal == "mal":
            time.sleep(1)
            print(f"nEita, {nome}; sinto muito")

    time.sleep(1)
    resposta_02 = input("\no que te deixou assim?")
    if resposta_02.lower() == "não quero falar":
        time.sleep(1)
        print("\nTudo bem, mas desejo melhoras")
    else:
        time.sleep(1)
        print("\nvoce disse: ", resposta_02)
        print("entao faz total sentido dizer que esteja", resposta)
    time.sleep(1)
    print(f"\n{nome}, você sente que precisa de alguma ajuda?")
    ajuda = input("responda com 'sim' ou 'não'")
    if ajuda.lower() == "sim":
        time.sleep(1)
        print(f"\n{nome}, então vamos conversar um pouco")
        time.sleep(1)
        print(f"\nvocê havia me dito: {resposta_02}")
        time.sleep(1)
        problema = input("Como isso chega para você?")
        if problema.lower() == "Não quero falar":
            time.sleep(1)
            print(f"Tudo bem, {nome}, mas lhe desejo melhoras")
        else:
            time.sleep(1)
            problema_ação = input("\nO que pensa em fazer diante disso?")
            if problema_ação.lower() == "me matar" or problema_ação.lower() == "matar" or  problema_ação.lower() == "suicidar" or problema_ação.lower() == "morrer":
                time.sleep(1)
                print(f"\n{nome}, sua situação exige cuidado humano")
                time.sleep(1)
                print("recomendo ligar para o CVV, no número 180")
            else:
                time.sleep(1)
                print("\nE acha que isso resolve?")
                time.sleep(1)
                ação = input("responda 'sim' ou 'não'")
                if ação.lower() == "sim":
                    time.sleep(1)
                    falta_ação = input("\nEntão que falta para fazer?")
                    if falta_ação.lower() == "nada":
                        time.sleep(1)
                        print("Então você sabe o que fazer")
                    elif falta_ação.lower() == "dinheiro" or falta_ação.lower() == "tempo":
                        time.sleep(1)
                        print(f"Realmente {nome}, entendo que isso pesa")
                        time.sleep(1)
                        print("Penso que então cabe entender que nem tudo controlamos")
                    else:
                        time.sleep(1)
                        print(f"\n{nome}, me parece que você sabe o que precisa fazer")
                        time.sleep(1) 
                        print("minha sugestão é que você procure ajuda humana profissional")

                else:
                    nao_fazer = input("\nEntão porque pensa em fazer isso? nãop")
                    if nao_fazer == "Não penso":
                        time.sleep(1)
                        print(f"Entendi {nome}, sugiro procurar ajuda humana")
                    else:
                        time.sleep(1)
                        print(f"\n{nome}, me parece que você sabe o que precisa fazer")
                        time.sleep(1) 
                        print("minha sugestão é que você procure ajuda humana profissional")

    else:
        time.sleep(1)
        print(f"\nTá bem, {nome}")
        time.sleep(1)
        print("Mas se precisar de algo pode me chamar")

else :
    time.sleep(1) 
    print("ok")
