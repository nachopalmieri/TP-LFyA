#Alternativa 1:

from audioop import mul
from ipaddress import summarize_address_range
from operator import truediv
from re import L

def calculator(input_operation):
    cadena_limpia = input_operation.replace(" ","")
    resultado = eval(input_operation)
    lista = list(cadena_limpia)
    resultadoFinal = 0
    listaAuxiliar = []
    ListaAux2 = []
    Posicioni = 0
    Posicionf = len(lista)
    contador = 0
    bandera = 0 
    for indice in range(Posicioni,Posicionf):
        if (lista[indice] == "+") | (lista[indice] == "-") | (lista[indice] == "/") : ##Suma, resta, division
            listaAuxiliar.append(lista[indice - 1])
            listaAuxiliar.append(lista[indice])
            listaAuxiliar.append(lista[indice + 1])
            operacionstr = "".join([str(_) for _ in listaAuxiliar])
            ListaAux2.append(resultado)
            ListaAux2.append(operacionstr)
            break
        else:
            if (lista[indice] == "*"): 
                if (lista[indice + 1] == "*"): ##Potencia
                    listaAuxiliar.append(lista[indice - 1])
                    listaAuxiliar.append(lista[indice])
                    listaAuxiliar.append(lista[indice + 1])
                    listaAuxiliar.append(lista[indice + 2])
                    operacionstr = "".join([str(_) for _ in listaAuxiliar])
                    ListaAux2.append(resultado)
                    ListaAux2.append(operacionstr)
                    break
                else: ##Multiplicacion
                    listaAuxiliar.append(lista[indice - 1])
                    listaAuxiliar.append(lista[indice])
                    listaAuxiliar.append(lista[indice + 1])
                    operacionstr = "".join([str(_) for _ in listaAuxiliar])
                    ListaAux2.append(resultado)
                    ListaAux2.append(operacionstr)
                    break
    return tuple(ListaAux2)

pasar = (input())
resultado = calculator(pasar)