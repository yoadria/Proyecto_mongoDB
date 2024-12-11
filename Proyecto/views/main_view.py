import flet as ft
'''
fichero que contiene la clase de la pagina principal
'''

class MainView:
    def __init__(self, page):
        self.page = page

    def build(self):
        '''Metodo que construlle la pagina principal'''

        self.page.title = "Pagina principal"

        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    
        #tamaño en px
        self.page.window_width = 400
        self.page.window_height = 500

        #para que no se pueda redimensionar
        self.page.window_resizable = False
        self.page.window_full_screen = False

    #crea un contenedor con los botones alineados en el centro de la pagina
        botones = ft.Container(
            content=ft.Column(
                controls=[
                    ft.ElevatedButton(text="Leer Datos", width=300, height=50, on_click=self.ir_a_leer),
                    ft.ElevatedButton(text="Insertar Datos", width=300, height=50, on_click=self.ir_a_insersiones),
                    ft.ElevatedButton(text="Actualizar Datos", width=300, height=50),
                    ft.ElevatedButton(text="Eliminar Datos", width=300, height=50),
                    ft.ElevatedButton(text="Generar Datos", width=300, height=50),
                    ft.ElevatedButton(text="Salir", width=300, height=50)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15,  #espacio entre los botones
            ),
            padding=10,
        )

    

        # Agregar los botones a la parte inferior de la página
        self.page.add(ft.Container(height=20))  # Espacio vacío arriba
        self.page.add(botones)  # Botones en la parte inferior
        self.page.update()

    def ir_a_insersiones(self, e):
        '''Función que se llama al presionar el botón "Insertar Datos"
        y abre la pagina "InsersionesVew"
        '''

        from views import InsercionesView
        # Limpiar la página actual
        self.page.clean()

        # Crear una instancia de InsersionesView y construirla
        insersiones_view = InsercionesView(self.page)
        insersiones_view.build()

    def ir_a_leer(self, e):
        '''Función que se llama al presionar el botón "Leer Datos"
        y abre la pagina "LeerView"
        '''

        from views import LeerViews
        # Limpiar la página actual
        self.page.clean()

        # Crear una instancia de LeerView y construirla
        leer_view = LeerViews(self.page)
        leer_view.build()
