from pydantic import BaseModel
from typing import List

# Define the Pydantic model for "DOCUMENTO"
class DocumentoItem(BaseModel):
    ID_CO: str  # NUM
    ID_TIPO_DOCTO: str  # ALF (EAT o EGC=Entradas)
    FECHA: str  # ALF
    NOTAS: str  # ALF
    DOCTO_ALTERNO: str  # ALF

# Define the Pydantic model for "MOVIMIENTO"
class MovimientoItem(BaseModel):
    ID_CO: str  # NUM
    ID_TIPO_DOCTO: str  # ALF (EAT o EGC=Entradas)
    CONSEC_DOCTO: str  # NUM
    NRO_REGISTRO: str  # NUM
    ID_BODEGA: str  # ALF
    ID_MOTIVO: str  # ALF
    ID_CO_MOVTO: str  # ALF
    ID_CCOSTO_MOVTO: str  # ALF
    ID_UNIDAD_MEDIDA: str  # ALF
    CANT_BASE: str  # NUM
    COSTO_PROM_UNI: str  # NUM
    NOTAS: str  # ALF
    DESC_VARIBLE: str  # ALF
    UM_INVENTARIO: str  # ALF
    ID_ITEM: str  # NUM
    UN: str  # ALF

# Define the main model for the request body
class RequestData(BaseModel):
    DOCUMENTO: List[DocumentoItem]
    MOVIMIENTO: List[MovimientoItem]
