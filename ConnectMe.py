__author__ = "Johan Steven Muñoz"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "johan.munozen@campusucc.edu.co"

#Programa de consola: ConnectMe

class Contacto:
    def __init__(self, nombre, numeroTelefono, correoElectronico, cargo):
        self.nombre = nombre
        self.telefono = numeroTelefono
        self.correo = correoElectronico
        self.cargo = cargo

    def mostrar_info(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")
        print(f"Cargo: {self.cargo}")

class Agenda:
    def __init__(self):
        self.contactos = []

    def registrar_contacto(self):
        print("\n Registrar nuevo contacto")
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        correo = input("Correo Electronico: ")
        cargo = input("Cargo: ")

        # Validacion de correo repetido:
        for c in self.contactos:
            if c.correo.lower() == correo.lower():
                print("Ya existe un contacto con este correo")
                return

        nuevo = Contacto(nombre, telefono, correo, cargo)
        self.contactos.append(nuevo)
        print("Contacto registrado correctamente")

    def buscar_contacto(self):
        print("\n Buscar contacto")
        dato = input("Ingrese nombre o correo: ").lower()
        encontrados = [c for c in self.contactos if dato in c.nombre.lower() or dato in c.correo.lower()]

        if encontrados:
            print(f"\n Se encontraron {len(encontrados)} contacto(s):")
            for c in encontrados:
                c.mostrar_info()
        else:
            print("No se encontró ningún contacto")

    def listar_contactos(self):
        print("\n Lista de contactos")
        if not self.contactos:
            print("No hay contactos registrados")
        else:
            for c in self.contactos:
                c.mostrar_info()

    def eliminar_contacto(self):
        print("\n Eliminar contacto")
        correo = input("Correo de contacto a eliminar: ").lower()

        for c in self.contactos:
            if c.correo.lower() == correo:
                self.contactos.remove(c)
                print("Contacto eliminado correctamente")
                return

        print("No se encontró ningún contacto con ese correo")


def menu():
    agenda = Agenda()

    while True:
        print("\n MENÚ PRINCIPAL")
        print("1. Registrar contacto")
        print("2. Buscar contacto")
        print("3. Listar contactos")
        print("4. Eliminar contacto")
        print("5. Salir")
        print("==========================")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            agenda.registrar_contacto()
        elif opcion == "2":
            agenda.buscar_contacto()
        elif opcion == "3":
            agenda.listar_contactos()
        elif opcion == "4":
            agenda.eliminar_contacto()
        elif opcion == "5":
            print("Saliendo del programa...!")
            break
        else:
            print("Opción inválida, intente de nuevo")

# Ejecución del programa
if __name__ == "__main__":
    menu()

