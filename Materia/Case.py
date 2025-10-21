opc=0
saida=0


while opc != 4:
    print("1 - Para receber um bom dia")
    print("2 - Para receber uma boa tarde")
    print("3 - Para receber uma boa noite")
    print("4 - Sair")
    OPC=int(input("Introduza uma opção: "))


    match opc:
        case 1:
            print("Bom dia")
        case 2:
            print("Boa tarde")
        case 3:
            print("Boa noite")
        case 4:
            print("Adeus")
            break

'''
while saida:
    print("1 - Para receber um bom dia")
    print("2 - Para receber uma boa tarde")
    print("3 - Para receber uma boa noite")
    print("4 - Sair")
    OPC=int(input("Introduza uma opção: "))


    match opc:
        case 1:
            print("Bom dia")
        case 2:
            print("Boa tarde")
        case 3:
            print("Boa noite")
        case 4:
            print("Adeus")
            break
'''