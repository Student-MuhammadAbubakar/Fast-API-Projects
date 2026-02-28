from fastapi import FastAPI, HTTPException,status
from typing import Any
from scalar_fastapi import get_scalar_api_reference 
from .scheme import Shipment
from .database import save, shipments
app=FastAPI()


@app.get("/shipment")
def GetShipment(id: int):
    if id  not in shipments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
                            ,detail="Id is not found")
        
    return shipments[id]
@app.post("/shipment")
def submit_shipment(shipment:Shipment)->dict[str,str]:
    new_id=max(shipments.keys())+1
    shipments[new_id]={"ID":new_id,"Contact_no":shipment.Contact_no,"Name":shipment.Name,"Address":shipment.Address}
    save()
    return{"Id":str(new_id)}
@app.put("/shipment")
def update_shipment(
    id: int, Contact_No: str, Name: str, Address: str
) -> dict[str, Any]:
    shipments[id] = {"ID":id,"Contact_no": Contact_No, "Name": Name, "Address": Address}
    save()
    return shipments[id]

@app.get("/scalar")
def get_Scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="scalar Api",
    )