# # Placeholder for any business logic (optional for now)
# from xml.sax.handler import version
# import json
#
#
# def generate_consecutive_number(consecutive: int, value: int):
#     return f"{consecutive:0>{value}}"
#
#
# def format_text(text: str, value: int) -> str:
#     return text.ljust(value)
#
#
# def format_number(value: str):
#     # Convert the value to float to handle both int and float types
#     formatted_value = f"{float(value):020.4f}"
#     return formatted_value
#
#
# def process_data(request_data):
#     # Read values from config.json
#     with open('config.json', 'r') as file:
#         config = json.load(file)
#
#     # Extract values for IdCia, Usuario, Clave
#     id_cia = config['IdCia']
#     user = config['Usuario']
#     clave = config['Clave']
#
#     first_line = f"{generate_consecutive_number(1, 7)}0000{ '00'}01{'001'}"
#     consecutive_file = 2
#     consecutive_doc = 1
#     # Initialize an empty list to hold all the Linea elements
#     lines = [f"<Linea>{first_line}</Linea>"]
#     ## Documents
#     for document in request_data.DOCUMENTO:
#         formatted_string_doc = (
#             f"{generate_consecutive_number(consecutive_file, 7)}"  # register_number
#             f"0450"  # type_register
#             f"00"  # subtype
#             f"07"  # version
#             f"001"  # company
#             f"1"  # index_doc
#             f"{format_text(document.ID_CO, 3)}"  # co
#             f"{format_text(document.ID_TIPO_DOCTO, 3)}"  # do_type
#             f"{generate_consecutive_number(consecutive_doc, 8)}"  # do_consecutive
#             f"{document.FECHA}"  # date
#             f"{format_text(' ', 15)}"  # third_party
#             f"061"  # class_do
#             f"1"  # state_do
#             f"0"  # print_state
#             f"{format_text(document.NOTAS, 255)}"  # notes
#             f"601"  # concept
#             f"{format_text(' ', 5)}"  # warehouse_outlet
#             f"{format_text(' ', 5)}"  # warehouse_entry
#             f"{format_text(document.DOCTO_ALTERNO, 15)}"  # alternate_document
#             f"{format_text(' ', 3)}"  # co_empty
#             f"{format_text(' ', 3)}"  # do_type_empty
#             f"{generate_consecutive_number(0, 8)}"  # do_consecutive_empty
#             f"{format_text(' ', 10)}"  # car_code
#             f"{format_text(' ', 15)}"  # transporter_code
#             f"{format_text(' ', 3)}"  # branch_tra_code
#             f"{format_text(' ', 15)}"  # person_code
#             f"{format_text(' ', 15)}"  # person_name
#             f"{format_text(' ', 15)}"  # person_identification
#             f"{format_text(' ', 30)}"  # guide
#             f"{generate_consecutive_number(consecutive_doc, 15)}"  # boxes
#             f"000000000000000.0000"  # weight
#             f"000000000000000.0000"  # volume
#             f"000000000000000.0000"  # insured_value
#             f"{format_text(' ', 255)}"  # empty_notes
#             f"{format_text(' ', 15)}"  # project
#         )
#         lines.append(f"<Linea>{formatted_string_doc}</Linea>")
#         consecutive_file += 1
#         consecutive_doc += 1
#     ## Movements
#     consecutive_mov = 1
#     for movement in request_data.MOVIMIENTO:
#         formatted_string_mov = (
#             f"{generate_consecutive_number(consecutive_file, 7)}"  # register_number
#             f"0450"  # type_register
#             f"00"  # subtype
#             f"07"  # version
#             f"001"  # company
#             f"{format_text(movement.ID_CO, 3)}"  # co
#             f"{format_text(movement.ID_TIPO_DOCTO, 3)}"  # do_type
#             f"{generate_consecutive_number(consecutive_doc, 8)}"  # do_consecutive
#             f"{generate_consecutive_number(consecutive_mov, 8)}"  # register_consecutive
#             f"{format_text(' ', 55)}"  # empty spaces
#             f"{format_text(movement.ID_BODEGA, 5)}"  # warehouse
#             f"{format_text(' ', 10)}"  # location
#             f"{format_text(' ', 15)}"  # lot
#             f"601"  # concept
#             f"{format_text(movement.ID_MOTIVO, 2)}"  # reason
#             f"{format_text(movement.ID_CO_MOVTO, 3)}"  # co_movement
#             f"{format_text(' ', 2)}"  # empty spaces
#             f"{format_text(movement.ID_CCOSTO_MOVTO, 15)}"  # cost_center_movement
#             f"{format_text(' ', 15)}"  # project
#             f"{format_text(movement.ID_UNIDAD_MEDIDA, 4)}"  # measury_unit
#             f"{format_number(movement.CANT_BASE)}"  # amount_base
#             f"000000000000000.0000"  # additional_amount
#             f"{format_number(movement.COSTO_PROM_UNI)}"  # unity_price
#             f"{format_text(movement.NOTAS, 255)}"  # notes
#             f"{format_text(movement.DESC_VARIBLE, 2000)}"  # description
#             f"{format_text(' ', 40)}"  # item_description
#             f"{format_text(movement.UM_INVENTARIO, 4)}"  # measure_unit
#             f"{format_text(' ', 10)}"  # entry_location
#             f"{format_text(' ', 15)}"  # entry_lot
#             f"{generate_consecutive_number(movement.ID_ITEM, 8)}"  # item
#             f"{format_text(' ', 50)}"  # item_reference
#             f"{format_text(' ', 20)}"  # barcode
#             f"{format_text(' ', 20)}"  # extension_1
#             f"{format_text(' ', 20)}"  # extension_2
#             f"{format_text(movement.UN, 20)}"  # business_unit
#             f"00000000"  # rowid
#         )
#         consecutive_mov += 1
#         consecutive_file += 1
#         # Add the formatted string as a Linea element
#         lines.append(f"<Linea>{formatted_string_mov}</Linea>")
#     last_line =  f"{generate_consecutive_number(consecutive_file, 7)}9999{'00'}01{'001'}"
#     lines.append(f"<Linea>{last_line}</Linea>")
#     # Final XML structure
#     xml_content = (
#             "<Importar xmlns:si=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">\n"
#             f"<NombreConexion>UnoEE</NombreConexion>\n"
#             f"<IdCia>{id_cia}</IdCia>\n"
#             f"<Usuario>{user}</Usuario>\n"
#             f"<Clave>{clave}</Clave>\n"
#             "<Datos>\n"
#             + "\n".join(lines) +  # Join all Linea elements
#             "\n</Datos>\n"
#             "</Importar>"
#     )
#
#     # Write to a file
#     with open("generated_data.xml", "w") as file:
#         file.write(xml_content)
#     return request_data
