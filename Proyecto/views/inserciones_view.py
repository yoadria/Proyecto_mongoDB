import flet as ft
from models.db_models import Medico, Paciente, Cita
from utils.style import button_style  # Importar los estilos


class InsercionesView:
    def __init__(self, page):
        self.page = page
        self.collection = ""  # Guardará el tipo de datos a insertar
        self.fields = ft.Column(visible=False)  # Contenedor de campos dinámicos

    def build(self):
        
        self.page.title = "Inserciones"
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Botones principales para elegir tipo de inserción
        botones = ft.Column(
            controls=[
                ft.ElevatedButton(
                    text="Paciente",
                    style=button_style,
                    width=300,
                    height=50,
                    on_click=lambda e: self.mostrar_campos(Paciente),
                ),
                ft.ElevatedButton(
                    text="Médico",
                    style=button_style,
                    width=300,
                    height=50,
                    on_click=lambda e: self.mostrar_campos(Medico),
                ),
                ft.ElevatedButton(
                    text="Cita",
                    style=button_style,
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
        botones_inferiores = ft.Column(
            controls=[
                ft.ElevatedButton(
                    text="Registrar",
                    style=button_style,
                    width=200,
                    height=50,
                    on_click=self.save_data,
                ),
                ft.ElevatedButton(
                    text="Volver",
                    style=button_style,
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
        from utils.labels import LABELS_MAP

        """Genera campos dinámicos en función de los atributos del modelo."""
        self.collection = modelo.__name__.lower() + "s"

        # Crea campos utilizando los valores del modelo
        atributos = modelo.__init__.__code__.co_varnames[1:]  # Obtiene los nombres de los parámetros del constructor

        # campos = [
        #     ft.TextField(label=atributo.capitalize(), width=300, color=ft.colors.BLACK)  # Establece color del texto a negro
        #     for atributo in atributos
        # ]

        campos = [
            ft.TextField(
                label=LABELS_MAP.get(atributo, atributo.capitalize()),  # Usa el mapeo de etiquetas o capitaliza por defecto
                width=300,
                color=ft.colors.BLACK  # Establece el color del texto a negro
            )
            for atributo in atributos
            if LABELS_MAP.get(atributo, True) is not False  # Solo muestra campos que hallamos definido en LABELS_MAP
        ]


        # Asigna los campos a la lista de controles
        self.fields.controls = campos
        self.fields.visible = True
        self.page.update()

    def save_data(self, e):

        from services import insert_data
        from views import AlertView

        # Extraer datos del contenedor de forma dinámica
        # Usamos las claves y valores de los controles tipo TextField
        datos = {}
        for control in self.fields.controls:
            if isinstance(control, ft.TextField):
                key = control.label.lower()
                value = control.value
                datos[key] = value

        if 'dni' in datos:
            datos['DNI'] = datos.pop('dni')
        

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
            print("entro por aki")
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
