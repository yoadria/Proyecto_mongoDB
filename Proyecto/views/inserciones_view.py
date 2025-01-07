import flet as ft
from models.db_models import Medico, Paciente, Cita

class InsercionesView:
    def __init__(self, page):
        self.page = page
        self.collection = ""  # Guardará el tipo de datos a insertar
        self.fields = ft.Column(visible=False)  # Contenedor de campos dinámicos

    def build(self):
        
        self.page.title = "Inserciones"
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window_width = 700
        self.page.window_height = 900
        self.page.window_resizable = False
        self.page.window_full_screen = False

        # Botones principales para elegir tipo de inserción
        botones = ft.Column(
            controls=[
                ft.ElevatedButton(
                    text="Paciente",
                    width=300,
                    height=50,
                    on_click=lambda e: self.mostrar_campos(Paciente),
                ),
                ft.ElevatedButton(
                    text="Médico",
                    width=300,
                    height=50,
                    on_click=lambda e: self.mostrar_campos(Medico),
                ),
                ft.ElevatedButton(
                    text="Cita",
                    width=300,
                    height=50,
                    on_click=lambda e: self.mostrar_campos(Cita),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )

        # Agregar botones y contenedor dinámico a la página
        self.page.add(
            ft.Container(
                content=ft.Column(
                    controls=[botones, self.fields],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=20,
            )
        )

        # Botones inferiores
        botones_inferiores = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text="Registrar",
                    width=200,
                    height=50,
                    on_click=self.save_data,
                ),
                ft.ElevatedButton(
                    text="Volver",
                    width=200,
                    height=50,
                    on_click=self.ir_a_main,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        )
        self.page.add(botones_inferiores)
        self.page.update()

    def mostrar_campos(self, modelo):

        """Genera campos dinámicos en función de los atributos del modelo."""
        self.collection = modelo.__name__.lower() + "s"

        #Crea campos utilizando los valores del modelo

        #Obtiene los nombres de los parámetros del constructor
        atributos = modelo.__init__.__code__.co_varnames[1:] #Basicamente obtiene el nombre de las variables para luego establecer el valor de los campos

        campos = [
            ft.TextField(label=atributo.capitalize(), width=300)
            for atributo in atributos
        ]

        #Asigna los campos a la lista de controles
        self.fields.controls = campos
        self.fields.visible = True
        self.page.update()

    def save_data(self, e):

        from services import insert_data
        from views import AlertView

        # Extraer datos del contenedor dinámico
        datos = {
            control.label.lower(): control.value
            for control in self.fields.controls
            if isinstance(control, ft.TextField)
        }

        # Validar campos vacíos
        if any(not value for value in datos.values()):
            alerta = AlertView(
                titulo="Advertencia",
                mensaje="No pueden haber campos vacíos.",
                page=self.page,
            )
            alerta.open_dialog()
            return

        # Intentar insertar en la base de datos
        try:
            insert_data(self.collection, datos)
            alerta = AlertView(
                titulo="Éxito",
                mensaje="Datos registrados correctamente.",
                page=self.page,
            )
            alerta.open_dialog()
            self.fields.controls.clear()
            self.fields.visible = False
            self.page.update()

        except Exception as ex:
            alerta = AlertView(
                titulo="Error",
                mensaje=f"Ha ocurrido un error inesperado: {ex}",
                page=self.page,
            )
            alerta.open_dialog()

    def ir_a_main(self, e):
        from views import MainView

        self.page.clean()
        main_view = MainView(self.page)
        main_view.build()
