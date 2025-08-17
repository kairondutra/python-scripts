def calcula_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) com base no peso e altura fornecidos.
    """
    return peso / (altura**2)

def classifica_imc(imc):
    """
    Classifica o Índice de Massa Corporal (IMC) de acordo com os valores definidos pela tabela padrão.
    """
    tabela_imc = {
        'baixo_peso': (0, 18.4),
        'peso_normal': (18.5, 24.9),
        'sobrepeso': (25.0, 29.9),
        'obesidade_grau_1': (30.0, 34.9),
        'obesidade_grau_2': (35.0, 39.9),
        'obesidade_grau_3': (40.0, float('inf'))
    }
    
    for classificacao, limites in tabela_imc.items():
        limite_menor = limites[0]
        limite_maior = limites[1]
        if limite_menor <= imc <= limite_maior:
            return classificacao
    return "Classificacao nao encontrada"

# Dicionario de mensagens pra melhorar a saida para o usuario
mensagens_amigaveis = {
    'baixo_peso': 'Baixo Peso',
    'peso_normal': 'Peso Normal ou Saudavel',
    'sobrepeso': 'Sobrepeso',
    'obesidade_grau_1': 'Obesidade Grau I',
    'obesidade_grau_2': 'Obesidade Grau II (severa)',
    'obesidade_grau_3': 'Obesidade Grau III (morbida)'
}

while True:
    try:
        peso = float(input("peso: "))
        if peso <= 0:
            print("O peso nao pode ser zero ou negativo! Tente novamente.")
        else:
            break
    except ValueError:
        print("Por favor, digite um numero valido para o peso.")

while True:
    try:
        altura = float(input("altura: "))
        if altura <= 0:
            print("A altura nao pode ser zero ou negativa! Tente novamente.")
        else:
            break
    except ValueError:
            print("Por favor, digite um numero valido para a altura.")

imc = calcula_imc(peso, altura)
classifica_chave = classifica_imc(imc)
classificacao_amigavel = mensagens_amigaveis.get(classifica_chave, "Nao classificado")

print(f"Seu indice de IMC e {imc:.2f}, que e classificado como {classificacao_amigavel}")