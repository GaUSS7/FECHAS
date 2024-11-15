from datetime import *

def leerfecha(mensaje,meses):
    while True:
        try:
            fecha = (input(mensaje+"Ingrela en este formato dd/mm/aaaa: "))
            dia = int(fecha[0:2])
            mes = int(fecha[3:5])
            anio = int(fecha[6:])
            
            if anio<1994 or anio>2114:
                print("El valor de año no es procesable")
                continue
            if not mes in meses:
                print(f"Este mes {mes} no valido")
                continue
            tupla=meses.get(mes)
            if mes != 2:
                if dia<1 or dia > tupla[1]:
                    print(f"No es una fecha valida {mes}")
                    continue
                else:
                    return fecha
            else:
                if anio%4==0:
                    if dia<1 or dia>29:
                        print(f"El fecha no es valida: {fecha}")
                        continue
                    else:
                        if dia<1 or dia>tupla[1]:
                            print(f"El fecha no es valida: {fecha}")
                        else:
                            return fecha
        except ValueError:
            print(f"La fecha {mes} no se procesable")
            
        
        

def actulaDate():
    now=datetime.now()
    showTime=now.strftime("%d/%m/%Y")  
    return showTime



def correcionFehas(fechaActual,FechaIngresada):
        #rebanadas de la fecha actual
        dayAC=int(fechaActual[0:2])
        monthAC=int(fechaActual[3:5])
        yearAC=int(fechaActual[6:])
        #rebanadas de la fecha ingreasda por el usuario
        dayING=int(FechaIngresada[0:2])
        monthING=int(FechaIngresada[3:5])
        yearING=int(FechaIngresada[6:])
        
        if yearAC==yearING and monthAC==monthING and dayAC==dayING:
            return False, "Ambas fechas no pueden ser iguales"
             
        if yearING>yearAC:
            return False , f"La fecha ingreada no puede ser mayor al fecha actual, fecha ingresada: {FechaIngresada} y fecha actual: {fechaActual}"
        
        if  monthING > monthAC and (yearING==yearAC or yearING!=yearAC):
            return False ,f"El mes ingreado es mayor al mes de la fecha actual, registre una fecha valida: {FechaIngresada} y fecha actual: {fechaActual}"
    
        if (yearING==yearAC or yearING<yearAC) and (dayAC != dayING and monthING <= monthAC):
            return True,  f"Ingrese una fecha. (la fecha debe ser menor a la actual {fechaActual}):"
        
        
        

        
def calculaEdad(fechaIngresada,fechaActual1):
     #rebanadas de la fecha actual
        dayAC=int(fechaActual1[0:2])
        monthAC=int(fechaActual1[3:5])
        yearAC=int(fechaActual1[6:])
        #rebanadas de la fecha ingreasda por el usuario
        dayING=int(fechaIngresada[0:2])
        monthING=int(fechaIngresada[3:5])
        yearING=int(fechaIngresada[6:])
        #calculo de la edad y meses
        edad_anios = yearAC - yearING
        meses = monthAC - monthING
        if (monthAC, dayAC) < (monthING, dayING):
            edad_anios -= 1
        # Cálculo de los meses adicionales
        if meses < 0:
            meses += 12
        
        return edad_anios,meses
                



    



