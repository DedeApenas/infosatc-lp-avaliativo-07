mediaNota = lambda nota1,nota2: round(nota1 * 0.4 + nota2 * 0.6) #round pra arredondar

def conceito(mediaAluno):
    if mediaAluno<=5.0 and mediaAluno>=0:
        letra="D"
    elif mediaAluno<=7.0 and mediaAluno>5.0:
        letra="C"
    elif mediaAluno<9.0 and mediaAluno>7.0:
        letra="B"
    elif mediaAluno>=9 and mediaAluno<=10:
        letra="A"
    return letra

for x in range (0,10):
    nota1=float(input("Digite sua Primeira Nota:"))
    nota2=float(input("Digite sua Segunda Nota:"))
    mediaAluno = mediaNota(nota1,nota2)
    letraConceito = conceito(mediaAluno)
    print("Sua média é de:",mediaAluno,"Conceito",letraConceito)
 