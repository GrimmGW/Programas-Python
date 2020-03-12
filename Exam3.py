import os.path
import time
# Usuario admin
# Escribir Admin en el menu de inicio e ingrese los siguientes datos para entrar:
# Usuario: Grimm
# Clave: 1234


class Inicio:
    def __init__(self):
        pass

    @staticmethod
    def Crear():
        filename = 'Usuario.txt'
        with open(filename, 'a') as f:
            f.write(str(input('Usuario Nuevo: ') + '\n'))
        filename = 'Clave.txt'
        with open(filename, 'a') as f:
            f.write(str(input('Clave  Nueva: ')+'\n'))
        Menu_1()

    @staticmethod
    def In_Sesion():
        menu = Inicio
        print('Iniciar Sesion')
        Usuario = str(input('Usuario: '))
        Clave = str(input('Clave: '))
        if Usuario+'\n' == open('Usuario.txt').read() and Clave+'\n' == open('Clave.txt').read():
            print('Inicio exitoso!')
            menu.Menu_2()
        else:
            print('Inicio incorrecto')
            Menu_1()

    @staticmethod
    def Admin():
        menu = Inicio
        print('Bienvenido Administrador')
        print('Ingrese el Usuario Administrador: ')
        A_Nom = input()
        if A_Nom == 'Grimm':
            print('Ingrese su Clave: ')
            A_Clave = input()
            if A_Clave == '1234':
                print('Bienvenido, Grimm')
                print('''Que desea hacer?
                1) Ver todos los Usuarios
                2) Eliminar Usuarios
                3) Salir''')
                print('')
                opc2 = int(input('Escoger: '))
                if opc2 == 1:
                    archive2 = open('Usuario.txt', 'r')
                    mensaje = archive2.read()
                    print(mensaje)
                    archive2.close()
                elif opc2 == 2:
                    fin = open('Usuario.txt', 'r')
                    fout = open('Usuario.txt', 'w')
                    for linea in fin:
                        if linea != linea:
                            fout.write(linea)
                    fout.close()
                    fin.close()
                    menu.Admin()
                elif opc2 == 3:
                    print('Saliendo...')
                    Menu_1()
                else:
                    print('Opcion Invalida')
                    menu.Admin()
            else:
                print('Opcion Invalida')
                menu.Admin()
        else:
            print('Opcion Invalida')
            menu.Admin()

    @staticmethod
    def Menu_2():
        menu = Inicio()
        global respuesta
        print('Que desea hacer?')
        print('''1) Utilizar la Calculadora
2) Cerrar Sesion''')
        print('')
        opc = int(input('Escoger: '))
        if opc == 1:
            print("Ingrese el primer numero: ")
            n1 = int(input())
            print("Ingrese el segundo numero: ")
            n2 = int(input())
            print("""Escoga una operacion:
                       1- Suma
                       2- Resta
                       3- Multiplicacion
                       0- Division""")
            opcion = int(input())
            if opcion == 1:
                respuesta = n1 + n2
            elif opcion == 2:
                respuesta = n1 - n2
            elif opcion == 3:
                respuesta = n1 * n2
            elif opcion == 4:
                respuesta = n1 / n2
            else:
                print('Comando desconocido, vuelva a intentarlo')
            print('Resultado: ', respuesta)
            menu.Menu_2()
        if opc == 2:
            print(':D')
            Menu_1()


def Menu_1():
    menu = Inicio
    print()
    print('Seleccione una opcion')
    print("""1) Iniciar sesion
2) Registrarse
3) Salir""")
    opc = input()
    if opc == '1':
        if os.path.exists('Usuario.txt'):
            menu.In_Sesion()
        else:
            print('Usuario no Encontrado!')
            Menu_1()
    elif opc == '2':
        menu.Crear()
    elif opc == '3':
        print('Hasta Luego!')
    elif opc == 'admin':
        menu.Admin()
    else:
        print('Opcion Invalida')
        Menu_1()


print('\033[0:34:36m Bienvenido!')
Menu_1()