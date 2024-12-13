import flet as ft

'''
Fichero que contiene la interfaz para insertar los datos
'''

class InsercionesView:
    def __init__(self, page):
        '''Constructor de la clase'''

        self.page = page
        self.collection = ""  # esta variable guardará en qué colección se guardarán los datos

        # Define los campos de médico como atributos de la clase
        self.medico_name = ft.TextField(label="Nombre del Médico", width=300)
        self.medico_especialidad = ft.TextField(label="Especialidad", width=300)
        self.medico_tf = ft.TextField(label="Teléfono", width=300)
        self.medico_email = ft.TextField(label="E-mail del médico", width=300)

        # Contenedores para campos dinámicos
        self.paciente_fields = ft.Column(visible=False)
        self.medico_fields = ft.Column(visible=False)
        self.cita_fields = ft.Column(visible=False)

    def build(self):
        '''Método que construye la página de Inserciones'''

        self.page.title = "Inserciones"
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window_width = 700
        self.page.window_height = 900

        self.page.window_resizable = False
        self.page.window_full_screen = False

        # Define los campos dentro de los contenedores
        self.paciente_fields.controls = [
            ft.TextField(label="Nombre del Paciente", width=300),
            ft.TextField(label="Edad del Paciente", width=300),
            ft.TextField(label="Dirección del Paciente", width=300),
            ft.TextField(label="Teléfono del Paciente", width=300),
            ft.TextField(label="E-mail del Paciente", width=300)
        ]

        self.medico_fields.controls = [
            self.medico_name,
            self.medico_especialidad, 
            self.medico_tf,
            self.medico_email 
        ]

        self.cita_fields.controls = [
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
                    on_click=lambda e: self.mostrar_campos("Paciente"),
                ),
                ft.ElevatedButton(
                    text="Médico",
                    width=300,
                    height=50,
                    on_click=lambda e: self.mostrar_campos("Medico"),
                ),
                ft.ElevatedButton(
                    text="Cita",
                    width=300,
                    height=50,
                    on_click=lambda e: self.mostrar_campos("Cita"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )

        # Agregar los botones y los contenedores dinámicos a la página
        self.page.add(
            ft.Container(
                content=ft.Column(
                    controls=[botones, self.paciente_fields, self.medico_fields, self.cita_fields],
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
                    on_click=self.save_data,  # Función para guardar los datos del médico
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
                    on_click=self.ir_a_main,  # Función para volver a página principal
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )
        self.page.add(botones_inferiores)

        self.page.update()

    def mostrar_campos(self, tipo):
        '''Método para mostrar campos dinámicamente según el botón presionado'''
        self.collection = tipo

        self.paciente_fields.visible = tipo == "Paciente"
        self.medico_fields.visible = tipo == "Medico"
        self.cita_fields.visible = tipo == "Cita"
        self.page.update()

    def ir_a_main(self, e):
        from views import MainView
        # Limpiar la página actual
        self.page.clean()

        # Crear una instancia de MainView y construirla
        main_view = MainView(self.page)
        main_view.build()

    def save_data(self, e):
        
        '''Método para guardar los datos según la colección seleccionada'''

        from services import insert
        from views import AlertView  # Para mostrar notificaciones

        # Mapeo de colecciones con sus campos correspondientes
        mapeado_colecciones = {
            "Paciente": self.paciente_fields,  # Acceder directamente a las variables
            "Medico": self.medico_fields,
            "Cita": self.cita_fields,
        }

        # Obtener los campos del contenedor activo
        contenedor_activo = mapeado_colecciones.get(self.collection)

        datos = {}
        for control in contenedor_activo.controls:
            if isinstance(control, ft.TextField):
                datos[control.label.lower().replace(" ", "_")] = control.value

        # Validar si hay campos vacíos
        if any(not value for value in datos.values()):
            alerta = AlertView(
                titulo="Advertencia",
                mensaje="No pueden haber campos vacíos.",
                page=self.page
            )
            alerta.open_dialog()
            return

        # Intentar la inserción en la base de datos
        try:
            insert(self.collection.lower() + "s", datos)  # Inserta en la colección correspondiente
            alerta = AlertView(
                titulo="Éxito",
                mensaje="Datos registrados correctamente.",
                page=self.page
            )
            alerta.open_dialog()
            self.reset()  # Limpia los campos después de registrar

        except Exception as ex:
            alerta = AlertView(
                titulo="Error",
                mensaje=f"Ha ocurrido un error inesperado: {ex}",
                page=self.page
            )
            alerta.open_dialog()

    def reset(self):
        '''Resetea los campos y vuelve a construir la página'''
        self.page.clean()
        self.collection = ""
        self.medico_name = ft.TextField(label="Nombre del Médico", width=300)
        self.medico_especialidad = ft.TextField(label="Especialidad", width=300)
        self.medico_tf = ft.TextField(label="Teléfono", width=300)
        self.medico_email = ft.TextField(label="E-mail del médico", width=300)
        self.build()


     

