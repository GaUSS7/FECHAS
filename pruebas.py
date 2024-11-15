from fecha import *


meses={
    1: ('enero',31),
    2: ('febrero',29),
    3: ('marzo',31),
    4: ('abril',30),
    5: ('mayo',31),
    6: ('junio',30),
    7: ('julio',31),
    8: ('agosto',31),
    9: ('septiembre',30),
    10: ('octubre',31),
    11: ('noviembre',30),
    12: ('diciembre',31),
} 

       
lisFechasING=[]
currentDate=actulaDate()
mensajaPrin=f"Ingrese una fecha. (la fecha debe ser menor a la actual {currentDate}): "
print(f"La fecha actual es: {currentDate}")
while True:
    askDate=leerfecha(mensajaPrin,meses)
    print(f"La fecha ingresada es: {askDate}")
    print("\n")
    vlaidacion,mensajaPrin=correcionFehas(currentDate,askDate)
    edad,mesesp=calculaEdad(askDate,currentDate)
    
    if vlaidacion:
        print("Fechas registradas")
        lisFechasING.append((askDate,edad,mesesp))
        exiT=input("Desea ingresar otra Fecha ? (S/N): ")
        if exiT in ("N","n"):
            break

print(f"La fecha ingresada es: {askDate} y la fecha actual es: {currentDate}")
print("*" * 60)
print("Registro  de Fechas".center(60))
print("*" * 60)
print('Fecha actual'.ljust(15), 'fecha Ingresada'.center(15), 'Edad'.center(15), 'Meses'.center(15))
for DateING,Edad,Meses in lisFechasING :
    print(currentDate.ljust(15),DateING.center(15),str(Edad).center(15),str(Meses).center(15))
print("*" * 60)



