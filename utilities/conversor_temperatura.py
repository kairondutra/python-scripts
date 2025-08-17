def celsius_to_farenheit(c): return (c * 9/5) + 32
def farenheit_to_celcius(f): return (f - 32) * 5/9
def celsius_to_kelvin(c): return  c + 273.15
def kelvin_to_celsius(k): return k - 273.15
def kelvin_to_fahrenheit(k): return (k - 273.15) * 9/5 + 32
def fahrenheit_to_kelvin(f): return (f - 32) * 5/9 + 273.15

print("Bem-vindo(a) ao conversor de temperaturas!\n")
print("Escolha uma opção:")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
print("3 - Celsius para Kelvin")
print("4 - Kelvin para Celsius")
print("5 - Kelvin para Fahrenheit")
print("6 - Fahrenheit para Kelvin")
print("0 - Sair")
escolha = int(input("Escolha o tipo de conversão: "))

print()
match escolha:
    case 1:
        print(f"Escolha: Celcius para Fahrenheit")
        valor = float(input("Necessário fornecer o valor em Celcius: "))
        print(f"{valor} em Celcius é equivalente a {celsius_to_farenheit(valor)} em Fahrenheit")
    case 2:
        print(f"Escolha: Fahrenheit para Celsius")
        valor = float(input("Necessário fornecer o valor em Fahrenheit: "))
        print(f"{valor} em Fahrenheit é equivalente a {farenheit_to_celcius(valor)} em Celsius")
    case 3:       
        print(f"Escolha: Celsius para Kelvin")
        valor = float(input("Necessário fornecer o valor em Celcius: "))
        print(f"{valor} em Celcius é equivalente a {celsius_to_kelvin(valor)} em Kelvin")
    case 4:       
        print(f"Escolha: Kelvin para Celsius")
        valor = float(input("Necessário fornecer o valor em Kelvin: "))
        print(f"{valor} em Kelvin é equivalente a {kelvin_to_celsius(valor)} em Celsius")
    case 5:      
        print(f"Escolha: Kelvin para Fahrenheit")
        valor = float(input("Necessário fornecer o valor em Kelvin: "))
        print(f"{valor} em Kelvin é equivalente a {kelvin_to_fahrenheit(valor)} em Fahrenheit")
    case 6:      
        print(f"Escolha: Fahrenheit para Kelvin")
        valor = float(input("Necessário fornecer o valor em Fahrenheit: "))
        print(f"{valor} em Fahrenheit é equivalente a {fahrenheit_to_kelvin(valor)} em Kelvin")
    case 0:      
        print("Encerrando programa...")
