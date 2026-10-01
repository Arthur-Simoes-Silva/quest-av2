from functions import depositar,sacar

saldo = 0
opcao = 0

while(True):
    print("SISTEMA BANCÁRIO")
    print("1- Depositar")
    print("2- Sacar")
    print("3- Encerrar o Programa")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Inválido, insira um número.")
        continue
         
    match opcao:
        case 1:
            while(True):
                print("\nDEPÓSITO")
                try:
                    quantia = int(input("Informe a quantia a ser depositada: "))
                    saldo = depositar(quantia,saldo)
                    print(f"Saldo atual: {saldo} R$")
                    break

                except ValueError:
                    print("Inválido, Tente novamente.")
        case 2:
                    while(True):
                        print("\nSAQUE")
                        try:
                            valor = int(input("Informe a quantia a ser sacada: "))
                            saldo = sacar(valor,saldo)
                            print(f"Saldo atual: {saldo} R$")
                            break
        
                        except ValueError:
                            print("Inválido, Tente novamente.")
        case 3:
              print("\nPrograma Encerrado.")
              break
       
        case _:
              print("\nOpção Inválida")
              
