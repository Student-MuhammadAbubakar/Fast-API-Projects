from fastapi import FastAPI, HTTPException, status
from typing import Any, Dict
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()
shipments = {
    2021: {
        "Contact no": "030803",
        "Name ": "MUHAMMAD ABUBAKAR",
        "Address": "Faisalabad",
    },
    2022: {
        "Contact no": "03123456789",
        "Name ": "ALI KHAN",
        "Address": "Lahore",
    },
    2023: {
        "Contact no": "03219876543",
        "Name ": "SARA BIBI",
        "Address": "Karachi",
    },
    2024: {
        "Contact no": "03330001122",
        "Name ": "OMAR RAHMAN",
        "Address": "Islamabad",
    },
    2025: {
        "Contact no": "03441234567",
        "Name ": "AYESHA NOOR",
        "Address": "Peshawar",
    },
}


@app.get("/shipment")
def GetShipment(id: int) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id is not found"
        )

    return shipments[id]


@app.post("/shipment")
def submit_shipment(Contact_no: str, Name: str, address: str) -> dict[str, str]:
    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {"Contact no": Contact_no, "Name": Name, "Address": address}
    return {"Id": str(new_id)}


@app.put("/shipment")
def update_shipment(
    id: int, Contact_No: str, Name: str, Address: str
) -> dict[str, Any]:
    shipments[id] = {"Contact no": Contact_No, "Name": Name, "Address": Address}
    return shipments[id]
@app.patch("/shipment")
def Updatesingle(id:int,Contact_no:str|None=None,Name:str|None=None,Address:str|None=None)->Dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id is not found"
        )
    shipment=shipments[id]
    if Contact_no:
        shipment["Contact no"]=Contact_no
    if Name:
        shipment["Name"]=Name
    if Address:
        shipment["Address"]=Address
    shipments[id]=shipment
    return shipment

@app.get("/scalar")
def get_Scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="scalar Api",
    )
