from fastapi import FastAPI, HTTPException
from app.models import RequestData
from app.services.data_processor import DataProcessor

# Initialize FastAPI app
app = FastAPI()

# POST endpoint to process data and return XML response
@app.post("/process_data_inputs")
async def process_data_endpoint(request_data: RequestData):
    """
    Endpoint to process request data and return an XML response.
    """
    # Create DataProcessor instance and process the data
    

    # Return the XML content as part of the response
    
    try:
        processor = DataProcessor(request_data, True)
        xml_content = processor.process() 
        # This will generate and save the XML
        return {"status": "success", "xml_response": xml_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/process_data_outputs")
async def process_data_endpoint(request_data: RequestData):
    """
    Endpoint to process request data and return an XML response.
    """
    # Create DataProcessor instance and process the data
    

    # Return the XML content as part of the response
    
    try:
        processor = DataProcessor(request_data, False)
        xml_content = processor.process() 
        # This will generate and save the XML
        return {"status": "success", "xml_response": xml_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.get("/health_check")
async def health_check():
    """
    Endpoint to process request data and return an XML response.
    """
    try:
        return {"status": "success", "xml_response":"successfull"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))