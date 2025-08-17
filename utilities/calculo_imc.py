# -*- coding: utf-8 -*-

tabela_imc = {
    'baixo_peso': (0, 18.4),
    'peso_normal': (18.5, 24.9),
    'sobrepeso': (25.0, 29.9),
    'obesidade_grau_1': (30.0, 34.9),
    'obesidade_grau_2': (35.0, 39.9),
    'obesidade_grau_3': (40.0, float('inf'))
}

peso = float(input("peso: "))
altura = float(input("altura: "))

imc = peso / (altura**2)

print(f"Seu IMC é de: {imc:.2f}")

for classificacao, limites in tabela_imc.items():
    limite_menor = limites[0]
    limite_maior = limites[1]

    if limite_menor <= imc <= limite_maior:
        print(f"Sua classificação é: {classificacao}")
        break
