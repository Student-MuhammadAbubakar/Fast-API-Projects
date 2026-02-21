from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference 
app=FastAPI()


@app.get("/shipment")
def GetShipment():
    return{"Contact no":"030803",
    "Name ":"MUHAMMAD ABUBAKAR",
    "Address":"Faisalabad",}

@app.get("/scalar")
def get_Scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="scalar Api",
    )