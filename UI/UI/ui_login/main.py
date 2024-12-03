import flet as ft
import time

def main(page: ft.Page):
    page.title = "Login"

    pantalla_logeo(page)
    campos_logeo(page)
    # Centrar todo el contenido de la página
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

#funcion para dimensionar la pantalla de logeo
def pantalla_logeo(page: ft.Page):
    #tamaño en px
    page.window_width = 350
    page.window_height = 500

    #para que no se pueda redimensionar
    page.window_resizable = False
    page.window_full_screen = False

    page.update()

# Función para agregar los campos de inicio de sesión
def campos_logeo(page: ft.Page):
    # Crear los campos centrados dentro de una columna
    campos = ft.Container(
        content=ft.Column(controls=[
            ft.Row(controls=[ft.Text("Username: ", size=14, weight="bold")],alignment="center"),
            ft.Row(controls=[ft.TextField(label="Username ", width=200)],alignment="center"),
            ft.Row(controls=[ft.Text("Password: ", size=14, weight="bold")],alignment="center"),
            ft.Row(controls=[ft.TextField(label="Password ", width=200)],alignment="center"),
            ft.Row(controls=[ft.ElevatedButton(text="login", width=200)],alignment="center")
        ]),
        margin=ft.Margin(top=100, left=0, right=0, bottom=0),
        # alignment=ft.MainAxisAlignment.CENTER,  # Centrar los controles verticalmente
        # horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Centrar los controles horizontalmente
    )

    # Agregar la columna a la página
    page.add(campos)

ft.app(target=main)
