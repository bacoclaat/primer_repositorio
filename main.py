# git config --global user.name "Baco"
# git config --global user.mail "ignacio.leyton.cornejo@gmail.com"
import agenda
while True:
    print(" ~~ MENU ~~ \n" \
    "\n" \
    "1. Agregar contacto." \
    "2. Listar contacto." \
    "3. Buscar contacto" \
    "4. Salir.")
    decision = input("Eliga una opcion")
    if decision == "1":
        nombre = input("Dame el nombre: ")
        telefono = input("Dame el telefono: ")
        agregar_contacto(nombre,telefono)
