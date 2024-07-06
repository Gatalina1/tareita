from optparse import Option


Saldo = 5000
print("\n Bienvenid@")
print("1. Consulta de Saldo")
print("2. Retirar Dinero")
print("3. Depositar Dinero")
print("4. Transferir Dinero a otra cuenta")
print("5. Salir")
Option = input("Seleccione una opción: ")

print()
 
if Option == '1':
    print("Su saldo actual es de ", Saldo)
elif Option == '2':
    Retirar = float(input("Ingrese la cantidad de dinero a retirar: "))
    if Retirar > Saldo:
       print("Fondos insuficientes")
    else:
        Saldo -= Retirar
        print("Su nuevo saldo es: ", Saldo)
elif Option == '3':
    deposito = float(input("Ingrese la cantidad de dinero a depositar: "))
    Saldo += deposito 
    print("Su saldo actual es de: ", Saldo) 
elif Option == '4':
    cuentaDestino = input("Ingrese el número de cuenta de destino: ")
    input("Ingresa la cantidad a depositar: ")
    print("Has transferido exitosamente a ", cuentaDestino)
    
elif Option == '5':
    print("Gracias por usar el cajero automático. ¡Hasta pronto!")
     

       