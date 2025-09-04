# git config --global user.name "Baco"
# git config --global user.mail "ignacio.leyton.cornejo@gmail.com"
import agenda
while True:
    print(" ~~ MENU ~~ \n" \
    "\n" 
    "1. Agregar contacto.\n" 
    "2. Listar contacto.\n" 
    "3. Buscar contacto.\n" 
    "4. Salir.")
    decision = input("Eliga una opcion: ")
    if decision == "1":
        nombre = input("Dame el nombre: ")
        telefono = input("Dame el telefono: ")
        agenda.agregar_contacto(nombre,telefono)
        input("Aprete cualquier tecla...")
    if decision == "2":
        agenda.listar_contactos()
        input("Aprete cualquier tecla...")
    if decision == "3":
        nombre = "Dame el nombre: "
        agenda.buscar_contacto(nombre)
        input("Aprete cualquier tecla...")
    if decision == "4":
        print("Adios!")
        break
