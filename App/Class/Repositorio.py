from Class import Energy
from Class import Connection
#Exibi a lista dos planos disponiveis e guarda cada um em uma variável
def alterarEnergia():
 planos = Energy.listarPlano()
 c = 3

 while c < (len(planos)) - 1:
    if (planos[c]).find("*") != -1:
        Atual = planos[c][28:64]
    if (planos[c]).find("Equilibrado") != -1:
        Equilibrado = planos[c][28:64]
    elif (planos[c]).find("Economia de energia") != -1:
        Economia = planos[c][28:64]
    elif (planos[c]).find("Alto desempenho") != -1:
        Desempenho = planos[c][28:64]
    c+=1

#Definir o plano de acordo com o fluxo
 fluxo = Connection.getFluxo()
 if(fluxo >= 50):
    gid = Desempenho
    nome = "Desempenho"
 elif(fluxo > 14 and fluxo < 50):
    gid = Equilibrado
    nome = "Equilibrado"
 else:
    gid = Economia
    nome = "Economia"

#Validação do plano, e troca do plano
 if(gid == Atual):
    print("Plano Atual já está de acordo com o fluxo!")
    return nome
 else:
    trocar = Energy.alterarPlano(gid)
    print(trocar)
    return nome