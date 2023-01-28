import pandas as pd
import pyfiglet

def is_valid_credit_card(card_number):
    """
    Validate a credit card number using the Luhn algorithm.
    """
    # Reverse the credit card number
    card_number = card_number[::-1]
    # Convert to integer
    card_number = [int(x) for x in card_number]
    # Double every second digit
    for i in range(0, len(card_number), 2):
        card_number[i] *= 2
        # Subtract 9 from numbers over 9
        if card_number[i] > 9:
            card_number[i] -= 9
    # Sum all digits
    sum_digit = sum(card_number)
    # Return True if sum is divisible by 10, else False
    if sum_digit % 10 == 0:
        return True
    else:
        return False

# Crear una lista vacía para almacenar los números de tarjeta de crédito
credit_cards = []

# imprimir el logo
ascii_banner = pyfiglet.figlet_format("BINSverify")
print(ascii_banner)
print ("by LOUISSTANICA")
print("")

# Preguntar al usuario cuántas tarjetas de crédito desea ingresar
num_cards = int(input("¿Cuántas tarjetas de crédito desea ingresar? "))

# Pedir al usuario que ingrese los números de tarjeta de crédito
for i in range(num_cards):
    card_number = input(f"Ingrese el número de tarjeta de crédito {i+1}: ")
    # Verificar si el número de tarjeta de crédito es válido
    valid = is_valid_credit_card(card_number)
    # Agregar el número de tarjeta de crédito y su validez a la lista
    credit_cards.append({"Número de tarjeta": card_number, "Válida": valid})

# Crear un dataframe a partir de la lista de tarjetas de crédito
df = pd.DataFrame(credit_cards)

# Imprimir la tabla de tarjetas de crédito
print(df)
