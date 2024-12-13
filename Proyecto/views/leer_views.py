import flet as ft


'''
Fichero que contiene la interfaz para leer los datos
'''

class LeerViews:
    def __init__(self, page):
        '''Constructor de la clase'''

        self.page = page
        self.collection = ""  # esta variable guardara en que coleccion se guardaran los datos depende de los campos desplegados

        self.medico_name = ft.TextField(label="Nombre del Médico", width=300)
        self.medico_especialidad = ft.TextField(label="Especialidad", width=300)
        self.medico_tf = ft.TextField(label="Teléfono", width=300)
        self.medico_email = ft.TextField(label="E-mail del médico", width=300)

    def build(self):

        '''Metodo que construlle la pagina Leer'''

        self.page.title = "Leer"
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window_width = 800
        self.page.window_height = 600

        self.page.update()

        paciente_fields = ft.Column(visible=False)
        medico_fields = ft.Column(visible=False)
        cita_fields = ft.Column(visible=False)
        botones_fields = ft.Column(visible=True)
        # boton_volver = ft.Column(visible=False)

        def mostrar_campos(tipo):
            '''Metodo para mostrar campos dinámicamente según el botón presionado'''
            self.collection = tipo

            botones_fields.visible = False
            paciente_fields.visible = tipo == "Paciente"
            medico_fields.visible = tipo == "Médico"
            cita_fields.visible = tipo == "Cita"
            # boton_volver.visible = tipo == "Volver"
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

        medico_fields.controls = [
            ft.Container(
                content=ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Nombre")),
                        ft.DataColumn(ft.Text("Especialidad")),
                        ft.DataColumn(ft.Text("Teléfono")),
                        ft.DataColumn(ft.Text("E-mail")),
                    ],
                    rows=[
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Juan Pérez")),
                            ft.DataCell(ft.Text("Oftalmología")),
                            ft.DataCell(ft.Text("666666666")),
                            ft.DataCell(ft.Text("juan@ejemplo.com")),
                        ]),
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Ana Gómez")),
                            ft.DataCell(ft.Text("Pediatría")),
                            ft.DataCell(ft.Text("777777777")),
                            ft.DataCell(ft.Text("ana@ejemplo.com")),
                        ]),
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Carlos López")),
                            ft.DataCell(ft.Text("Cardiología")),
                            ft.DataCell(ft.Text("888888888")),
                            ft.DataCell(ft.Text("carlos@ejemplo.com")),
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
                        on_click=volver_a_menu_principal
                    ),
                    ft.ElevatedButton(
                        text="Buscar",
                        width=300,
                        height=50,
                        on_click=volver_a_menu_principal
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER  # Centra los botones verticalmente
            ),
            alignment=ft.alignment.center  # Centra toda la columna en el contenedor
        )     
    ]

        paciente_fields.controls = [
            ft.Container(
                content=ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Nombre")),
                        ft.DataColumn(ft.Text("Especialidad")),
                        ft.DataColumn(ft.Text("Teléfono")),
                        ft.DataColumn(ft.Text("E-mail")),
                    ],
                    rows=[
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Juan Pérez")),
                            ft.DataCell(ft.Text("Oftalmología")),
                            ft.DataCell(ft.Text("666666666")),
                            ft.DataCell(ft.Text("juan@ejemplo.com")),
                        ]),
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Ana Gómez")),
                            ft.DataCell(ft.Text("Pediatría")),
                            ft.DataCell(ft.Text("777777777")),
                            ft.DataCell(ft.Text("ana@ejemplo.com")),
                        ]),
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Carlos López")),
                            ft.DataCell(ft.Text("Cardiología")),
                            ft.DataCell(ft.Text("888888888")),
                            ft.DataCell(ft.Text("carlos@ejemplo.com")),
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
                        on_click=volver_a_menu_principal
                    ),
                    ft.ElevatedButton(
                        text="Buscar",
                        width=300,
                        height=50,
                        on_click=volver_a_menu_principal
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER  # Centra los botones verticalmente
            ),
            alignment=ft.alignment.center  # Centra toda la columna en el contenedor
        )     
    ]

        cita_fields.controls = [
            ft.Container(
                content=ft.DataTable(
                    columns=[
                        ft.DataColumn(ft.Text("Nombre")),
                        ft.DataColumn(ft.Text("Especialidad")),
                        ft.DataColumn(ft.Text("Teléfono")),
                        ft.DataColumn(ft.Text("E-mail")),
                    ],
                    rows=[
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Juan Pérez")),
                            ft.DataCell(ft.Text("Oftalmología")),
                            ft.DataCell(ft.Text("666666666")),
                            ft.DataCell(ft.Text("juan@ejemplo.com")),
                        ]),
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Ana Gómez")),
                            ft.DataCell(ft.Text("Pediatría")),
                            ft.DataCell(ft.Text("777777777")),
                            ft.DataCell(ft.Text("ana@ejemplo.com")),
                        ]),
                        ft.DataRow(cells=[
                            ft.DataCell(ft.Text("Carlos López")),
                            ft.DataCell(ft.Text("Cardiología")),
                            ft.DataCell(ft.Text("888888888")),
                            ft.DataCell(ft.Text("carlos@ejemplo.com")),
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
                        on_click=volver_a_menu_principal
                    ),
                    ft.ElevatedButton(
                        text="Buscar",
                        width=300,
                        height=50,
                        on_click=volver_a_menu_principal
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER  # Centra los botones verticalmente
            ),
            alignment=ft.alignment.center  # Centra toda la columna en el contenedor
        )     
    ]

        botones_fields.controls = [
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
            ft.ElevatedButton(
                text="Volver",
                width=300,
                height=50,
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

        
