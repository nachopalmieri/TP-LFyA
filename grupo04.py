from ast import NotIn
from ntpath import join
from operator import index


operandos = ["0","1","2","3","4","5","6","7","8","9"]
operadores = ["-","+","/","*","^"] ## Ordenados por peso


def calculator(input_operation):
    
    ## Convertimos ** a ^
    ## Trabajamos los caso en los que haya * o / seguidos de un -
    ecuacion_limpia = input_operation.replace(" ", "")
    ecuacion = list(ecuacion_limpia)
    contador = 0
    for caracter in ecuacion:
        if caracter == "*":
            if  ecuacion[contador+1] == "*":
                ecuacion[contador] = "^"
                ecuacion[contador+1] = ""
            elif ecuacion[contador+1] == "-":
                indiceNegativo = contador + 1
                numeroNegativo = ecuacion[contador + 2]
                ecuacion[indiceNegativo] = str(float(numeroNegativo) * (-1))
                ecuacion[contador+2] = ""
        elif caracter == "/":
            if ecuacion[contador+1] == "-":
                indiceNegativo = contador + 1
                numeroNegativo = ecuacion[contador + 2]
                ecuacion[indiceNegativo] = str(float(numeroNegativo) / (-1))
                ecuacion[contador+2] = ""
        contador = contador + 1
    for item in ecuacion:
        if item == "":
            ecuacion.remove(item)

    
    resultadoEval = eval(ecuacion_limpia) ## Resuelve la cadena entera
    str(resultadoEval)
    resultadoFinal = 0

    banderaPrimeraOperacion = 0
    while (resultadoEval != resultadoFinal):
        indice_apertura, indice_cierre = buscar_bloque(ecuacion)

        ## Evaluar lo que hay dentro de ese bloque
        operadores_bloque=[]
        for indice in range(indice_apertura, indice_cierre):
            caracter = ecuacion[indice]
            if caracter in operadores:
                peso = operadores.index(caracter)
                operadores_bloque.append([caracter,indice,peso])

        ## Teniendo los operadores dentro del bloque
        ## empezar a operarlos
        operadores_bloque.sort(key= lambda op : op[2], reverse=True)
        bandera = 0

        longitudOperadores_bloque = len(operadores_bloque)
        for item in operadores_bloque:
            operador, indice , peso = item
            
            ## Acomodamos los indices en caso de requerirlo
            if bandera != 0:
                operadores_bloque.pop(bandera-1)
                for item2 in operadores_bloque:
                    if (indice < item2[1]):
                        indice = indice - 2

            ## Operamos segun el peso o prioridad de operadores
            if operador=="*":
                resultado = float(ecuacion[indice-1]) * float(ecuacion[indice+1])
            elif operador=="/":
                resultado = float(ecuacion[indice-1]) / float(ecuacion[indice+1])
            elif operador=="+":
                resultado = float(ecuacion[indice-1]) + float(ecuacion[indice+1])
            elif operador == "-":
                resultado = float(ecuacion[indice-1]) - float(ecuacion[indice+1])
            elif operador == "^":
                resultado = float(ecuacion[indice-1]) ** float(ecuacion[indice+1])

            ## Guardamos primera operacion
            if banderaPrimeraOperacion == 0:
                primeraOperacion = str(ecuacion[indice-1])+operador+(ecuacion[indice+1])
                banderaPrimeraOperacion = 1
            
            ## Eliminamos los operandos ya utilizados
            ecuacion.pop(indice)
            ecuacion.pop(indice)
            ecuacion[indice-1] = resultado

            ## Eliminamos parentesis
            if (bandera == longitudOperadores_bloque - 1):
                if (len(ecuacion) != 1):
                    ecuacion.pop(indice)
                    ecuacion.pop(indice-2)
            bandera = bandera + 1
        
        ## Si solo queda un elemento en la lista, es el valor final
        if len(ecuacion) == 1:
            resultadoFinal = ecuacion[0]
    tupla = (resultadoFinal, primeraOperacion)
    return tupla


def buscar_bloque(ecuacion):
    ## Encontrar bloques () mas internos y a la izquierda posible
    if ")" in ecuacion:
        indice_cierre = ecuacion.index(")")

        caracter=""
        indice = indice_cierre
        while(caracter != "("):
            indice = indice - 1
            caracter = ecuacion[indice]

        indice_apertura = indice
    else:
        indice_apertura = 0
        indice_cierre = len(ecuacion)-1
    return indice_apertura, indice_cierre


resultado = calculator(input())
