from fastapi import FastAPI, HTTPException
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
    

    # Return the XML content as part of the response
    
    try:
        processor = DataProcessor(request_data)
        xml_content = processor.process() 
        # This will generate and save the XML
        return {"status": "success", "xml_response": xml_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))