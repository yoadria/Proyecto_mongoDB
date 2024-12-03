import flet as ft


def main(page: ft.Page):
    page.title = "Página principal"

    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 


    pantalla_formato(page)
    botones_inferiores(page)

def pantalla_formato(page: ft.Page):
    #tamaño en px
    page.window_width = 400
    page.window_height = 500

    #para que no se pueda redimensionar
    page.window_resizable = False
    page.window_full_screen = False

    page.update()

def botones_inferiores(page: ft.Page):
    #crea un contenedor con los botones alineados en el centro de la pagina
    botones = ft.Container(
        content=ft.Column(
            controls=[
                ft.ElevatedButton(text="Leer Datos", width=300, height=50),
                ft.ElevatedButton(text="Insertar Datos", width=300, height=50),
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
    page.add(ft.Container(height=20))  # Espacio vacío arriba
    page.add(botones)  # Botones en la parte inferior


ft.app(target=main)

