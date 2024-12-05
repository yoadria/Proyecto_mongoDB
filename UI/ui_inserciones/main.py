import flet as ft


def main(page: ft.Page):
    page.title = "Inserciones"

    pantalla_formato(page)
    campos_insercion(page)
    botones_inferiores(page)

    page.vertical_alignment = ft.MainAxisAlignment.START  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 

    page.update()


def pantalla_formato(page: ft.Page):
    # Tamaño de la ventana
    page.window_width = 700
    page.window_height = 900

    page.window_resizable = False
    page.window_full_screen = False

    page.update()


def campos_insercion(page: ft.Page):
    # Contenedores dinámicos para mostrar/ocultar los campos
    paciente_fields = ft.Column(visible=False)
    medico_fields = ft.Column(visible=False)
    cita_fields = ft.Column(visible=False)

    # Función para mostrar campos dinámicamente según el botón presionado
    def mostrar_campos(tipo):
        paciente_fields.visible = tipo == "Paciente"
        medico_fields.visible = tipo == "Médico"
        cita_fields.visible = tipo == "Cita"
        page.update()

    # Contenido de los campos dinámicos
    paciente_fields.controls = [
        ft.TextField(label="Nombre del Paciente", width=300),
        ft.TextField(label="Edad del Paciente", width=300),
        ft.TextField(label="Dirección del Paciente", width=300),
        ft.TextField(label="Teléfono del Paciente", width=300),
        ft.TextField(label="E-mail del Paciente", width=300)
    ]

    medico_fields.controls = [
        ft.TextField(label="Nombre del Médico", width=300),
        ft.TextField(label="Especialidad", width=300),
        ft.TextField(label="Teléfono", width=300),
        ft.TextField(label="E-mail del médico", width=300)
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
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[botones, paciente_fields, medico_fields, cita_fields],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            padding=20,
        )
    )
def botones_inferiores(page: ft.Page):
    botones_inferiores = ft.Row(
        controls=[
            ft.ElevatedButton(
                text="Registrar",
                width=200,
                height=50,
            ),
            ft.ElevatedButton(
                text="Borrar",
                width=200,
                height=50,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=15,
    )
    page.add(botones_inferiores)

    


ft.app(main)
