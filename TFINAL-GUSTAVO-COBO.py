from guizero import App, Box, PushButton, Text, TextBox, ListBox, Combo, RadioButton

encuestas = []
respuA = 0
respuB = 0
respuC = 0
cuentapreg = 0

def actionalu():
    if comboalu2.value == "":
        noenc = Text(abmencuestas,text="No hay encuestas Disponible", size = 20)
        noenc.value
    else:

        comboalu2.visible = True
        nomyapelabel.visible = True
        nomyapealumno.visible = True
        salir_button.visible =True
    
def combo_enc():

    textopreg1.visible = True
    textopreg1.value = combopreg.value.split(" - ")[0] 
    opcionA.visible = True
    opcionB.visible = True
    opcionC.visible = True
    textopreg2.visible = False
    textopreg2.value = combopreg.value.split(" - ")[1] 
    textopreg3.visible = False
    textopreg3.value = combopreg.value.split(" - ")[2] 
    textopreg4.visible = False
    textopreg4.value = combopreg.value.split(" - ")[3] 
    
def actioncont():
    global password
    password = input_passprofe.value 
    if password == "1234":  
        actionprofe()
        passprofelabel.visible = False
        input_passprofe.visible = False
        button3.visible= False
        
    else:
        message4.visible = True
        input_passprofe.value = ""
    
def actionprofe():
    
    comboalu2.visible = False
    resA.visible = False
    resB.visible = False
    resC.visible = False
    cantrespA.visible = False
    cantrespB.visible = False
    cantrespC.visible = False

    button1.visible = False
    button2.visible = False
    button3.visible =True
    passprofelabel.visible = True
    input_passprofe.visible = True
    input_passprofe.value
    
    if password == "1234":
        message4.visible = False
        message2.visible = False
        alumnos.visible = False
        encuesta_label.visible = True
        nombre_encuesta_input.visible = True
        pregunta1_label.visible = True
        pregunta1_input.visible = True
        pregunta2_label.visible = True
        pregunta2_input.visible = True
        pregunta3_label.visible = True
        pregunta3_input.visible = True
        pregunta4_label.visible = True
        pregunta4_input.visible = True
        crear_button.visible = True
        eliminar_button.visible = True
        finalizar_button.visible = True
        salir_button.visible = True
        crear_button.align="right"
        eliminar_button.align="right"
        finalizar_button.align="right"
        salir_button.align="right"
        lista_encuestas.visible = True
        lista_encuestas.align ="left"
        button1.visible = False
        button2.visible = False
        input_passprofe.value = ""
    else:
        message4.visible = True
        input_passprofe.value = ""

def Opcion_A():
    global respuA 
    respuA = respuA + 1
    cantrespA.visible = False
    cantrespA.value = respuA
    cuenta()
    
def Opcion_B():
    global respuB 
    respuB = respuB + 1
    cantrespB.visible = False
    cantrespB.value = respuB
    cuenta()

def Opcion_C():
    global respuC
    respuC = respuC + 1
    cantrespC.visible = False
    cantrespC.value = respuC
    cuenta()

def cuenta():
    global cuentapreg
    cuentapreg=cuentapreg+1
    if cuentapreg==1:
        textopreg1.visible = False
        textopreg2.visible = True
    elif cuentapreg==2:
        textopreg2.visible = False
        textopreg3.visible = True
    elif cuentapreg==3:
        textopreg3.visible = False
        textopreg4.visible = True
    elif cuentapreg==4:
        resalu = Text(abmencuestas,text= "El Alumno: "+nomyapealumno.value,size=20)
        resalu.value
        nomyapelabel.visible = False
        nomyapealumno.visible = False
        textopreg4.visible = False
        resA.visible = True
        cantrespA.visible = True
        resB.visible = True
        cantrespB.visible = True
        resC.visible = True
        cantrespC.visible = True
        opcionA.visible = False
        opcionB.visible = False
        opcionC.visible = False

def crear_encuesta():
    nombre = nombre_encuesta_input.value
    pregunta1 = pregunta1_input.value
    pregunta2 = pregunta2_input.value
    pregunta3 = pregunta3_input.value
    pregunta4 = pregunta4_input.value
    encuesta = {"Encuesta": nombre, "Pregunta1": pregunta1, "Pregunta2": pregunta2, 
                "Pregunta3": pregunta3,"Pregunta4": pregunta4 }
    encuestas.append(encuesta)
    actualizar_lista_encuestas()
    nombre_encuesta_input.clear()
    pregunta1_input.clear()
    pregunta2_input.clear()
    pregunta3_input.clear()
    pregunta4_input.clear()
    mensaje.visible = True
    mensaje.value = f"Encuesta: {nombre} creada correctamente."

# Actualizamos la Lista de encuestas
def actualizar_lista_encuestas():
    lista_encuestas.clear()
    comboalu2.clear()
    
    for idx, encuesta in enumerate(encuestas, start=1):
     lista_encuestas.append(f"ID: {idx},Encuesta: {encuesta['Encuesta']}),Pregunta1: {encuesta['Pregunta1']},Pregunta2: {encuesta['Pregunta2']}, Pregunta3: {encuesta['Pregunta3']}, Pregunta4: {encuesta['Pregunta4']}")
     comboalu2.append(f"Encuesta: {encuesta['Encuesta']}")
     combopreg.append(f"Pregunta1: {encuesta['Pregunta1']} - Pregunta2: {encuesta['Pregunta2']} - Pregunta3: {encuesta['Pregunta3']} - Pregunta4: {encuesta['Pregunta4']}")
    

# Eliminamos la Encuesta
def eliminar_encuesta():
    selected = lista_encuestas.value
    if selected:
        parts = selected.split(",Encuesta")
        i = int(parts[0].split(": ")[1])-1
        encuesta_eliminada = encuestas.pop(i)
        actualizar_lista_encuestas()
        mensaje.value = f"Encuesta: {encuesta_eliminada['Encuesta']} eliminada correctamente."

def finalizar_carga():
    encuesta_label.visible = False
    nombre_encuesta_input.visible = False
    pregunta1_label.visible = False
    pregunta1_input.visible = False
    pregunta2_label.visible = False
    pregunta2_input.visible = False
    pregunta3_label.visible = False
    pregunta3_input.visible = False
    pregunta4_label.visible = False
    pregunta4_input.visible = False
    crear_button.visible = False
    eliminar_button.visible = False
    finalizar_button.visible = False
    lista_encuestas.visible = False
    button1.visible = True
    button2.visible = True
    mensaje.visible = False
    
# Función para mostrar las encuestas en la lista
def salir_encuesta():
    abmencuestas.destroy()

def mostrar_encuestas():
    actualizar_lista_encuestas()

def iniciar():
    #message1 = Text(abmencuestas, text= "Bienvenidos al Sistema de Encuentas Escolares",  size= 20)
    #message2 = Text(abmencuestas, text= "Seleccione la Opción:",  size= 20)
    message1.visible = True
    message2.visible = True
    button1 = PushButton(boton, actionalu, text="Alumno", grid=[0,0] )
    button2 = PushButton(boton,  actionprofe, text="Profesor", grid=[2,0] )
    button1.visible = False
    button2.visible = False



abmencuestas = App(title= "Encuestas Escolares", width= 1000,height= 800, bg=(254,130,10))
message1 = Text(abmencuestas, text= "Bienvenidos al Sistema de Encuentas Escolares",  size= 20)
message2 = Text(abmencuestas, text= "Seleccione la Opción:",  size= 20)
boton = Box(abmencuestas, layout="grid", grid=[1,0])
button1 = PushButton(boton, actionalu, text="Alumno", grid=[0,0] )
button2 = PushButton(boton,  actionprofe, text="Profesor", grid=[2,0] )
passprofelabel = Text(abmencuestas,"Ingrese la contraseña: ")
input_passprofe = TextBox(abmencuestas,"")
input_passprofe.visible= False
passprofelabel.visible= False
message4 = Text(abmencuestas, text= "La Contraseña es incorrecta ingresela nuevamente",  size= 20)
message4.visible = False

nomyapelabel = Text(abmencuestas,"Ingrese su Nombre y Apellido: ")
nomyapealumno = TextBox(abmencuestas,"", width= 60)
nomyapelabel.visible = False
nomyapealumno.visible = False
button3 = PushButton(abmencuestas, command=actioncont, text="Validar", grid=[6,0] )
button3.visible = False
alumnos = Text(abmencuestas, text= "Elija una Encuesta:", visible=False)

comboalu2 = Combo(abmencuestas, options=[], command=combo_enc, visible=False)

cajaresp = Box(abmencuestas, layout="grid")
combopreg = Combo(abmencuestas, options=[], command=combo_enc, visible=False)
textopreg1 = Text(abmencuestas,"")
textopreg2 = Text(abmencuestas,"")
textopreg3 = Text(abmencuestas,"")
textopreg4 = Text(abmencuestas,"")
opcionA = PushButton(cajaresp, text="Opcion A", command=Opcion_A, grid=[0, 15, 1, 1])
opcionB = PushButton(cajaresp, text="Opcion B", command=Opcion_B, grid=[2, 15, 1, 1])
opcionC = PushButton(cajaresp, text="Opcion C", command=Opcion_C, grid=[4, 15, 1, 1])
opcionA.visible = False
opcionB.visible = False
opcionC.visible = False
resA = Text(abmencuestas, text= "La cantidad de respuestas Opcion A es de: ", visible= False)
cantrespA = Text(abmencuestas,0)
resB = Text(abmencuestas, text= "La cantidad de respuestas Opcion B es de: ", visible= False)
cantrespB = Text(abmencuestas,0)
resC = Text(abmencuestas, text= "La cantidad de respuestas Opcion C es de: ", visible= False)
cantrespC = Text(abmencuestas,0)
cantrespA.visible = False
cantrespB.visible = False
cantrespC.visible = False

caja = Box(abmencuestas, layout="grid")
cajaresp = Box(abmencuestas, layout="grid")

# Etiquetas y Cajas
encuesta_label = Text(caja, text="Nombre de la Encuesta:", grid=[0, 0])
nombre_encuesta_input = TextBox(caja, grid=[1, 0], width=80)
pregunta1_label = Text(caja, text="Pregunta1:", grid=[0, 1])
pregunta2_label = Text(caja, text="Pregunta2:", grid=[0, 2])
pregunta3_label = Text(caja, text="Pregunta3:", grid=[0, 3])
pregunta4_label = Text(caja, text="Pregunta4:", grid=[0, 4])
pregunta1_input = TextBox(caja, grid=[1, 1], width=80)
pregunta2_input = TextBox(caja, grid=[1, 2], width=80)
pregunta3_input = TextBox(caja, grid=[1, 3], width=80)
pregunta4_input = TextBox(caja, grid=[1, 4], width=80)
encuesta_label.visible = False
nombre_encuesta_input.visible = False
pregunta1_label.visible = False
pregunta1_input.visible = False
pregunta2_label.visible = False
pregunta2_input.visible = False
pregunta3_label.visible = False
pregunta3_input.visible = False
pregunta4_label.visible = False
pregunta4_input.visible = False

# Botones

crear_button = PushButton(caja, text="Cargar Encuesta", command=crear_encuesta, grid=[0, 5, 2, 1])
eliminar_button = PushButton(caja, text="Eliminar Encuesta", command=eliminar_encuesta, grid=[2, 5, 2, 1])
finalizar_button = PushButton(caja, text="Finalizar Carga", command=finalizar_carga, grid=[4, 5, 2, 1])
salir_button = PushButton(caja, text="Salir", command=salir_encuesta, grid=[6, 5, 2, 1])
crear_button.visible = False
eliminar_button.visible = False
finalizar_button.visible = False
salir_button.visible = False
lista_encuestas = ListBox(caja, items=[], grid=[0, 5, 2, 3], width=500, height=80)
lista_encuestas.visible = False

# Mensajes
mensaje = Text(caja, text="", grid=[0, 10, 2, 1])
mensaje.visible = False

actualizar_lista_encuestas()

# Ejecutamos la app de Encuestas
abmencuestas.display()
