from fastapi import HTTPException

from app.services.config import load_config
from app.services.utils import format_text, format_number, generate_consecutive_number, convert_date_to_custom_format
from app.services.siesa_client import call_siesa_client


def generate_xml(id_cia, user, clave, lines):
    """
    Generates the final XML content from the header, body, and footer.
    """
    # Final XML structure
    print(" llegue acaca")
    xml_content = (
            "<Importar xmlns:si=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">\n"
            f"<NombreConexion>Pruebas</NombreConexion>\n"
            f"<IdCia>{id_cia}</IdCia>\n"
            f"<Usuario>{user}</Usuario>\n"
            f"<Clave>{clave}</Clave>\n"
            "<Datos>\n"
            + "\n".join(lines) +  # Join all Linea elements
            "\n</Datos>\n"
            "</Importar>"
    )

    try:
        with open("generated_data.xml", 'w', encoding='utf-8') as file:
            file.write(xml_content)
        print(f"XML content has been successfully saved to generated_data.xml")
    except Exception as e:
        print(f"Error saving XML data: {e}")
    try:
        # Call the SOAP service with the provided data and flag
        tipo_error = 0
        response = call_siesa_client(xml_content, tipo_error)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class DataProcessor:
    def __init__(self, request_data):
        self.request_data = request_data
        self.config = load_config()  # Load config

    def process(self):
        """
        Main processing function to generate XML data.
        """
        # Extract values for IdCia, Usuario, Clave
        id_cia = self.config['IdCia']
        user = self.config['Usuario']
        clave = self.config['Clave']

        first_line = f"{generate_consecutive_number(1, 7)}0000{'00'}01{'001'}"
        consecutive_file = 2
        consecutive_doc = 1
        # Initialize an empty list to hold all the Linea elements
        lines = [f"<Linea>{first_line}</Linea>"]

        # Process Documents and update consecutive_file
        consecutive_file = self.process_documents(consecutive_file, consecutive_doc, lines)

        # Process Movements and update consecutive_file
        consecutive_file = self.process_movements(consecutive_file, consecutive_doc, lines)

        # Final Line
        last_line = f"{generate_consecutive_number(consecutive_file, 7)}9999{'00'}01{'001'}"
        lines.append(f"<Linea>{last_line}</Linea>")

        # Generate Final XML content
        return generate_xml(id_cia, user, clave, lines)

    def process_documents(self, consecutive_file, consecutive_doc, lines):
        """
        Processes the document data and returns a list of formatted lines for the documents.
        """
        for document in self.request_data.DOCUMENTO:
            formatted_string_doc = (
                f"{generate_consecutive_number(consecutive_file, 7)}"  # register_number
                f"0450"  # type_register
                f"00"  # subtype
                f"07"  # version
                f"001"  # company
                f"1"  # index_doc
                f"{format_text(document.ID_CO, 3)}"  # co
                f"{format_text(document.ID_TIPO_DOCTO, 3)}"  # do_type
                f"{generate_consecutive_number(consecutive_doc, 8)}"  # do_consecutive
                f"{convert_date_to_custom_format(document.FECHA)}"  # date
                f"{format_text(document.ID_TERCERO, 15)}"  # third_party
                f"061"  # class_do
                f"1"  # state_do
                f"0"  # print_state
                f"{format_text(document.NOTAS, 255)}"  # notes
                f"601"  # concept
                f"{format_text(' ', 5)}"  # warehouse_outlet
                f"{format_text(' ', 5)}"  # warehouse_entry
                f"{format_text(document.DOCTO_ALTERNO, 15)}"  # alternate_document
                f"{format_text(' ', 3)}"  # co_empty
                f"{format_text(' ', 3)}"  # do_type_empty
                f"{generate_consecutive_number(0, 8)}"  # do_consecutive_empty
                f"{format_text(' ', 10)}"  # car_code
                f"{format_text(' ', 15)}"  # transporter_code
                f"{format_text(' ', 3)}"  # branch_tra_code
                f"{format_text(' ', 15)}"  # person_code
                f"{format_text(' ', 50)}"  # person_name
                f"{format_text(' ', 15)}"  # person_identification
                f"{format_text(' ', 30)}"  # guide
                f"{format_number(0,15)}"  # boxes
                f"000000000000000.0000"  # weight
                f"000000000000000.0000"  # volume
                f"000000000000000.0000"  # insured_value
                f"{format_text(' ', 255)}"  # empty_notes
                f"{format_text(' ', 15)}"  # project
            )
            lines.append(f"<Linea>{formatted_string_doc}</Linea>")
            consecutive_file += 1
            consecutive_doc += 1
        return consecutive_file

    def process_movements(self, consecutive_file, consecutive_doc, lines):
        """
        Processes the movement data and returns a list of formatted lines for the movements.
        """
        consecutive_mov = 1
        for movement in self.request_data.MOVIMIENTO:
            formatted_string_mov = (
                f"{generate_consecutive_number(consecutive_file, 7)}"  # register_number
                f"0470"  # type_register
                f"00"  # subtype
                f"06"  # version
                f"001"  # company
                f"{format_text(movement.ID_CO, 3)}"  # co
                f"{format_text(movement.ID_TIPO_DOCTO, 3)}"  # do_type
                f"{generate_consecutive_number(consecutive_doc, 8)}"  # do_consecutive
                f"{generate_consecutive_number(consecutive_mov, 10)}"  # register_consecutive
                f"{format_text(' ', 55)}"  # empty spaces 
                f"{format_text(movement.ID_BODEGA, 5)}"  # warehouse
                f"{format_text(' ', 10)}"  # location
                f"{format_text(' ', 15)}"  # lot
                f"601"  # concept
                f"{format_text(movement.ID_MOTIVO, 2)}"  # reason
                f"{format_text(movement.ID_CO_MOVTO, 3)}"  # co_movement
                f"{format_text(' ', 2)}"  # empty spaces 
                f"{format_text(movement.ID_CCOSTO_MOVTO, 15)}"  # cost_center_movement
                f"{format_text(' ', 15)}"  # project
                f"{format_text(movement.ID_UNIDAD_MEDIDA, 4)}"  # measury_unit
                f"{format_number(movement.CANT_BASE,20)}"  # amount_base
                f"{format_number(1,20)}" # additional_amount
                f"{format_number(movement.COSTO_PROM_UNI,20)}"  # unity_price
                f"{format_text(movement.NOTAS, 255)}"  # notes
                f"{format_text(movement.DESC_VARIBLE, 2000)}"  # description
                f"{format_text(' ', 40)}"  # item_description
                f"{format_text(movement.UM_INVENTARIO, 4)}"  # measure_unit
                f"{format_text(' ', 10)}"  # entry_location
                f"{format_text(' ', 15)}"  # entry_lot
                f"{generate_consecutive_number(movement.ID_ITEM, 7)}"  # item
                f"{format_text(' ', 50)}"  # item_reference
                f"{format_text(' ', 20)}"  # barcode
                f"{format_text(' ', 20)}"  # extension_1
                f"{format_text(' ', 20)}"  # extension_2
                f"{format_text(movement.ID_UN, 20)}"  # business_unit
                f"{generate_consecutive_number(0, 8)}"  # do_consecutive_empty # rowid
            )
            lines.append(f"<Linea>{formatted_string_mov}</Linea>")
            consecutive_file += 1
            consecutive_mov += 1
        return consecutive_file
