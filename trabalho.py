import random

print("MISTÉRIO DA TAÇA")
print("="*50)
print("Era uma sexta-feira, 13 de julho, véspera da grande e " \
"aguardada final entre a PUCPR e a UFPR, quando o clima de tensão e rivalidade " \
"foi interrompido por um mistério na sala da diretora: a cobiçada " \
"Taça Araucária de Ouro havia desaparecido.")
print("="*50)

vidas = 3
pontos = 0
conquista_bastao = False
conquista_oswaldo = False
conquista_explorador = False
conquista_mestre = False
suspeitos_interrogados = set()
locais_visitados = set()

personagens = {
    "1": {
        "nome": "Jason",
        "entrevista": "Ele não diz muita coisa, mas anda com uma faca e foi visto rondando o estacionamento."
    },
    "2": {
        "nome": "Técnico Joãozinho",
        "entrevista": "Relatou que viu o apagão das câmeras diretamente pelo seu notebook."
    },
    "3": {
        "nome": "Decano Rodrigo",
        "entrevista": "Afirma que passa o tempo todo registrando tudo rigorosamente em sua caderneta."
    },
    "4": {
        "nome": "Nicole",
        "entrevista": "Comanda as líderes de torcida e menciona que adora colecionar troféus."
    },
    "5": {
        "nome": "Cachorro Oswaldo",
        "entrevista": "É um cachorro caramelo e não fala nada, mas deixou rastros pelo campus."
    },
    "6": {
        "nome": "Mascote Leãozinho",
        "entrevista": "Garante que sequer compareceu ao jogo final, tendo um álibi."
    },
    "7": {
        "nome": "Aluno da UFPR",
        "entrevista": "Afirma indiscutivelmente que odeia futebol e que não tem nada a ver com o sumiço da taça."
    }
}

local = { 
    "1": {
        "nome": "Diretoria",
        "item": None,
        "detalhe_item": "",
        "fatos": "O local onde a Taça Araucária de Ouro foi roubada na sexta-feira."
    },
    "2": {
        "nome": "Estacionamento",
        "item": None,
        "detalhe_item": "",
        "fatos": "Área externa onde foram vistas movimentações estranhas perto dos postes de energia."
    },
    "3": {
        "nome": "Campo de Futebol",
        "item": None,
        "detalhe_item": "",
        "fatos": "O gramado principal onde ocorreu a grande final."
    },
    "4": {
        "nome": "Sala de TI",
        "item": None,
        "detalhe_item": "",
        "fatos": "Onde o sistema de monitoramento da instituição é controlado."
    },
    "5": {
        "nome": "Arquibancada",
        "item": None,
        "detalhe_item": "",
        "fatos": "Onde a torcida costuma se reunir para apoiar os times."
    },
    "6": {
        "nome": "Secretaria",
        "item": None,
        "detalhe_item": "",
        "fatos": "O setor administrativo central do campus universitário."
    }
}

itens_jogo = [
    {
        "nome": "Bloco de notas do Decano",
        "detalhe": "Você folheia as páginas do bloco de notas, mas só encontra anotações sobre comportamento de alunos."
    },
    {
        "nome": "Notebook do Joãozinho",
        "detalhe": "Analisando o notebook, você descobre registros que provam que as câmeras da diretoria foram desligadas durante o apagão!"
    },
    {
        "nome": "Facão do Jason",
        "detalhe": "Olhando para o facão você percebe que os fios de energia foram cortados com precisão cirúrgica."
    },
    {
        "nome": "Osso",
        "detalhe": "Você pega o osso e percebe que ele está completamente molhado de baba do cão Oswaldo!"
    },
    {
        "nome": "Bastão de pregos",
        "detalhe": "Item investigado."
    }
]

chaves_locais = list(local.keys())
random.shuffle(chaves_locais)

for i in range(5):
    chave_loc = chaves_locais[i]
    local[chave_loc]["item"] = itens_jogo[i]["nome"]
    local[chave_loc]["detalhe_item"] = itens_jogo[i]["detalhe"]

investigando = True

while investigando and vidas > 0:
    print(50*"_")
    print(f"Vidas: {vidas} | Pontuação: {pontos}")
    print("O que você deseja fazer agora?")
    print("[1] Interrogar um suspeito")
    print("[2] Investigar um local")
    print("[3] Consultar analise do caderno (Premissas e Deducao)")
    print("[4] Fazer acusacao final")

    opcao = input("Digite uma opcao: ").strip()

    if opcao == "1":
        print("\nQual suspeito você deseja interrogar?")
        for chave, dados in personagens.items():
            print(f"[{chave}] {dados['nome']}")
            
        personagem = input("Digite o número do suspeito: ").strip()

        if personagem in personagens:
            nome_suspeito = personagens[personagem]['nome']
            print(f"\nVocê conversou com {nome_suspeito}:")
            print(f"-> Relato: {personagens[personagem]['entrevista']}")
            
            if personagem == "5":
                if not conquista_oswaldo:
                    carinho = input("Deseja fazer carinho no Cachorro Oswaldo? (s/n): ").strip().lower()
                    if carinho == 's':
                        conquista_oswaldo = True
                        pontos += 25
                        print("\nVocê faz carinho no cão caramelo. Ele abana o rabo alegremente e desenterra um velho brinquedo de pelúcia no gramado.")
                        print("CONQUISTA: Oswaldo detetive desbloqueada! (+25 pontos)")
                    else:
                        print("Você decidiu não mexer com o cachorro.")
                else:
                    print("\nOswaldo já brincou com você antes e agora está apenas descansando feliz.")

            if personagem not in suspeitos_interrogados:
                suspeitos_interrogados.add(personagem)
                if len(suspeitos_interrogados) == len(personagens) and not conquista_mestre:
                    conquista_mestre = True
                    pontos += 30
                    print("CONQUISTA: Mestre dos interrogatórios desbloqueada! (+30 pontos)")
        else:
            print("\nOpção de suspeito inválida!")

    elif opcao == "2":
        print("\nQual local você deseja investigar?")
        for chave, dados in local.items():
            print(f"[{chave}] {dados['nome']}")
            
        escolha_local = input("Digite o número do local: ").strip()

        if escolha_local in local:
            lugar_nome = local[escolha_local]['nome']
            print(f"\nVocê foi até: {lugar_nome}")
            print(f"-> Observação: {local[escolha_local]['fatos']}")

            if escolha_local not in locais_visitados:
                locais_visitados.add(escolha_local)
                if len(locais_visitados) == len(local) and not conquista_explorador:
                    conquista_explorador = True
                    pontos += 30
                    print("CONQUISTA: Explorador completo desbloqueada! (+30 pontos)")

            if local[escolha_local]['item'] is not None:
                item_encontrado = local[escolha_local]['item']
                print(f"Você encontrou um item: {item_encontrado}")
                inspecionar = input("Deseja inspecionar o item de perto? (s/n): ").strip().lower()

                if inspecionar == 's':
                    if "bastão de pregos" in item_encontrado.lower() and not conquista_bastao:
                        conquista_bastao = True
                        pontos += 35
                        print("\nFLAGRANTE: Assim que você pega o bastão de pregos, o Aluno da UFPR surge correndo de capuz, arranca o bastão da sua mão gritando que é dele e vai embora resmungando!")
                        print("CONQUISTA: Ladrão de bastões desbloqueada! (+35 pontos)")
                    
                    elif "osso" in item_encontrado.lower():
                        pontos += 15
                        print(f"-> Detalhe: {local[escolha_local]['detalhe_item']}")
                        print("CONQUISTA: Cão farejador desbloqueada! (+15 pontos)")

                    elif "bloco de notas" in item_encontrado.lower():
                        pontos -= 5
                        print(f"-> Detalhe: {local[escolha_local]['detalhe_item']}")
                        print("Você perdeu 5 pontos por inspecionar uma pista irrelevante.")

                    else:
                        pontos += 20
                        print(f"-> Detalhe: {local[escolha_local]['detalhe_item']}")
                        print("Você investigou uma evidência importante e ganhou 20 pontos!")
                    
                    local[escolha_local]['item'] = None
                else:
                    print("Você decidiu não mexer no item por enquanto.")
            else:
                pontos += 5
                print("Nenhum item relevante à vista neste local, mas você mapeou a área. (+5 pontos)")
        else:
            print("\nLocal inválido!")

    elif opcao == "3":
        print("\n" + "="*30)
        print("--- ANALISE DO CADERNO (PREMISSAS) ---")
        print("="*30)
        if len(suspeitos_interrogados) < len(personagens) or len(locais_visitados) < len(local):
            print("O caderno de análise formal ainda está bloqueado!")
            print(f"Interrogue todos os suspeitos ({len(suspeitos_interrogados)}/{len(personagens)}) e visite todos os locais ({len(locais_visitados)}/{len(local)}) para desbloquear as premissas importantes.")
        else:
            print("Premissas Iniciais e Dedução Formal Desbloqueadas:\n")
            print("P1: ¬L (Leãozinho não compareceu)")
            print("P2: ¬L → C (Se faltou, Jason cortou fios)")
            print("P3: C → ¬B (Se cortou fios, câmeras pararam)")
            print("P4: H (Nicole coleciona troféus)")
            print("P5: I (Nicole comanda a torcida)")
            print("P6: (¬B ∧ (H ∧ I)) → Z")
            print("\nAplique as regras de inferência formal para deduzir quem é Z.")

    elif opcao == "4":
        print("\n" + "="*30)
        print("--- ACUSACAO FINAL ---")
        print("="*30)
        print("Quem você acha que roubou a Taça Araucária de Ouro?")
        for chave, dados in personagens.items():
            print(f"[{chave}] {dados['nome']}")
        
        acusacao_num = input("Digite o número do suspeito que deseja acusar: ").strip()

        if acusacao_num == "":
            print("\nEntrada vazia! Você não digitou nenhum número.")
        elif acusacao_num in personagens:
            if personagens[acusacao_num]['nome'].lower() == "nicole":
                bonus_investigacao = 0
                if len(suspeitos_interrogados) == len(personagens):
                    bonus_investigacao = 30

                bonus_vidas = vidas * 10
                pontos += bonus_vidas + bonus_investigacao
                
                print(f"\nParabéns! Você concluiu que Nicole roubou a taça aproveitando o apagão técnico gerado por Jason, combinado com seu perfil e motivação!")
                print(f"Bônus por terminar com {vidas} vida(s): +{bonus_vidas} pontos.")
                print(f"Sua pontuação final foi de {pontos} pontos!")
                investigando = False
            else:
                vidas -= 1
                print(f"\nErrado! {personagens[acusacao_num]['nome']} não é a culpada ou tem um álibi.")
                if vidas > 0:
                    print(f"Você perdeu uma vida! Restam {vidas} vidas. Continue investigando.")
                else:
                    print("\nGAME OVER! Suas vidas acabaram e o mistério ficou sem solução.")
        else:
            print("\nOpção inválida! Digite um número de 1 a 7.")
    else:
        print("\nOpção inválida! Digite 1, 2, 3 ou 4.")