#Funções

#Área Círculo

def exibir_menu():
    print(f'{'-'*30}ESCOLHA A OPÇÃO DESEJADA{'-'*30}\n')

    print('Digite 1: para calcular a área de um CÍRCULO.')
    print('Digite 2: para calcular a área de um TRIÂNGULO.')
    print('Digite 3: para calcular a área de um TRAPÉZIO.')
    print('Digite 4: para SAIR do programa.\n')

#Área Círculo

def calcular_circulo(r):
    area = 3.14 * r ** 2
    return area

#Área Triângulo

def calcular_triangulo(base, altura):
    area = (base * altura) / 2
    return area

#Área Trapézio

def calcular_trapezio(base_maior, base_menor, altura):
    area = ((base_maior + base_menor) * altura) / 2
    return area


#Programa Principal

while True:

    exibir_menu()
    opcao = int(input('Informe a opção desejada: '))

    #Laço de Repetição

    match opcao:
        case 1:
            print('Área do círculo: area = π*r²')
            r = float(input('Informe o raio do círculo: '))
            print(f'Área do círculo: {calcular_circulo(r)}.')
            continue
        case 2:
            print('Área do triângulo: area = (base * altura) / 2')
            base = float(input('Informe a base do triângulo: '))
            altura = float(input('Informe a altura do triângulo: '))
            print(f'Área do triângulo: {calcular_triangulo(base, altura)}.')
            continue
        case 3:
            print('Área do trapézio: area = (base maior + base menor) * altura / 2')
            base_maior = float(input('Informe a base maior do trapézio: '))
            base_menor = float(input('Informe a base menor do trapézio: '))
            altura = float(input('Informe a altura do trapézio: '))
            print(f'Área do trapézio: {calcular_trapezio(base_maior, base_menor, altura)}.')
            continue
        case 4:
            break
        case _:
            print('Opção Inválida')
            continue