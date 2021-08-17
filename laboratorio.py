import math

def imprimir(resultadoReal,resultadoImaginario):
    tipoRespuesta = int(input("¿como quiere ver su respuesta?\n(1) de forma cartesiana\n(2) de forma polar\n(3) de forma polar y carteciana\nelija un numero: "))
    modulo = (resultadoReal**2 + resultadoImaginario**2)**(1/2)
    fase  = math.atan(resultadoImaginario/resultadoReal)
    if tipoRespuesta == 1:
        print ("la respuesta en cartesiano es: ",resultadoReal,"+ (",resultadoImaginario,")i")
    elif tipoRespuesta == 2:
        print("la respuesta en polar es: ", modulo ," < ", fase)
    elif tipoRespuesta == 3:
        print ("la respuesta en cartesiano es: ",resultadoReal,"+ (",resultadoImaginario,")i")
        print("la respuesta en polar es: ", modulo ," < ", fase)
    else:
        print("dato no valido, vuelva a intantar")
        imprimir(resultadoReal,resultadoImaginario)

def operar1Numeros(a,b,operacion,tipoCoordenadas):
    if operacion == 5:
        modulo = (a**2 + b**2)**(1/2)
        print("el modulo es: ",modulo)
    elif operacion == 6:
        resulatadoReal = a
        resultadoImaginario  = -b
        imprimir(resulatadoReal,resultadoImaginario)
    elif operacion == 7:
        if tipoCoordenadas == 1:
            modulo = (a**2 + b**2)**(1/2)
            fase  = math.atan(b/a)
            print(modulo ," < ", fase)
        else:
            resultadoReal = a * math.cos(b)
            resultadoImaginario = a * math.sin(b)
            print (resultadoReal,"+ (",resultadoImaginario,")i")
    elif operacion == 8:
        fase  = math.atan(b/a)
        print("la fase es: ", fase)

def operar2Numeros(a1,b1,a2,b2,operacion):
    if operacion == 1:
        resulatadoReal = a1 + a2
        resultadoImaginario  = b1 + b2
        imprimir(resulatadoReal,resultadoImaginario)
    elif operacion == 2:
        resultadoReal = a1 - a2
        resultadoImaginario  = b1 - b2
        imprimir(resultadoReal,resultadoImaginario)
    elif operacion == 3:
        resultadoReal = a1*a2 - b1*b2
        resultadoImaginario  = a1*b2 + a2*b1
        imprimir(resultadoReal,resultadoImaginario)
    elif operacion == 4:
        resultadoReal = (a1*a2 + b1*b2)/(a2**2 + b2**2)
        resultadoImaginario  = (b1*a2 - a1*b2)/(a2**2 + b2**2)
        imprimir(resultadoReal,resultadoImaginario)


def pedirDatos():
    tipoCoordenadas = int(input("¿en que coordenadas quiere trabajar?\n(1) cartesianas\n(2) polares\nelija un numero:"))
    
    if tipoCoordenadas < 1 or tipoCoordenadas > 2:
        print("dato del tipo de coordenadas, invalido por favor digite denuevo")
        pedirDatos()

    operacion = int(input("que operacion quiere\n(1) suma\n(2) resta\n(3) multiplicacion\n(4) division\n(5) modulo\n(6) conjugado\n(7) conversion\n(8) fase\nelija un numero:  "))
    
    if operacion == 1 or operacion == 2 or operacion == 3 or operacion == 4:
        if tipoCoordenadas == 2:
            a1p = int(input("digite el modulo del primer dato: "))
            b1p = int(input("digite la fase del primer dato: "))
            a2p = int(input("digite el modulo del segundo dato: "))
            b2p = int(input("digite la fase del primer dato: "))
            a1 = a1p * math.cos(b1p)
            b1 = a1p * math.sin(b1p)
            a2 = a2p * math.cos(b2p)
            b2 = a2p * math.sin(b2p)
        else:
            a1 = int(input("digite el dato real del primer dato: "))
            b1 = int(input("digite el dato imaginario del primer dato: "))
            a2 = int(input("digite el dato real del segundo dato: "))
            b2 = int(input("digite el dato imaginario del segundo dato: "))
        
        operar2Numeros(a1,b1,a2,b2,operacion)
    elif operacion == 5 or operacion == 6 or operacion == 7 or operacion == 8:
        if tipoCoordenadas == 2:
            a = int(input("digite el modulo: "))
            b = int(input("digite la fase: "))
        else:
            a = int(input("digite el dato real: "))
            b = int(input("digite el dato imaginario: "))
        operar1Numeros(a,b,operacion,tipoCoordenadas)
    else:
        print("dato de operacion invalido, por favor digite denuevo")
        pedirDatos()
    
pedirDatos()

