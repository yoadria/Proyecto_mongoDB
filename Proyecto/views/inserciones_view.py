import flet as ft

'''
Fichero que contiene la interfaz para insertar los datos
'''

class InsercionesView:
    def __init__(self, page):
        '''Constructor de la clase'''

        self.page = page
        self.collection = ""  # esta variable guardara en que coleccion se guardaran los datos depende de los campos desplegados

        # estos son los campos dinamico de medico, solo he trabajado con esto para la prueba 
        # hay que mirar si lo hacemos asi o de la manera ya estructurada
        self.medico_name = ft.TextField(label="Nombre del Médico", width=300)
        self.medico_especialidad = ft.TextField(label="Especialidad", width=300)
        self.medico_tf = ft.TextField(label="Teléfono", width=300)
        self.medico_email = ft.TextField(label="E-mail del médico", width=300)

    def build(self):
        '''Metodo que construlle la pagina Insersiones'''

        
        self.page.title = "Insersiones"
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window_width = 700
        self.page.window_height = 900

        self.page.window_resizable = False
        self.page.window_full_screen = False

        # Contenedores dinámicos para mostrar/ocultar los campos
        paciente_fields = ft.Column(visible=False)
        medico_fields = ft.Column(visible=False)
        cita_fields = ft.Column(visible=False)

        
        def mostrar_campos(tipo):
            '''Metodo para mostrar campos dinámicamente según el botón presionado'''
            self.collection = tipo

            paciente_fields.visible = tipo == "Paciente"
            medico_fields.visible = tipo == "Médico"
            cita_fields.visible = tipo == "Cita"
            self.page.update()

            
        # Contenido de los campos dinámicos
        paciente_fields.controls = [
            ft.TextField(label="Nombre del Paciente", width=300),
            ft.TextField(label="Edad del Paciente", width=300),
            ft.TextField(label="Dirección del Paciente", width=300),
            ft.TextField(label="Teléfono del Paciente", width=300),
            ft.TextField(label="E-mail del Paciente", width=300)
        ]

        medico_fields.controls = [
            # estos atributos ya estan definidos arriba, otra forma de hacerlo 
            self.medico_name,
            self.medico_especialidad, 
            self.medico_tf,
            self.medico_email 
        ]

        cita_fields.controls = [
            ft.TextField(label="Paciente de la cita", width=300),
            ft.TextField(label="Médico de la Cita", width=300),
            ft.TextField(label="Fecha de la Cita", width=300),
            ft.TextField(label="Motivo de la Cita", width=300)
        ]


        # Crear los botones principales
        botones = ft.Column(
            controls=[
                ft.ElevatedButton(
                    text="Paciente",
                    width=300,
                    height=50,
                    on_click=lambda e: mostrar_campos("Paciente"),
                ),
                ft.ElevatedButton(
                    text="Médico",
                    width=300,
                    height=50,
                    on_click=lambda e: mostrar_campos("Médico"),
                ),
                ft.ElevatedButton(
                    text="Cita",
                    width=300,
                    height=50,
                    on_click=lambda e: mostrar_campos("Cita"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )

        # Agregar los botones y los contenedores dinámicos a la página
        self.page.add(
            ft.Container(
                content=ft.Column(
                    controls=[botones, paciente_fields, medico_fields, cita_fields],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=20,
            )
        )

        botones_inferiores = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text="Registrar",
                    width=200,
                    height=50,
                    on_click=self.save_data, # Funcion para guardar los datos del medico
                ),
                ft.ElevatedButton(
                    text="Borrar",
                    width=200,
                    height=50,
                ),
                ft.ElevatedButton(
                    text="Volver",
                    width=200,
                    height=50,
                    on_click=self.ir_a_main, # Funcion para volver a pagina principal
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )
        self.page.add(botones_inferiores)


        self.page.update()
    
    def ir_a_main(self, e):
        from views import MainView
        # Limpiar la página actual
        self.page.clean()

        # Crear una instancia de MainView y construirla
        main_view = MainView(self.page)
        main_view.build()

    def save_data(self, e):

        '''Metodo que llama a la funcion insert de crud_operations.py'''

        from services import insert
        from views import AlertView  # esta instancia llama a la clase AlertView para las notificaciones
        if self.collection == "Médico":
            medico = {
                "nombre": self.medico_name.value, # valor del campo nombre
                "especialidad": self.medico_especialidad.value, # valor del campo especialidad
                "telefono": self.medico_tf.value, # valor del campo telefono
                "email": self.medico_email.value, # valor del campo email
            }

            try:
                # Validar que los campos no estén vacíos
                if not medico["nombre"] or not medico["especialidad"] or not medico["telefono"] or not medico["email"]:
                    # mostrar mensage de campos vacios
                    alerta = AlertView(
                        titulo="Advertencia",
                        mensaje="No pueden haber campos vacíos.",
                        page=self.page
                    )
                    alerta.open_dialog()
                    self.reset()
                    return

                insert("medicos", medico)
                # Mostrar mensaje de éxito
                alerta = AlertView(
                    titulo="Éxito",
                    mensaje="Datos registrados correctamente.",
                    page=self.page
                )
                alerta.open_dialog()
                self.reset() # Limpiar los campos al volver a la página principal  
                return

            except ValueError:
                # Mostrar mensaje de error
                alerta = AlertView(
                    titulo="Error",
                    mensaje="Ha ocurrido un error inesperado lo sentimos.",
                    page=self.page
                )
                alerta.open_dialog()
                self.reset()
                return
            



    def reset(self):

        self.page.clean()
        self.collection = ""
        self.medico_name = ft.TextField(label="Nombre del Médico", width=300)
        self.medico_especialidad = ft.TextField(label="Especialidad", width=300)
        self.medico_tf = ft.TextField(label="Teléfono", width=300)
        self.medico_email = ft.TextField(label="E-mail del médico", width=300)
        self.build()

     

