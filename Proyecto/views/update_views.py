import flet as ft
from services.crud_operations import read_data, update_data

class ModificarViews:
    def __init__(self, page):
        '''Constructor de la clase'''
        self.page = page
        self.collection_name = ""  # Nombre de la colección seleccionada

    def build(self):
        
        '''Método que construye la página Modificar'''
        self.page.title = "Modificar"
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window_width = 800
        self.page.window_height = 600
        self.page.update()

        botones_fields = ft.Column(visible=True)
        buscar_fields = ft.Column(visible=False)
        formulario_fields = ft.Column(visible=False)

        def seleccionar_tipo(tipo):
            '''Método para seleccionar el tipo de búsqueda y mostrar el formulario de búsqueda'''
            self.collection_name = tipo
            botones_fields.visible = False
            buscar_fields.visible = True
            formulario_fields.visible = False

            buscar_fields.controls = [
                ft.TextField(
                    label="DNI" if tipo in ["Pacientes", "Medicos"] else "Nro de Cita",
                    width=300,
                    on_submit=lambda e: buscar_registro(e.control.value),
                ),
                ft.ElevatedButton(
                    text="Buscar",
                    width=300,
                    height=50,
                    on_click=lambda e: buscar_registro(
                        buscar_fields.controls[0].value  # Obtener el valor del TextField
                    ),
                ),
                ft.ElevatedButton(
                    text="Volver",
                    width=300,
                    height=50,
                    on_click=volver_a_menu_principal,
                ),
            ]
            self.page.update()

        def buscar_registro(identificador):
            '''Método para buscar un registro específico'''
            try:
                if not identificador:
                    buscar_fields.controls.append(
                        ft.Text("Por favor, ingrese un identificador válido.", color=ft.colors.RED)
                    )
                    self.page.update()
                    return

                # Filtrar el registro según el DNI o nro_cita
                datos = read_data(self.collection_name)
                filtro = None
                if self.collection_name in ["Pacientes", "Medicos"]:
                    filtro = next((fila for fila in datos if str(fila.get("DNI", "")) == identificador), None)
                elif self.collection_name == "Citas":
                    filtro = next((fila for fila in datos if str(fila.get("nro_cita", "")) == identificador), None)

                if filtro:
                    mostrar_formulario([filtro], list(filtro.keys()))
                else:
                    buscar_fields.controls.append(
                        ft.Text("No se encontró ningún registro con ese identificador.", color=ft.colors.RED)
                    )
                self.page.update()

            except Exception as e:
                buscar_fields.controls.append(
                    ft.Text(f"Error al buscar el registro: {str(e)}", color=ft.colors.RED)
                )
                self.page.update()

        def mostrar_formulario(filas, columnas):
            '''Método para mostrar el formulario de modificación'''
            buscar_fields.visible = False
            formulario_fields.visible = True

            inputs = {
                col: ft.TextField(label=col, value=str(filas[0].get(col, "")), width=300)
                for col in columnas if col not in ["_id", "DNI","nro_cita"]
            }

            formulario_fields.controls = [
                *inputs.values(),
                ft.ElevatedButton(
                    text="Guardar Cambios",
                    width=300,
                    height=50,
                    on_click=lambda e: guardar_cambios(inputs),
                ),
                ft.ElevatedButton(
                    text="Cancelar",
                    width=300,
                    height=50,
                    on_click=volver_a_menu_principal,
                ),
            ]
            self.page.update()

        def guardar_cambios(inputs):
            '''Método para guardar los cambios realizados'''
            try:
                # Obtener los valores del formulario
                nuevos_datos = {key: field.value for key, field in inputs.items()}
                
                # Determinar el filtro de actualización según la colección
                filtro = {}
                if self.collection_name in ["Pacientes", "Medicos"]:
                    filtro = {"DNI": nuevos_datos.get("DNI")}
                elif self.collection_name == "Citas":
                    filtro = {"nro_cita": nuevos_datos.get("nro_cita")}

                #NO DEJAMOS ACTUALIZAR NI EL DNI NI EL NRO CITA
                if "DNI" in filtro:
                    nuevos_datos.pop("DNI", None)
                elif "nro_cita" in filtro:
                    nuevos_datos.pop("nro_cita", None)

                # Llamar a update_data para realizar la actualización
                update_data(self.collection_name, filtro, nuevos_datos)

                # Mostrar mensaje de éxito
                formulario_fields.controls = [
                    ft.Text("Cambios guardados con éxito.", color=ft.colors.GREEN),
                    ft.ElevatedButton(
                        text="Volver",
                        width=300,
                        height=50,
                        on_click=volver_a_menu_principal,
                    ),
                ]

            except Exception as e:
                # Mostrar mensaje de error
                formulario_fields.controls = [
                    ft.Text(f"Error al guardar cambios: {str(e)}", color=ft.colors.RED),
                    ft.ElevatedButton(
                        text="Volver",
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

        botones_fields.controls = [
            ft.ElevatedButton(
                text="Paciente",
                width=300,
                height=50,
                on_click=lambda e: seleccionar_tipo("Pacientes"),
            ),
            ft.ElevatedButton(
                text="Médico",
                width=300,
                height=50,
                on_click=lambda e: seleccionar_tipo("Medicos"),
            ),
            ft.ElevatedButton(
                text="Cita",
                width=300,
                height=50,
                on_click=lambda e: seleccionar_tipo("Citas"),
            ),
        ]

        # Agregar los botones y las secciones dinámicas a la página
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
