from fastapi import FastAPI, HTTPException, status
from typing import Any
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

@app.delete("/shipment")
def delete_shipment(id:int)->dict[str,str]:
    shipments.pop(id)
    return{"detail":f"The shipment with id # {id} has been deleleted...."}
@app.get("/scalar")
def get_Scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="scalar Api",
    )
