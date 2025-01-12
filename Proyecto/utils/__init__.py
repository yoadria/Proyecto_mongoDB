from .labels import LABELS_MAP, COLUMNAS_MAP, ENCABEZADOS_MAPA
from .style import  button_style, estilo_encabezado, estilo_celda, estilo_tabla
from .validators import validacion_id, validar_email, validar_telefono, validar_dni, validar_edad

__all__ = ["ENCABEZADOS_MAPA","COLUMNAS_MAP","LABELS_MAP", "button_style", "estilo_encabezado", 
           "estilo_celda", "estilo_tabla", "validacion_id", "validar_email", "validar_telefono", 'validar_dni',
           'validar_edad']
