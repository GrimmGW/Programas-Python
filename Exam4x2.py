from os import system


class paciente:
    def __init__(self, nombre, apellido, nacimiento, pais, genero, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.pais = pais
        self.edad = edad
        if genero == "1":
            self.genero = "Hombre"
        elif genero == "2":
            self.genero = "Mujer"
        self.estatus = "Sospechoso"

    def mostrar(self):
        system('cls')
        print('\033[1:31m ')
        print('|///////////////////|')
        print('| MOSTRAR PACIENTES |')
        print('|///////////////////|')
        print('\033[0:0m ')
        return f'\nGenero: {self.genero}\nNombre: {self.nombre}\nApellido: {self.apellido}' \
               f'\nFecha de Nacimiento: {self.nacimiento}\nPais: {self.pais}' \
               f'\nEdad: {self.edad}\nEstatus: {self.estatus}\n '


ListaP = list()


def pacientes():
    pass


def ModStatus(patients):
    NuevoPaciente = paciente('', '', '', '', '', '')
    if not patients:
        print('No hay Pacientes Agregados')
        print('''Agregar uno?
        
        > Si
        > No''')
        Principal()
    else:
        while True:
            print('\033[1:33m ')
            print('|///////////////////////////|')
            print('|      OPCION MODIFICAR     |')
            print('|///////////////////////////|')
            print('\033[0:0m ')
            print('1-Hacer un diagnostico')
            print('2-Cambiar estatus a Facellecido')
            print('3-Cambiar estatus a Curado')
            print('4-Cambiar estatus manualmente (sospechoso/activo/descartado')
            print('5-Volver')
            try:
                opc = int(input('Opcion: '))
                if 0 < opc < 5:
                    nombre = input('Ingrese el Nombre: ')
                    break
                elif opc == 5:
                    Principal()
            except:
                system('cls')
                print('Opcion Invalida')
                input()
        Recorrer = 0
        while nombre != NuevoPaciente.nombre:
            try:
                NuevoPaciente = patients[Recorrer]
                Recorrer += 1
            except:
                system('cls')
                print('No Encontrado!')
                input()
                print('')
                ModStatus(patients)
        if nombre == NuevoPaciente.nombre:
            print(NuevoPaciente.nombre)
            print('Encontrado!')
            print('')
            if opc == 1:
                try:
                    print('A continuacion, se le debe realizar al Paciente las siguientes preguntas')
                    print('Responda honestamente:')
                    print(' ')
                    Tos = Diagnosticar(input('Tiene Tos Seca? si/no\n'))
                    if not Tos:
                        Flema = Diagnosticar(input('Tiene con Flema? si/no\n'))
                    else:
                        Flema = False
                    Respirar = Diagnosticar(input('Le Cuesta Respirar? o, Siente que le Falta el Aire? si/no\n'))
                    Fiebre = Diagnosticar(input('Tiene fiebre? si/no\n'))
                    if Tos == True and Respirar == True and Fiebre == True:
                        print('Posee COVID-19')
                        NuevoPaciente.estatus = 'COVId-19 Activo'
                    elif Flema == True and Fiebre == True or Flema == True and Fiebre == False:
                        print('Usted PUEDE tener COVID-19')
                        NuevoPaciente.estatus = 'Sospechoso (Gripe)'
                    else:
                        print('Usted PUEDE tener COVID-19')
                        NuevoPaciente.estatus = 'Descartado (Alergia)'
                except:
                    ModStatus(patients)
            if opc == 2:
                while True:
                    system('cls')
                    respuesta = input('Este Paciente Falleció? si/no\n')
                    if respuesta.upper() == 'SI':
                        print('Este Paciente ha Fallecido D:')
                        NuevoPaciente.estatus = "Fallecido"
                        ModStatus(patients)
                    elif respuesta.upper() == 'NO':
                        ModStatus(patients)
                    else:
                        print('Ingrese una Opcion Valida.\n')
            if opc == 3:
                while True:
                    system('cls')
                    respuesta = input('Este Paciente se Recuperó? si/no\n')
                    if respuesta.upper() == 'SI':
                        NuevoPaciente.estatus = "Recuperado"
                        print('Hecho!\n\n')
                        ModStatus(patients)
                    elif respuesta.upper() == 'NO':
                        ModStatus(patients)
                    else:
                        print('Ingrese una Opcion Valida.')
            if opc == 4:
                while True:
                    system('cls')
                    print('1-Sospechoso')
                    print('2-Activo')
                    print('3-Descartado (Gripe/Fiebre)')
                    print('4-Volver')
                    opc2 = input('Opcion: ')
                    if opc2 == '1':
                        NuevoPaciente.estatus = "Sospechoso"
                        ModStatus(patients)
                    elif opc2 == '2':
                        NuevoPaciente.estatus = "Posee COVID-19"
                        ModStatus(patients)
                    elif opc2 == '3':
                        while opc2 != '1' and opc2 != '2':
                            print('''1) Gripe
                                2) Fiebre''')
                            opc2 = input('Opcion:')
                            if opc2 == '1':
                                NuevoPaciente.estatus = "Descartado (Gripe)"
                                ModStatus(patients)
                            elif opc2 == '2':
                                NuevoPaciente.estatus = "Descartado (Fiebre)"
                                ModStatus(patients)
                            else:
                                print('Opcion Invalida')
                                print('')
                    elif opc2 == '4':
                        ModStatus(patients)
                    else:
                        print('Opcion Invalida')
                        ModStatus(patients)

def AcercaDe():
    print('\033[1:30m ')
    print('COVID-19:')
    print('\033[0:0m ')
    print('''La COVID-19 es una enfermedad infecciosa causada por un nuevo
virus que no había sido detectado en humanos hasta la fecha.

El virus causa una enfermedad respiratoria como la gripe (influenza) con diversos síntomas (tos, fiebre, etc.) que,
en casos graves, puede producir una neumonía. Para protegerse puede lavarse las
manos regularmente y evitar tocarse la cara.''')
    print('')
    input('Siguiente -->')
    system('cls')
    print('\033[1:30m ')
    print('Como se Propaga?')
    print('\033[0:0m ')
    print('''El nuevo coronavirus se propaga principalmente por contacto directo (1 metro o 3 pies)
con una persona infectada cuando tose o estornuda, o por contacto con sus gotículas
respiratorias (saliva o secreciones nasales).''')
    print('')
    input('Siguiente -->')
    system('cls')
    print('\033[1:30m ')
    print('Sintomas:')
    print('\033[0:0m ')
    print('''La COVID-19 se caracteriza por síntomas leves, como, secreciones nasales, dolor de garganta,
tos y fiebre. La enfermedad puede ser más grave en algunas personas y provocar neumonía
o dificultades respiratorias.

Más raramente puede ser mortal. Las personas de edad avanzada y las personas con otras afecciones
médicas (como asma, diabetes o cardiopatías) pueden ser más vulnerables y enfermar de gravedad.''')
    print('')
    input('Siguiente -->')
    system('cls')
    print('\033[1:30m ')
    print('Prevencion                                     ACTUALMENTE NO HAY CURA PARA LA COVID-19')
    print('\033[0:0m ')
    print('''Puede reducir el riesgo de infección:
            
~ Lavándose las manos regularmente con agua y jabón o con desinfectante
de manos a base de alcohol
~ Cubriéndose la nariz y la boca al toser y estornudar con un pañuelo
de papel desechable o con la parte interna del codo
~ Evitando el contacto directo (1 metro o 3 pies) con cualquier persona
con síntomas de resfriado o gripe (influenza)''')
    print('')
    input('Fin -->')
    Principal()

def Diagnosticar(respuesta):     # En esta parte se hace el diagnostico del Paciente ya ingresado
    if respuesta.upper() == 'SI':
        return True
    elif respuesta.upper() == 'NO':
        return False
    else:
        print('Escriba una Respuesta Valida')
        input()
        ModStatus(pacientes)


def agregar():     # Se agrega un Nuevo Paciente
    while True:
        system('cls')
        print('\033[1:36m ')
        print('|//////////////////////////|')
        print('|     AGREGAR PACIENTE     |')
        print('|//////////////////////////|')
        print('\033[0:0m ')
        genero = input('''Escriba su Genero:
        
        1) Hombre
        2) Mujer
        3) Volver''')
        if genero != "1" or genero != "2":
            while genero != "1" and genero != "2":
                if genero == "3":
                    Principal()
                genero = input('Opcion Incorrecta')
            system('cls')
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            fecha = input('Fecha de nacimiento: ')
            pais = input('Pais de procedencia: ')
            while True:
                try:
                    edad = int(input('Edad: '))
                    if edad > 0:
                        break
                    else:
                        print('Ingrese una edad valida')
                        print('')
                except:
                    print('Ingresaste una letra/caracter!')
            NuevoPaciente = paciente(nombre, apellido, fecha, pais, genero, edad)
            return NuevoPaciente


def Principal():
    opc = None
    while opc != '0':
        system('cls')
        print('\033[1:35m ')
        print('|///////////////////|')
        print('|      COVID-19     |')
        print('|///////////////////|')
        print('\033[0:0m ')
        print('''1) Acerca de Coronavirus
2) Agregar un Paciente
3) Mostrar Todos los Pacientes
4) Opcion Modificar
0) Salir''')
        opc = input('Opcion: ')
        if opc == '1':
            AcercaDe()
        elif opc == '2':
            Paciente = agregar()
            ListaP.append(Paciente)
            system('cls')
        elif opc == '3':
            system('cls')
            try:
                for persona in ListaP:
                    print(persona.mostrar())
                    input('Siguiente -->')
            except:
                print('Nada que Mostrar aqui')
                input()
        elif opc == '4':
            system('cls')
            ModStatus(ListaP)
        elif opc == '0':
            print('\033[1:30m ')
            print('''Hasta luego!
RECUERDE LAVARSE LAS MANOS!
NO SALIR DE CASA SOLO LUGARES DE ABASTESENCIA, USE MASCARILLA.
#quedateencasa''')
            break
        else:
            print('Opcion invalida.')


Principal()
