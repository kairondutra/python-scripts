import random

minusculas = "abcdefghijklmnopqrstuvwxyz"
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>/?"

tamanho = int(input("Informe o tamanho da senha: "))
usar_maiusculas = input("Deve conter letras maiusculas? (y/n): ").lower() == "y"
usar_numeros = input("Deve conter números? (y/n): ").lower() == "y"
usar_simbolos = input("Deve conter símbolos? (y/n): ").lower() == "y"

caracteres = minusculas
if usar_maiusculas:
    caracteres += maiusculas
if usar_numeros:
    caracteres += numeros
if usar_simbolos:
    caracteres += simbolos

senha = "".join(random.choice(caracteres) for _ in range(tamanho))
print(f"Senha gerada: {senha}")