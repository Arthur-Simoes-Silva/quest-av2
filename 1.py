
# 1° Questão

print("Informe dois números para serem divididos")
while(True):
    try:

        nmr1 = int(input("Informe o primeiro número: "))
        nmr2 = int(input("Informe o segundo número: "))

        resultado = nmr1 / nmr2

    except ValueError:
        print("Digite apenas números!")

    except ZeroDivisionError:
        print("Não é possível dividir por 0")

    else:
        print(resultado)
        break

