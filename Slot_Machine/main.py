import  random

MAX_LINES = 3
MAX_APOSTA = 100
MIN_APOSTA = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D":8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

''' Slot Machine ciclo '''

def check_vencedor(columns, lines, aposta, values):
    vencedores = 0
    vencedores_lines = []
    for line in range (lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            vencedores += values[symbol] * aposta
            vencedores_lines.append(line + 1)
    
    return vencedores, vencedores_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row], end= "")

        print()

''' User Steeps'''

def deposito():
    while True:
        quantia = input("Qual valor você gostaria de depositar? R$")
        if quantia.isdigit():
            quantia = int(quantia)
            if quantia > 9.99:
                break
            else:
                print("O valor mínimo tem que ser acima de R$9,99.")
        else: 
            print("Por favor inclua um número.")
    
    return quantia 

def get_number_of_lines():
    while True: 
        lines = input("Insira a quantidade de linhas que deseja apostar (1-" + str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Coloque o um número válido de linha")
        else:
            print("Por favor inclua um número")
    
    return lines

def get_aposta():
    while True: 
        quantia = input("Qual valor que deseja apostar na linha desejada? R$")
        if quantia.isdigit():
            quantia = int(quantia)
            if MIN_APOSTA <= quantia  <= MAX_APOSTA:
                break
            else:
                print(f"O valor deve ser entre R${MIN_APOSTA} - R${MAX_APOSTA}. ")
        else: 
            print("Por favor inclua um número.")
    
    return quantia

''' MAIN Program'''

def main():
    saldo = deposito()
    lines = get_number_of_lines()

    while True:
        aposta = get_aposta()
        total_aposta = aposta * lines

        if total_aposta > saldo:
            print(f"Você não possui saldo o suficiente para apostar, atualmente seu saldo contém: R${saldo}")
        else: 
            break

    print(f"Você está apostando R${aposta} em {lines} linhas. Total de aposta é igual a : R${total_aposta}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    vencedores, vencedores_lines = check_vencedor(slots, lines, aposta, symbol_value)
    print(f"Você ganhou R${vencedores}.")
    print(f"Você ganhou nas linhas: ", *vencedores_lines)
main()