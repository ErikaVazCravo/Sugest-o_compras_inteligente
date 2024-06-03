# Entrada do usuário
cogumelo_desejado = input()

# Função para sugerir cogumelos com preços mais baixos com base em um cogumelo desejado.
def sugerir_cogumelos(cogumelo_desejado):
    #TODO: Defina um dicionário onde as chaves são os tipos de cogumelos e os valores são os preços correspondentes
    catalogo = {
        "Shitake": 10,
        "Portobello": 8,
        "Shimeji": 6,
        "Champignon": 12,
        "Funghi": 16,
        "Porcini": 16
    }

    # Lista de cogumelos em ordem de prioridade
    ordem_prioridade = ["Shitake", "Portobello", "Shimeji", "Champignon", "Funghi", "Porcini"]


    # Verifica se o cogumelo desejado está no catálogo
    if cogumelo_desejado in catalogo:
        # TODO: Se estiver no catálogo, armazene o preço do cogumelo desejado e crie uma lista vazia para as sugestões
        valor_desejado = catalogo[cogumelo_desejado]
        sugestoes = []
        
        # Procura por cogumelos mais baratos no catálogo seguindo a ordem de prioridade
        for cogumelo in ordem_prioridade:
            if cogumelo in catalogo:
                valor = catalogo[cogumelo]
                if valor <= valor_desejado and cogumelo != cogumelo_desejado:
                    sugestoes.append((cogumelo, valor))
                    if len(sugestoes) == 2:
                        break
        
        if not sugestoes:
            # TODO: Se não houver sugestões, exiba a mensagem indicada no enunciado
            print("Desculpe, não há sugestões disponíveis.")
        else:
            for sugestao, valor_sugestao in sugestoes:
                print(f"{sugestao} - Valor: {valor_sugestao}")
    else:
        # TODO: Se o cogumelo desejado não estiver no catálogo, exiba uma mensagem de erro indicada no enunciado
        print("Cogumelo não encontrado no catálogo.")

# Chamada da função para sugerir cogumelos
sugerir_cogumelos(cogumelo_desejado)