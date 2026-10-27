saldo = 1000

def consultar_saldo(saldo):
    print("su saldo actual es de: $", saldo)

    return saldo   

def depositar_saldo(saldo):
    deposito = int(input("ingresa el valor a depositar: "))
    
    if deposito > 0:
        saldo = saldo + deposito
        print("Deposito realizado. Su nuevo saldo es de: $", saldo)
        

    elif deposito == 0:
        print("valor no valido para depositar")
        
    
    else:
        print("el valor a depositar no es valido")
        

    return saldo

def retirar_saldo(saldo):
    retiro = int(input("cual es su valor a retirar? :"))
    if retiro < saldo:
        saldo = saldo - retiro
        print("retiro exitoso, su nuevo saldo es de: $", saldo)
        return saldo
    
    elif retiro == 0:
        print("valor de retiro, no valido")
        return retiro

    else:
        retiro > saldo
        print("no tienes suficiente denero para este retiro")
        return retiro

#MENU

print("===CAJERO AUTOMATICO===")
print("1.Consultar saldo")
print("2.Depositar dinero")
print("3.Retirar dinero")
print("0.Salir")

opcion = int(input("escriba el numero relacionado con lo que desea hacer:"))

if opcion == 1:
    consultar_saldo(saldo)

elif opcion == 2:
    depositar_saldo(saldo)

elif opcion == 3:
    retirar_saldo(saldo)
    
elif opcion == 0:
    print("gracias por usar nuestro cajero. vuelva pronto")

else:
    print("opcion no valida")
    