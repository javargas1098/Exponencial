from typing import Any
from zeep import Client, exceptions
from zeep.helpers import serialize_object
from zeep.exceptions import Fault
import logging
from collections import OrderedDict
from lxml import etree 
import json
from zeep.plugins import HistoryPlugin

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SOAP_URL = "http://172.16.0.124/wsunoee/WSUNOEE.asmx?wsdl"

# Create a Zeep client
history = HistoryPlugin()
client = Client(wsdl=SOAP_URL, plugins=[history])

    

def call_siesa_client(data: str, valor: int) -> dict:
    """
    Call the SOAP service ImportarXML method.

    Args:
        data (str): XML content to be sent.
        valor (int): Error handling flag.

    Returns:
        dict: Response from the SOAP service.

    Raises:
        Exception: For any faults or errors during the SOAP call.
    """
    try:
        logger.info("Calling SOAP service")
        # Call the ImportarXML method from the SOAP service
        response = client.service.ImportarXML(pvstrDatos=data, printTipoError=valor)
        response_string = str(serialize_object(response)) 
        logger.info("SOAP service response: %s", response_string)
        return response_string
    except Fault as e:
        logging.error(f"SOAP Fault: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise