import flet as ft

class AlertView:
    def __init__(self, titulo: str, mensaje: str, page: ft.Page):
        """
        Clase para gestionar alertas en Flet.

        Args:
            titulo (str): Título del diálogo.
            mensaje (str): Mensaje del diálogo.
            page (ft.Page): Página donde se mostrará el diálogo.
        """
        self.page = page
        self.titulo = titulo
        self.mensaje = mensaje

        # Crear el diálogo al inicializar
        self.dialog = ft.AlertDialog(
            title=ft.Text(self.titulo, text_align=ft.TextAlign.CENTER),  # Título centrado
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            self.mensaje,
                            text_align=ft.TextAlign.CENTER,  # Texto centrado
                        ),
                        ft.Row(
                            controls=[
                                ft.ElevatedButton(
                                    "Cerrar",
                                    on_click=lambda e: self.close_dialog()
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,  # Botón alineado a la derecha
                        ),
                    ],
                    spacing=20,  # Espacio entre el texto y el botón
                ),
                width=400,
                height=80,
            )
        )
        self.page.dialog = self.dialog  # Asociar el diálogo a la página

    def open_dialog(self):
        """
        Abre el diálogo.
        """
        self.dialog.open = True
        self.page.update()

    def close_dialog(self):
        """
        Cierra el diálogo.
        """
        self.dialog.open = False
        self.page.update()
