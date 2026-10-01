lista_notas = []

while(True):
    try:
        alunos = int(input("Quantos alunos deseja informar a nota: "))
        break
    except ValueError:
        print("Inválido, insira um número")
        continue

for i in range (alunos):
    while(True):
        try:
            notas = float(input("Digite a nota: "))
            if notas >= 7:
                lista_notas.append(notas)
            break

        except ValueError:
            print("Inválido, Tente novamente")
            continue

print(lista_notas)