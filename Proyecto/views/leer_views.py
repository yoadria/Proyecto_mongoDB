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
        # Crear columnas de la tabla
        columns = [
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Especialidad")),
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("E-mail"))
        ]
        
        # Crear filas de la tabla
        rows = [
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Juan Pérez")),
                ft.DataCell(ft.Text("Oftalmología")),
                ft.DataCell(ft.Text("666666666")),
                ft.DataCell(ft.Text("juan@ejemplo.com"))
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Ana Gómez")),
                ft.DataCell(ft.Text("32")),
                ft.DataCell(ft.Text("Lima")),
                ft.DataCell(ft.Text("Lima"))
            ]),
            ft.DataRow(cells=[
                ft.DataCell(ft.Text("Carlos López")),
                ft.DataCell(ft.Text("24")),
                ft.DataCell(ft.Text("Ciudad de México")),
                ft.DataCell(ft.Text("Lima"))
            ]),
        ]
        
        # Crear DataTable
        tabla = ft.DataTable(columns=columns, rows=rows)
        
        self.page.add(tabla)
        # Agregar la tabla a la páginaº
        
