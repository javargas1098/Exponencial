from typing import Any

from zeep import Client
from zeep.exceptions import Fault

SOAP_URL = "http://192.168.100.75/WSUNOEE/WSUNOEE.asmx?wsdl"

# Create a Zeep client
client = Client(SOAP_URL)

def call_siesa_client(data: str, valor: int) -> Any:
    """
    """
    try:
        # Call the ImportarXML method from the SOAP service
        response = client.service.ImportarXML(pvstrDatos=data, printTipoError=valor)
        return response
    except Fault as fault:
        raise fault


