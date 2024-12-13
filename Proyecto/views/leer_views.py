import flet as ft

class LeerViews:
    def __init__(self, page):
        '''Constructor de la clase'''

        self.page = page
        self.collection = ""  # Esta variable guardará en qué colección se guardarán los datos

        # Campos del médico
        self.medico_name = ft.TextField(label="Nombre del Médico", width=300)
        self.medico_especialidad = ft.TextField(label="Especialidad", width=300)
        self.medico_tf = ft.TextField(label="Teléfono", width=300)
        self.medico_email = ft.TextField(label="E-mail del médico", width=300)

    def build(self):
        '''Método que construye la página Leer'''

        self.page.title = "Leer"
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window_width = 800
        self.page.window_height = 600

        self.page.update()

        # Campos de cada sección
        paciente_fields = ft.Column(visible=False)
        medico_fields = ft.Column(visible=False)
        cita_fields = ft.Column(visible=False)
        botones_fields = ft.Column(visible=True)

        def mostrar_campos(tipo):
            '''Método para mostrar campos dinámicamente según el botón presionado'''
            self.collection = tipo

            botones_fields.visible = False
            paciente_fields.visible = tipo == "Paciente"
            medico_fields.visible = tipo == "Médico"
            cita_fields.visible = tipo == "Cita"
            self.page.update()

        def volver_a_menu_principal(e):
            '''Método para mostrar de nuevo los botones principales y ocultar los campos'''
            botones_fields.visible = True
            paciente_fields.visible = False
            medico_fields.visible = False
            cita_fields.visible = False
            self.page.update()

        def mostrar_busqueda(e):
            pass

        # Estilo de los botones (color, bordes redondeados y tamaño)
        button_style = ft.ButtonStyle(
            bgcolor="#FFA07A",
            color="black",
            overlay_color="#D35400",  # Color al hacer clic
            shape=ft.RoundedRectangleBorder(radius=10)  # Bordes redondeados
        )

        # Estilo del encabezado de las tablas
        def estilo_encabezado(texto):
            """Crea un DataColumn con estilo de encabezado en negrita."""
            return ft.DataColumn(
                ft.Text(texto, weight="bold", color="black", size=16) # Encabezados en negrita
            )

        # Estilo de las celdas de las tablas
        def estilo_celda(texto):
            """Crea un contenedor con estilo para una celda de la tabla."""
            return ft.DataCell(
                ft.Container(
                    content=ft.Text(texto, color="black"),
                    alignment=ft.alignment.center  # Centra el texto
                    # border=ft.border.all(1, "black"),  # Borde negro
                )
            )


        # Estilo para la tabla
        def estilo_tabla(columns, rows):
            return ft.Container(
                content=ft.DataTable(
                    columns=columns,
                    rows=rows,
                    vertical_lines=ft.BorderSide(3, "black"),  # Líneas verticales negras
                    horizontal_lines=ft.BorderSide(3, "black"),  # Líneas horizontales negras
                    divider_thickness=1,  # Grosor de las líneas divisorias
                    heading_row_color=ft.colors.BLUE_GREY_200,  # Fondo azul para la fila de encabezado
                    # data_row_color={"even": "#E8F6F3", "odd": "#D1F2EB"},  # Colores alternos en filas
                    border=ft.border.all(1, "black"),  # Borde negro alrededor de la tabla
                ),
                border=ft.border.all(2, "black"),
                border_radius=8,  # Aplica el border_radius a toda la tabla
                padding=0  # Para evitar espacio adicional en el contenedor
            )

        # Contenido de la tabla de médicos
        medico_fields.controls = [
            ft.Container(
                content=estilo_tabla(
                    columns=[
                        estilo_encabezado("Nombre"),
                        estilo_encabezado("Especialidad"),
                        estilo_encabezado("Teléfono"),
                        estilo_encabezado("E-mail"),
                    ],
                    rows=[
                        ft.DataRow(cells=[
                            estilo_celda("Juan Pérez"),
                            estilo_celda("Oftalmología"),
                            estilo_celda("666666666"),
                            estilo_celda("juan@ejemplo.com"),
                        ]),
                        ft.DataRow(cells=[
                            estilo_celda("Ana Gómez"),
                            estilo_celda("Pediatría"),
                            estilo_celda("777777777"),
                            estilo_celda("ana@ejemplo.com"),
                        ]),
                        ft.DataRow(cells=[
                            estilo_celda("Carlos López"),
                            estilo_celda("Cardiología"),
                            estilo_celda("888888888"),
                            estilo_celda("carlos@ejemplo.com"),
                        ]),
                    ]
                ),
                alignment=ft.alignment.center,  # Centra la tabla
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ElevatedButton(
                            text="Volver",
                            width=300,
                            height=50,
                            style=button_style,
                            on_click=volver_a_menu_principal
                        ),
                        ft.ElevatedButton(
                            text="Buscar",
                            width=300,
                            height=50,
                            style=button_style,
                            on_click=mostrar_busqueda
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER  # Centra los botones verticalmente
                ),
                alignment=ft.alignment.center  # Centra toda la columna en el contenedor
            )
        ]

        # Contenido de la tabla de pacientes
        paciente_fields.controls = [
            ft.Container(
                content=estilo_tabla(
                    columns=[
                        estilo_encabezado("Nombre"),
                        estilo_encabezado("Especialidad"),
                        estilo_encabezado("Teléfono"),
                        estilo_encabezado("E-mail"),
                    ],
                    rows=[
                        ft.DataRow(cells=[
                            estilo_celda("Juan Pérez"),
                            estilo_celda("Oftalmología"),
                            estilo_celda("666666666"),
                            estilo_celda("juan@ejemplo.com"),
                        ]),
                        ft.DataRow(cells=[
                            estilo_celda("Ana Gómez"),
                            estilo_celda("Pediatría"),
                            estilo_celda("777777777"),
                            estilo_celda("ana@ejemplo.com"),
                        ]),
                        ft.DataRow(cells=[
                            estilo_celda("Carlos López"),
                            estilo_celda("Cardiología"),
                            estilo_celda("888888888"),
                            estilo_celda("carlos@ejemplo.com"),
                        ]),
                    ]
                ),
                alignment=ft.alignment.center,  # Centra la tabla
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ElevatedButton(
                            text="Volver",
                            width=300,
                            height=50,
                            style=button_style,
                            on_click=volver_a_menu_principal
                        ),
                        ft.ElevatedButton(
                            text="Buscar",
                            width=300,
                            height=50,
                            style=button_style,
                            on_click=mostrar_busqueda
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER  # Centra los botones verticalmente
                ),
                alignment=ft.alignment.center  # Centra toda la columna en el contenedor
            )
        ]

        # Contenido de la tabla de citas
        cita_fields.controls = [
            ft.Container(
                content=estilo_tabla(
                    columns=[
                        estilo_encabezado("Nombre"),
                        estilo_encabezado("Especialidad"),
                        estilo_encabezado("Teléfono"),
                        estilo_encabezado("E-mail"),
                    ],
                    rows=[
                        ft.DataRow(cells=[
                            estilo_celda("Juan Pérez"),
                            estilo_celda("Oftalmología"),
                            estilo_celda("666666666"),
                            estilo_celda("juan@ejemplo.com"),
                        ]),
                        ft.DataRow(cells=[
                            estilo_celda("Ana Gómez"),
                            estilo_celda("Pediatría"),
                            estilo_celda("777777777"),
                            estilo_celda("ana@ejemplo.com"),
                        ]),
                        ft.DataRow(cells=[
                            estilo_celda("Carlos López"),
                            estilo_celda("Cardiología"),
                            estilo_celda("888888888"),
                            estilo_celda("carlos@ejemplo.com"),
                        ]),
                    ]
                ),
                alignment=ft.alignment.center,  # Centra la tabla
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.ElevatedButton(
                            text="Volver",
                            width=300,
                            height=50,
                            style=button_style,
                            on_click=volver_a_menu_principal
                        ),
                        ft.ElevatedButton(
                            text="Buscar",
                            width=300,
                            height=50,
                            style=button_style,
                            on_click=mostrar_busqueda
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER  # Centra los botones verticalmente
                ),
                alignment=ft.alignment.center  # Centra toda la columna en el contenedor
            )
        ]

        # Botones principales para seleccionar el tipo de entidad (Paciente, Médico, Cita)
        botones_fields.controls = [
            ft.ElevatedButton(
                text="Paciente",
                width=300,
                height=50,
                style=button_style,
                on_click=lambda e: mostrar_campos("Paciente"),
            ),
            ft.ElevatedButton(
                text="Médico",
                width=300,
                height=50,
                style=button_style,
                on_click=lambda e: mostrar_campos("Médico"),
            ),
            ft.ElevatedButton(
                text="Cita",
                width=300,
                height=50,
                style=button_style,
                on_click=lambda e: mostrar_campos("Cita"),
            ),
            ft.ElevatedButton(
                text="Volver",
                width=300,
                height=50,
                style=button_style,
                on_click=lambda e: ir_a_main("Volver"),
            ),
        ]

        def ir_a_main(e):
            from views import MainView
            # Limpiar la página actual
            self.page.clean()

            # Crear una instancia de MainView y construirla
            main_view = MainView(self.page)
            main_view.build()

        # Agregar los botones y los contenedores dinámicos a la página
        self.page.add(
            ft.Container(
                content=ft.Column(
                    controls=[botones_fields, paciente_fields, medico_fields, cita_fields],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=20,
            )
        )
