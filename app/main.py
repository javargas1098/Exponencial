from fastapi import FastAPI
from app.models import RequestData
from app.services.data_processor import DataProcessor

# Initialize FastAPI app
app = FastAPI()

# POST endpoint to process data and return XML response
@app.post("/process_data")
async def process_data_endpoint(request_data: RequestData):
    """
    Endpoint to process request data and return an XML response.
    """
    # Create DataProcessor instance and process the data
    print(" ekldkndaeklnd")
    processor = DataProcessor(request_data)
    xml_content = processor.process()  # This will generate and save the XML

    # Return the XML content as part of the response
    return {"status": "success", "xml_data": xml_content}