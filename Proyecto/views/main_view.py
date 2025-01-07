import flet as ft

'''
Fichero que contiene la clase de la página principal
'''

class MainView:
    def __init__(self, page):
        self.page = page

    def build(self):
        '''Método que construye la página principal'''

        self.page.title = "Página Principal"

        # Centrar los elementos de la página
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        # Tamaño de la ventana
        self.page.window_width = 400
        self.page.window_height = 550

        # Evitar que se pueda redimensionar la ventana
        self.page.window_resizable = False
        self.page.window_full_screen = False

        self.page.bgcolor = ft.colors.WHITE

        # Estilo de los botones (color, bordes redondeados y tamaño)
        button_style = ft.ButtonStyle(
            bgcolor="#FFA07A",
            color="black",
            overlay_color="#D35400",  # Color al hacer clic
            shape=ft.RoundedRectangleBorder(radius=10)  # Bordes redondeados
        )

        # Botones principales (Aplicación de estilo general)
        botones = ft.Container(
            content=ft.Column(
                controls=[
                    ft.ElevatedButton(
                        text="Leer Datos",
                        width=300,
                        height=50,
                        style=button_style,
                        on_click=self.ir_a_leer,
                    ),
                    ft.ElevatedButton(
                        text="Insertar Datos",
                        width=300,
                        height=50,
                        style=button_style,
                        on_click=self.ir_a_insersiones,
                    ),
                    ft.ElevatedButton(
                        text="Actualizar Datos",
                        width=300,
                        height=50,
                        style=button_style,
                        on_click=self.ir_a_modificaciones,
                    ),
                    ft.ElevatedButton(
                        text="Eliminar Datos",
                        width=300,
                        height=50,
                        style=button_style,
                    ),
                    ft.ElevatedButton(
                        text="Generar Datos",
                        width=300,
                        height=50,
                        style=button_style,
                    ),
                    ft.ElevatedButton(
                        text="Salir",
                        width=300,
                        height=50,
                        style=button_style,
                        on_click=self.cerrar,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15,  # Espacio entre los botones
            ),
            padding=10,
        )

        # Agregar los botones y título a la parte superior de la página
        self.page.add(
            ft.Container(
                content=ft.Text(
                    "Menú Principal",
                    size=28,
                    weight="bold",
                    color="Black"
                ),
                alignment=ft.alignment.center,
                margin=ft.Margin(0, 20, 0, 20)  # Margen superior e inferior
            )
        )

        self.page.add(botones)
        self.page.update()

    def cerrar(self, e):
        '''Función que se llama al presionar el botón "Salir" y cierra la ventana.'''
        self.page.window_close()

    def ir_a_insersiones(self, e):
        '''Función que se llama al presionar el botón "Insertar Datos" y abre la página "InsercionesView".'''
        from views import InsercionesView
        self.page.clean()  # Limpiar la página actual
        insersiones_view = InsercionesView(self.page)
        insersiones_view.build()

    def ir_a_leer(self, e):
        '''Función que se llama al presionar el botón "Leer Datos" y abre la página "LeerViews".'''
        from views import LeerViews
        self.page.clean()  # Limpiar la página actual
        submenu_view = LeerViews(self.page)
        submenu_view.build()

    def ir_a_modificaciones(self, e):
    
        from views import ModificarViews
        self.page.clean()  # Limpiar la página actual
        modificar_view = ModificarViews(self.page)
        modificar_view.build()
