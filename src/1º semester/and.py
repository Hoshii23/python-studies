print("veremos se vc pode se aposentar")
print("insira seu sexo(M/F), anos de contribuicao e idade ")
print("")
sexo=input()
contri=int(input())
idade=int(input())
if sexo=="F" and idade>=60 and contri>=15:
    print("pessoa apta a aposentar por idade")
elif sexo=="M" and idade>=65 and contri>=15:
    print("pessoa apta a aposentar por idade")
elif sexo=="F" and contri>=30:
    print("pessoa apta a aposentar por contribuição")
elif sexo=="M" and contri>=35:
    print("pessoa apta a aposentar por contribuição")
else:
    print("nao apto a aposentar")