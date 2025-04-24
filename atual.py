from nltk.tokenize.toktok import ToktokTokenizer
from dicionarios import palavras_positivas, palavras_negativas, palavras_neutras, palavras_negacao, atenuadores, intensificadores

tokenizer = ToktokTokenizer()

nome = input("Olá! Qual é o seu nome? ")
idade = input("Quantos anos você tem, {}? ".format(nome))
print(f"\nSeja bem-vindo(a), {nome}! Vamos analisar sentimentos nas suas frases. 😊\n")

# Função para verificar multiplicador e peso
def verificar_multiplicador_e_peso(palavra):
    if palavra in intensificadores:
        return 3, 1.25  # Intensificador
    elif palavra in atenuadores:
        return 0.5, 0.75  # Atenuador
    return 1, 1  # Normal

# Função de análise de sentimento
def analisar_sentimento(frase):
    palavras = tokenizer.tokenize(frase.lower())

    score_total = 0
    soma_positivos = 0
    soma_negativos = 0
    sentimento_count = {"neutro": 0}
    alcance_negacao = 0

    multiplicador = 1

    for palavra in palavras:
        novo_multiplicador, _ = verificar_multiplicador_e_peso(palavra)
        if novo_multiplicador != 1:
            multiplicador *=novo_multiplicador
            continue

        if palavra in palavras_negacao:
            alcance_negacao = 2
            continue

        inverter = alcance_negacao > 0

        if palavra in palavras_positivas:
            score = palavras_positivas[palavra] * multiplicador
            score_total += -score if inverter else score
            soma_positivos += abs(score) if not inverter else 0
            soma_negativos += abs(score) if inverter else 0

        elif palavra in palavras_negativas:
            score = palavras_negativas[palavra] * multiplicador
            score_total += -score if inverter else score
            soma_negativos += abs(score) if not inverter else 0
            soma_positivos += abs(score) if inverter else 0
        elif palavra in palavras_neutras:
            sentimento_count["neutro"] += 1

        multiplicador = 1
        if alcance_negacao > 0:
            alcance_negacao -= 1
    total_valores = soma_positivos + soma_negativos

    if total_valores > 0:
        porcentagem_sentimentos = {
            "positivo": (soma_positivos / total_valores) * 100,
            "negativo": (soma_negativos / total_valores) * 100,
            "neutro": (sentimento_count["neutro"])
        }
    else:
        porcentagem_sentimentos = {"positivo": 0, "negativo": 0, "neutro": 100}

    sentimento = "Sentimento POSITIVO 😊" if score_total > 0 else \
                 "Sentimento NEGATIVO 😞" if score_total < 0 else \
                 "Sentimento NEUTRO 😐"

    return sentimento, porcentagem_sentimentos, score_total

# Pergunta para o usuário
sentimento = input("O que está sentindo? (ou 'sair' para encerrar): ")
if sentimento.lower() == 'sair':
    print("ENCERRANDO PROGRAMA.")
else:
    resultado, porcentagem_sentimentos, score_total = analisar_sentimento(sentimento)
    print(f"\nResultado: {resultado}")
    print(f"Porcentagem de palavras positivas: {porcentagem_sentimentos['positivo']:.2f}%")
    print(f"Porcentagem de palavras negativas: {porcentagem_sentimentos['negativo']:.2f}%")
    print(f"Quantidade de palavras neutras: {porcentagem_sentimentos['neutro']}")
    print(f"Score Total: {score_total:.2f}")
    print("\nObrigado por compartilhar. Fique bem! 🌟")
