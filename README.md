# Desafios de Código - Simulando Desafios com IAs Generativas
# 4 / 5 - Sugestão de Compras Inteligente

# Desafio

Neste desafio, você deve criar um programa que simule o auxílio de vendas de um site de catálogos de cogumelos utilizando inteligência artificial. O intuito é oferecer aos clientes sugestões de cogumelos que estão em promoção. Dessa forma, o programa deve permitir que o usuário informe o nome de um cogumelo desejado e, com base nessa informação, deve sugerir até dois cogumelos adicionais da lista, cujos valores sejam iguais ou menores que o do cogumelo selecionado pelo cliente. No caso de não haver sugestões disponíveis, ou seja, se o cogumelo escolhido for o mais caro, o programa deve exibir uma mensagem indicando que não há sugestões.

Abaixo apresentamos a lista de cogumelos oferecidos pela loja com todos os seus valores. Considere que essa lista já está ordenada por prioridade, ou seja, você deve oferecer como alternativas nessa ordem:

| Cogumelo     | Valor |
| ------------ | ----- |
| Shitake      | 10    |
| Portobello   | 8     |
| Shimeji      | 6     |
| Champignon   | 12    |
| Funghi       | 16    |
| Porcini      | 16    |

## Entrada

A entrada será uma string representando o nome do cogumelo desejado pelo usuário.

## Saída

Uma lista com no máximo 2 sugestões de cogumelos mais baratos do que o enviado como entrada. Lembrando que a sugestão das alternativas deve considerar a lista de cogumelos na ordem descrita na tabela supracitada neste desafio.

**IMPORTANTE**: Considere que cada saída (cogumelo selecionado) deve estar em linhas diferentes.

## Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada     | Saída                                      |
| ----------- | ------------------------------------------ |
| Shitake     | Portobello - Valor: 8 / Shimeji - Valor: 6 |
| Champignon  | Shitake - Valor: 10 / Portobello - Valor: 8|
| Portobello  | Shimeji - Valor: 6                         |
| Shimeji     | Desculpe, não há sugestões disponíveis.    |

## Atenção

Se você não está familiarizado com a linguagem de programação, não se preocupe! Você pode usar uma das seguintes inteligências artificiais para te ajudar a entender o código:

- ChatGPT: [https://chat.openai.com/](https://chat.openai.com/)
- Copilot: [https://copilot.microsoft.com/](https://copilot.microsoft.com/)
- Gemini: [https://gemini.google.com/](https://gemini.google.com/)
- Amazon Q (Para Empresas): [https://aws.amazon.com/pt/q/](https://aws.amazon.com/pt/q/)

Abaixo adicionamos algumas sugestões de uso e prompts para te auxiliar na resolução:

| Sugestões de Uso           | Sugestões de Prompts                                             |
| -------------------------- | ---------------------------------------------------------------- |
| Explicação de Conceitos    | Pode me explicar o que são estruturas de dados e dar exemplos?   |
| Entendimento do Problema   | Quais são as restrições ou requisitos específicos que devo considerar neste desafio? |
| Sugestões de Abordagem     | Quais são as etapas principais que devo seguir para resolver este desafio? |
| Ajuda na Depuração         | Estou recebendo um erro de sintaxe neste trecho de código. O que pode estar errado? |
| Revisão de Algoritmos      | Você pode revisar meu algoritmo de ordenação e me dar feedback sobre sua eficiência? |

# SOLUÇÃO COMENTADA:

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
