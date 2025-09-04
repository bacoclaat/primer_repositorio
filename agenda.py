#Agenda
contacto = []
def agregar_contacto(nombre,telefono):
    contacto.append({"nombre": nombre, "telefono": telefono})

def listar_contactos():
    print("\nLista de contactos : ")
    for c in contactos:
        print(f"{c["nombre"]} - {c["telefono"]}")

nombre = input("Ingrese el nombre: ")
telefono = input("Ingrese el telefono: ")
agregar_contacto(nombre,telefono)
print("Contacto Agregado")