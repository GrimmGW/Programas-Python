class Television:
    def __init__(self):
        print("La TV esta Apagada.")

    @staticmethod
    def Boton(Encender = "off"):
        if Encender == "off":
            Encender = "on"
            print("El interruptor esta en ON.")
        else:
            if Encender == "on":
                Encender = "off"

                print("El interruptor esta ahora en OFF.")

    @staticmethod
    def Volumen(volumen=0):
        Subir_bajar = input("Desea Subir o Bajar volumen? (subir/bajar)")
        if Subir_bajar == "s":
            cantidad = int(input("cuanto? (Ingrese un Numero): "))
            volumen += cantidad
            if volumen > 10:
                volumen = 10
            print("El Volumen esta en: ", volumen)
        elif Subir_bajar == "b":
            cantidad = int(input("Cuanto? (Ingrese un Numero): "))
            volumen -= cantidad
            if volumen < 0:
                volumen = 0
            print("El Volumen esta ahora en: ", volumen)

    @staticmethod
    def Canal(canal=1):
        new_canal = int(input("Que canal deseas ver? (ingrese un numero del 1 al 10): "))
        if new_canal < 1 or new_canal > 10:
            print("No existe ese canal")
        else:
            channel = new_canal
            print("Estas en el canal: ", channel)


def Inicio():
    tv = Television()

    opcion2 = None
    while opcion2 != "0":
        print("""Television calidAd
                0) - Salir
                1) - Apagar o Prender la TV
                2) - Subir o Bajar el Volumen
                3) - Cambiar el Canal
                """)

        opcion = input("Escoger: ")
        print()
        if opcion == "0":
            print("Hasta Luego.")
            break
        elif opcion == "1":
            tv.Boton()
        elif opcion == "2":
            tv.Volumen()
        elif opcion == "3":
            tv.Canal()
        else:
            print("\nOpcion Invalida")


Inicio()
