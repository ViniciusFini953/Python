nota1 = input("digite a primeira nota:")
nota2 = input("digite a segunda nota:")
nota3 = input("digite a terceira nota:")
nota4 = input("digite a quarta nota;")

# vamos converter as variaveis de notas
# para o tipo float
nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float (nota3)
nota4 = float (nota4)
4
média = (nota1 + nota2 + nota3 + nota4) /4

# se a nota media do aluno for maior a 7, -> aprovado
# senão se a nota media do aluno for menor ou igual a 4, -> reprovado
# senão, -> recuperação
if média >= 7:
    print("aprovado")
elif média <= 4:
    print("reprovado")
else:
    print("recuperação")