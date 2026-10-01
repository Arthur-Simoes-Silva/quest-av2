from functions import carga_horaria

print("SISTEMA DE CARGA HORÁRIA")

while(True):
    try:
        horas = int(input("Informe o número de horas trabalhadas: "))
        carga_horaria(horas)
        break

    except ValueError:
        print("Inválido! Insira um número por favor.")