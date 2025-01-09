import flet as ft
from services.crud_operations import read_data
from utils.style import button_style, estilo_encabezado, estilo_celda, estilo_tabla

class LeerViews:
    def __init__(self, page):
        '''Constructor de la clase'''

        self.page = page
        self.collection_name = ""  # Nombre de la colección seleccionada

    def build(self):
        '''Método que construye la página Leer'''

        self.page.title = "Leer"
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.page.window_width = 1000  # Aumentamos el tamaño de la ventana
        self.page.window_height = 700  # Aumentamos la altura de la ventana

        self.page.update()

        botones_fields = ft.Column(visible=True)
        tabla_fields = ft.Column(visible=False)

        def mostrar_campos(tipo):
            '''Método para mostrar los datos dinámicamente según la colección seleccionada'''
            self.collection_name = tipo

            # Ocultar botones y mostrar tabla
            botones_fields.visible = False
            tabla_fields.visible = True

            try:
                # Obtener datos de la colección utilizando crud_operations
                datos = read_data(self.collection_name)

                # Si hay datos, filtramos el campo '_id' de las columnas y filas
                if datos:
                    
                    # Obtener las columnas sin incluir '_id'
                    columnas = []
                    for col in datos[0].keys():
                        if col != "_id":
                            columnas.append(col)

                    # Obtener las filas sin incluir '_id'
                    filas = []
                    for row in datos:
                        fila_filtrada = {}
                        for key, value in row.items():
                            if key != "_id":
                                fila_filtrada[key] = value
                        filas.append(fila_filtrada)

                    # Crear tabla con los datos filtrados utilizando los estilos proporcionados
                    tabla = estilo_tabla(
                        columns=[estilo_encabezado(col) for col in columnas],
                        rows=[ft.DataRow(cells=[estilo_celda(str(fila[col])) for col in columnas]) for fila in filas]
                    )

                    # Aplicar el estilo de la tabla
                    tabla_fields.controls = [
                        ft.Column(
                            controls=[tabla],
                            scroll=ft.ScrollMode.AUTO,  # Desplazamiento automático si es necesario
                            height=500,  # Ajustamos la altura de la tabla
                            width=950,  # Ancho de la tabla
                        ),
                        ft.ElevatedButton(
                            text="Volver",
                            style=button_style,
                            width=300,
                            height=50,
                            on_click=volver_a_menu_principal  # Conectar botón "Volver"
                        )
                    ]

                else:
                    tabla_fields.controls = [
                        ft.Text("No hay datos disponibles.", color=ft.colors.RED),
                        ft.ElevatedButton(
                            text="Volver",
                            style=button_style,
                            width=300,
                            height=50,
                            on_click=volver_a_menu_principal
                        )
                    ]
            
            except Exception as e:
                tabla_fields.controls = [
                    ft.Text(f"Error al cargar los datos: {str(e)}", color=ft.colors.RED),
                    ft.ElevatedButton(
                        text="Volver",
                        style=button_style,
                        width=300,
                        height=50,
                        on_click=volver_a_menu_principal
                    )
                ]

            self.page.update()

        def volver_a_menu_principal(e):
            '''Método para volver al menú principal'''
            botones_fields.visible = True
            tabla_fields.visible = False
            self.page.update()

        def ir_a_main(e):
            from views import MainView
            # Limpiar la página actual
            self.page.clean()

            # Crear una instancia de MainView y construirla
            main_view = MainView(self.page)
            main_view.build()

        botones_fields.controls = [
            ft.ElevatedButton(
                text="Paciente",
                style=button_style,
                width=300,
                height=50,
                on_click=lambda e: mostrar_campos("pacientes"),
            ),
            ft.ElevatedButton(
                text="Médico",
                style=button_style,
                width=300,
                height=50,
                on_click=lambda e: mostrar_campos("medicos"),
            ),
            ft.ElevatedButton(
                text="Cita",
                style=button_style,
                width=300,
                height=50,
                on_click=lambda e: mostrar_campos("citas"),
            ),
            ft.ElevatedButton(
                text="Volver",
                style=button_style,
                width=300,
                height=50,
                on_click=lambda e: ir_a_main("Volver"),
            )
        ]

        # Agregar los botones y la tabla dinámica a la página
        self.page.add(
            ft.Container(
                content=ft.Column(
                    controls=[botones_fields, tabla_fields],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=20,
            )
        )
