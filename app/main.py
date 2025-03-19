from fastapi import FastAPI, HTTPException
from app.models import RequestData
from app.services.data_processor import DataProcessor

# Initialize FastAPI app
app = FastAPI(title="Exponencial API", description="API for Processing Data", version="1.0.0")

# POST endpoint to process data inputs
@app.post("/process_data_inputs")
async def process_data_inputs(request_data: RequestData):
    """
    Endpoint to process input data and return an XML response.
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

# POST endpoint to process data outputs   
@app.post("/process_data_outputs")
async def process_data_outputs(request_data: RequestData):
    """
    Endpoint to process output  data and return an XML response.
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
    

# Health check endpoint   
@app.get("/health_check")
async def health_check():
    """
    Check API health status.
    """
    return {"status": "success", "message": "Service is running"}