import flet as ft
from utils.style import button_style  # Importar los estilos

class DeleteView:
    def __init__(self, page):
        '''Constructor de la clase'''
        self.page = page

    def build(self):
        '''Método que construye la página Eliminar'''
        self.page.title = "Eliminar"
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.update()

        botones_fields = ft.Column(visible=True)
        buscar_fields = ft.Column(visible=False)
        formulario_fields = ft.Column(visible=False)

        def seleccionar_tipo(tipo):
            '''Método para seleccionar el tipo de búsqueda y mostrar el formulario de búsqueda'''
            botones_fields.visible = False
            buscar_fields.visible = True
            formulario_fields.visible = False

            buscar_fields.controls = [
                ft.TextField(
                    label="DNI" if tipo in ["Pacientes", "Medicos"] else "Nro de Cita",
                    width=300,
                    on_submit=lambda e: mostrar_formulario(),
                    color=ft.Colors.BLACK
                ),
                ft.ElevatedButton(
                    text="Buscar",
                    style=button_style,
                    width=300,
                    height=50,
                    on_click=lambda e: mostrar_formulario(),
                ),
                ft.ElevatedButton(
                    text="Volver",
                    style=button_style,
                    width=300,
                    height=50,
                    on_click=volver_a_menu_principal,
                ),
            ]
            self.page.update()

        def mostrar_formulario():
            '''Método para mostrar la información del registro y el botón de eliminar'''
            buscar_fields.visible = False
            formulario_fields.visible = True

            formulario_fields.controls = [
                ft.TextField(label="Nombre", value="Nombre Ejemplo", width=300, read_only=True),
                ft.TextField(label="Apellido", value="Apellido Ejemplo", width=300, read_only=True),
                ft.TextField(label="DNI/Nro de Cita", value="12345678", width=300, read_only=True),
                ft.ElevatedButton(
                    text="Eliminar",
                    style=button_style,
                    width=300,
                    height=50,
                    on_click=confirmar_eliminacion,
                ),
                ft.ElevatedButton(
                    text="Cancelar",
                    style=button_style,
                    width=300,
                    height=50,
                    on_click=volver_a_menu_principal,
                ),
            ]
            self.page.update()

        def confirmar_eliminacion(e):
            '''Método para mostrar un diálogo de confirmación de eliminación'''
            dialogo = ft.AlertDialog(
                title=ft.Text("Confirmación"),
                content=ft.Text("¿Está seguro que desea eliminar este registro?"),
                actions=[
                    ft.TextButton("Cancelar", on_click=lambda e: self.page.dialog.dismiss()),
                    ft.TextButton("Confirmar", on_click=lambda e: mostrar_exito())
                ]
            )
            self.page.dialog = dialogo
            dialogo.open = True
            self.page.update()

        def mostrar_exito():
            '''Método para mostrar un mensaje de éxito'''
            self.page.dialog.dismiss()
            formulario_fields.controls = [
                ft.Text("Registro eliminado con éxito.", color=ft.colors.GREEN),
                ft.ElevatedButton(
                    text="Volver",
                    style=button_style,
                    width=300,
                    height=50,
                    on_click=volver_a_menu_principal,
                ),
            ]
            self.page.update()

        def volver_a_menu_principal(e=None):
            '''Método para volver al menú principal'''
            botones_fields.visible = True
            buscar_fields.visible = False
            formulario_fields.visible = False
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
                on_click=lambda e: seleccionar_tipo("Pacientes"),
            ),
            ft.ElevatedButton(
                text="Médico",
                style=button_style,
                width=300,
                height=50,
                on_click=lambda e: seleccionar_tipo("Medicos"),
            ),
            ft.ElevatedButton(
                text="Cita",
                style=button_style,
                width=300,
                height=50,
                on_click=lambda e: seleccionar_tipo("Citas"),
            ),
            ft.ElevatedButton(
                text="Volver",
                style=button_style,
                width=300,
                height=50,
                on_click=lambda e: ir_a_main("Volver"),
            )
        ]

        self.page.add(
            ft.Container(
                content=ft.Column(
                    controls=[botones_fields, buscar_fields, formulario_fields],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=20,
            )
        )
