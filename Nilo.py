import time

#saudação inicial
print("Olá! eu sou Nilo.")
time.sleep(1)
print("Fui criado para saber sobre como você está.")
time.sleep(1)
print("\nQual seu nome?")
nome = input("Meu nome é: ")
time.sleep(1)
print(f"\nOlá, {nome}")

#começar conversa
time.sleep(1)
print("\nPara comecar, digite 'vamos'")
comeco = input("vamos começar? ").strip()
if comeco.lower() != "vamos":
  print(f"\nTá bem, {nome}")
  time.sleep(1)
  print("Mas se precisar de algo pode me chamar.")

#Sabendo como está
else:
 mensagem = input("\nComo você está se sentindo: ").lower()
 humor = 5

 ótimo = mensagem.count("ótimo")*3
 feliz = mensagem.count("feliz")*2
 bem = mensagem.count("bem") * 1
 mal = mensagem.count("mal") * -1
 triste = mensagem.count("triste") * -2
 péssimo = mensagem.count("péssimo") * -3

 humor = 5 + bem + feliz + mal + triste + péssimo + ótimo
 humor_numero = humor

 if humor >= 7:
  humor = "muito bem"
  print(f"Você me parece estar muito bem, {nome}")
 elif humor >= 6:
  humor = "bem"
  print(f"Você me parece estar bem, {nome}")
 elif humor >= 5:
  humor = "normal"
  print(f"Você me parece estar normal, {nome}")
 elif humor >= 4:
  humor = "mal"
  print(f"Você me parece estar mal, {nome}")
 elif humor >= 3:
  print(f"Você me parece estar muito mal, {nome}")
  humor = "muito mal"
 else:
  humor = "péssimo"
  print(f"Você me parece estar péssimo, {nome}")

 #Saber o  motivo
 time.sleep(1)
 motivo = input("\nO que te deixou assim? ").lower()

 consegui = motivo.count("consegui")*3
 passei = motivo.count("passei")*3
 ganhei = motivo.count("ganhei")*3
 feliz = motivo.count("feliz")*2
 nada = motivo.count("nada")
 errei = motivo.count("errei") * -1
 perdi = motivo.count("perdi") * -2
 chorei = motivo.count("chorei") * -3

 motivo_humor = humor_numero + consegui + passei + ganhei + feliz + nada + errei + perdi + chorei
 
 if motivo_humor >= 7:
    print("\nQue coisa boa!")
    print(f"Isso parece combinar com o fato de estar {humor}.")
 elif motivo_humor >= 5:
    print("\nEntendi.")
    print(f"Você disse: {motivo}")
    print(f"Então faz sentido dizer que esteja {humor}.")
 else: 
    print(f"Entendi {nome},")
    print(f"Isso faz total sentido com você estar {humor}.")

  #classificação de bem-estar
 bem = "\033[0;32;42mAA\033[0;0;0m"
 normal = "\033[0;33;43mAA\033[0;0;0m"
 mal = "\033[0;31;41mAA\033[0;0;0m"

 if motivo_humor >= 6:
    print(f"Já que você está assim, vou classificar seu bem estar como: {bem} ")
 elif motivo_humor >= 5:
    print(f"Já que você está assim, vou classificar seu bem estar como: {normal} ")
 else: 
    print(f"Já que você está assim, vou classificar seu bem estar como: {mal} ")

 print(f"""\nNossa classificação é:
 bem: {bem}
 normal : {normal}
 mal: {mal}      """) 



     
    
#     print(f"\n{nome}, você sente que precisa de alguma ajuda?")
#     ajuda = input("responda com 'sim' ou 'não'")
#     if ajuda.lower() == "sim":
#         time.sleep(1)
#         print(f"\n{nome}, então vamos conversar um pouco")
#         time.sleep(1)
#         print(f"\nvocê havia me dito: {resposta_02}")
#         time.sleep(1)
#         problema = input("Como isso chega para você?")
#         if problema.lower() == "Não quero falar":
#             time.sleep(1)
#             print(f"Tudo bem, {nome}, mas lhe desejo melhoras")
#         else:
#             time.sleep(1)
#             problema_ação = input("\nO que pensa em fazer diante disso?")
#             if problema_ação.lower() == "me matar" or problema_ação.lower() == "matar" or  problema_ação.lower() == "suicidar" or problema_ação.lower() == "morrer":
#                 time.sleep(1)
#                 print(f"\n{nome}, sua situação exige cuidado humano")
#                 time.sleep(1)
#                 print("recomendo ligar para o CVV, no número 180")
#             else:
#                 time.sleep(1)
#                 print("\nE acha que isso resolve?")
#                 time.sleep(1)
#                 ação = input("responda 'sim' ou 'não'")
#                 if ação.lower() == "sim":
#                     time.sleep(1)
#                     falta_ação = input("\nEntão que falta para fazer?")
#                     if falta_ação.lower() == "nada":
#                         time.sleep(1)
#                         print("Então você sabe o que fazer")
#                         print(f"\nAté logo, {nome}!")
#                         print("Foi bom conversar com você.")
#                     elif falta_ação.lower() == "dinheiro" or falta_ação.lower() == "tempo":
#                         time.sleep(1)
#                         print(f"Realmente {nome}, entendo que isso pesa")
#                         time.sleep(1)
#                         print("Penso que então cabe entender que nem tudo controlamos")
#                         print(f"\nAté logo, {nome}!")
#                         print("Foi bom conversar com você.")
#                     else:
#                         time.sleep(1)
#                         print(f"\n{nome}, me parece que você sabe o que precisa fazer")
#                         time.sleep(1) 
#                         print("minha sugestão é que você procure ajuda humana profissional")
#                         print(f"\nAté logo, {nome}!")
#                         print("Foi bom conversar com você.")

#                 else:
#                     nao_fazer = input("\nEntão porque pensa em fazer isso? não")
#                     if nao_fazer == "Não penso":
#                         time.sleep(1)
#                         print(f"Entendi {nome}, sugiro procurar ajuda humana")
#                         print(f"\nAté logo, {nome}!")
#                         print("Foi bom conversar com você.")
#                     else:
#                         time.sleep(1)
#                         print(f"\n{nome}, me parece que você sabe o que precisa fazer")
#                         time.sleep(1) 
#                         print("minha sugestão é que você procure ajuda humana profissional")
#                         print(f"\nAté logo, {nome}!")
#                         print("Foi bom conversar com você.")

#     else:
#         time.sleep(1)
#         print(f"\nTá bem, {nome}")
#         time.sleep(1)
#         print("Mas se precisar de algo pode me chamar")

# else :
#     time.sleep(1) 
#     print("ok")
