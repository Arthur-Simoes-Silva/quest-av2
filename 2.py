# 2° Questão

lista_notas = []
contador = 0

while contador < 3:
    nota = float(input("Insira a nota: "))
    if nota >= 0 and nota <= 10:
        contador+=1
        lista_notas.append(nota)
    else:
        print("Nota inválida!")

media = sum(lista_notas) / len(lista_notas)

print(lista_notas)
print(media)