import flet as ft
import time

def main(page: ft.Page):
    page.title = "Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    pantalla_logeo(page)
    campos_logeo(page)


#funcion para dimensionar la pantalla de logeo
def pantalla_logeo(page: ft.Page):
    #tamaño en px
    page.window_width = 350
    page.window_height = 500

    #para que no se pueda redimensionar
    page.window_resizable = False
    page.window_full_screen = False

    page.update()

def campos_logeo(page: ft.Page):
    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )

    page.update()

ft.app(target=main)
